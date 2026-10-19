"""从领域目录生成自包含技能；运行 --check 只检查一致性。"""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NATIVE_GUIDE = """# 内置 MCP 调用约定

只使用客户端原生 MCP；不要求安装 Run API Gateway 或启动 easyeda-bridge。
国内 CLI 常用 lceda-pro，国际版为 easyeda-pro；桌面客户端要求 4.1.60 或以上。
工具名以 tools/list 的真实返回为准，本机实测是 LCEDA-Pro.help、LCEDA-Pro.discover、LCEDA-Pro.call。

## 首次调用

1. 调用实际前缀的 help，参数 `{}`。
2. 调用实际 call，参数 `{"path":"doctor","input":{}}`。
3. 调用实际 call，参数 `{"path":"session.list","input":{}}`。
4. 选择 alive 会话并核对用户指定工程；多会话不随意选择。

原生 call 接收 `{path, input}`，不是直接接收 eda.* 方法名。实际返回包含 MCP
isError、原生命令 ok 和 data（部分版本为 value）。必须检查每一层，再解释业务结果。

## API 渐进查询

先调用 help `{"path":"doc.api"}`，再用 call 查询：

```json
{"path":"doc.api","input":{"className":"DMT_Project","methodName":"getCurrentProjectInfo"}}
```

按当前客户端类型查询 mount、重载、枚举、参数和返回。类名与 eda 挂载名不是同一个字符串；
例如 DMT_Project 通常挂载为 dmt_Project。未知接口先 discover/help，不编造工具或字段。
某些能力依赖 .eext：查询 doc.external 和 functions 判断是否真实暴露；只有菜单没有上层接口
时，不能声称可通过原生 MCP 全自动调用。需要安装、开发或增加接口时说明具体缺口。

## 扩展调用的权限上下文

调用自研 `external.easyedaMcp.*` 时，从 `functions` 核对扩展名 easyeda-mcp 的真实 UUID，
并在 invoke.input 中传入 extUuid。本机扩展为 `b0f54bac131848dab885c8215a0ac81c`。
省略 extUuid 会使用独立脚本上下文，面板已经确认允许修改时仍可能读到 READ_ONLY。
不能使用内置 eda 身份冒充本扩展，不能在外部请求中用 writeEnabled=true 开启写入。
原生 eda API 与外部扩展接口使用各自的实际权限上下文；先读回能力，再调用已授权的目标。

复制或移动本地 .eprj3 后，工程 UUID 可能随路径变化，必须重新读取；文档 UUID 相同也不能继续复用旧工程 UUID。
导入 PCB 的 importChanges 返回 true 可能只是打开确认窗口，应用后须回读实际器件/网络。
openDocument 超时也可能已经打开图页，先回读活动文档与路径；不重放可能已生效的写入。

## 只读工程查询

查询 invoke 帮助后调用 call，session 必须替换为 session.list 返回的真实 ID：

```json
{"path":"invoke","input":{"session":"实际会话ID","extUuid":"eda","timeout":15000,"code":"return {project:(await eda.dmt_Project.getCurrentProjectInfo()) ?? null,currentDocument:(await eda.dmt_SelectControl.getCurrentDocumentInfo()) ?? null};"}}
```

project 为 null 时说明当前窗口没有工程；不要自动打开最近工程或安装 Gateway。
先回读对象 ID、位号、引脚与真实坐标，再执行具体操作。原理图坐标单位通常为 10mil，PCB 为 mil；
用当前类型定义核对单位、轴向、画布原点和数据原点，不靠图形观感猜坐标。

## 写入与完成判断

只读任务不调用 create/modify/delete/save/export。已授权生成或修改任务可执行范围内操作，
保留已有修改；批量或替换操作先用候选副本。单次调用失败或超时后先回读，不盲目重放可能已经生效的写入。
很多 API 依赖当前活动图页，打开目标文档后核对实际激活状态；等待拓扑计算稳定后再做网表和 DRC 查询。
按目标版本查询计算状态；缺少状态 API 时采用有期限的回读，而不是永久等待。

MCP 响应成功不等于几何、连通或制造正确。依次核对返回对象、实际网表/DRC、保存后重新打开、
实际导出文件与预览。没有运行的层次写明未验证。自动布线、制造导出等 Beta 接口需按客户端版本适配。
本包不会提供自动下单或付款授权。

## 自包含安装

每个技能的参考文件位于自己的 references/。需要另一技能时按名称调用；单独安装：
`npx skills add full-aigc-skills/easyeda-skills --skill 技能名`。
此命令是发布后的安装方式，本地未发布候选请使用当前加载的真实目录，不假定远端已经存在。
"""


def outputs():
    suite = json.loads((ROOT / 'catalog.json').read_text())
    lock = json.loads((ROOT / 'source-lock.json').read_text())
    sources = {r['repository']: r for r in lock['records']}
    result = {}
    for item in suite['skills']:
        name = item['name']
        base = Path('skills') / name
        description = json.dumps(item['description'], ensure_ascii=False)
        source_kind = '官方技能整合，已将传输改为内置 MCP' if item['upstreamSkill'] else '从官方扩展与接口提炼的领域工作流'
        body = f'''---
name: {name}
description: {description}
license: Apache-2.0
metadata:
  source-kind: {item['origin']}
---

# {name}

{item['description']}

## 首次使用

读取 [原生 MCP 约定](references/native-mcp.md)，按真实工具返回执行 help、doctor、session.list。
不要把工程为空或扩展未安装解释为需要切换到 WebSocket Gateway。

## 当前任务

需要明确：{'；'.join(item['inputs'])}。

'''
        body += '\n'.join(f'{i}. {step}。' for i, step in enumerate(item['steps'], 1))
        body += '\n\n## 验证结果\n\n' + '\n'.join('- ' + value + '。' for value in item['checks'])
        body += '\n\n## 容易出错的地方\n\n' + '\n'.join('- ' + value + '。' for value in item['pitfalls'])
        body += f'\n\n## 使用示例\n\n“{item["example"]}”\n\n'
        body += '具体 API 入口、来源和执行范围见 [操作参考](references/operations.md)。\n'
        body += f'\n来源性质：{source_kind}。本技能的存在不代表上游扩展已安装或工作流已实测。\n'
        if item['upstreamSkill']:
            body += f'上游技能名：`{item["upstreamSkill"]}`；这里为中文整理与原生 MCP 适配版本。\n'
            body += '\n## 已随包携带的官方完整资源\n\n'
            body += '先读 [包内资源与内置 MCP 适配](references/bundled-official.md)，再按任务读取 '
            body += '[完整官方原文](upstream/SKILL.md)。原文、脚本、Schema、样例和配套资料已随本技能携带。\n'
            body += '官方原文中的 WebSocket Bridge、旧安装路径或 companion 旧仓库名仅作来源记录；'
            body += '实时编辑始终使用上述原生 MCP，离线工具使用本技能内的实际路径。不要启动 upstream/scripts/bridge-server.mjs。\n'
        if name == 'easyeda-extension-use':
            body += '\n先读 [内部扩展调用](references/eext-integration.md)，包含 14 个领域接口与实测帮助查询替代路径。\n'
        if name == 'easyeda-use':
            body += '\n完整任务从 easyeda-end-to-end 开始；专门操作按技能名称分派。单独安装：'
            body += '`npx skills add full-aigc-skills/easyeda-skills --skill easyeda-end-to-end`。\n'
        if name == 'easyeda-mcp-setup':
            body += '''
## 本地诊断脚本

脚本支持 start、doctor、sessions、current-project、api-help；没有任意工程写入入口。
使用当前已加载技能目录中的脚本；挂载型宿主可使用：

```bash
python3 -B /mnt/skills/user/easyeda-mcp-setup/scripts/native_mcp.py doctor
python3 -B /mnt/skills/user/easyeda-mcp-setup/scripts/native_mcp.py current-project --session 实际会话ID
```

普通文件系统宿主请换成当前加载目录的绝对路径。默认地址为
`http://127.0.0.1:31637/mcp`；可用 --endpoint 指定其他 loopback 地址。
仅当用户要求启动服务时运行 start；它不安装客户端、不更改系统权限、不打开工程。
'''
        result[base / 'SKILL.md'] = body
        result[base / 'references/native-mcp.md'] = NATIVE_GUIDE
        operations = '# 操作参考\n\n## 第一个工具调用\n\n'
        operations += '调用 tools/list 实际返回的原生 `.help`，参数 `{}`，再查询 `doc.api` 帮助。\n'
        operations += '本工作流首先查询以下类，具体方法、参数、返回以当前客户端帮助为准：\n\n'
        for cls in item['classes']:
            operations += '```json\n' + json.dumps({'path': 'doc.api', 'input': {'className': cls}}, ensure_ascii=False) + '\n```\n\n'
        operations += '之后在选定会话中通过原生 `invoke` 执行已查询的 API。涉及扩展时先查询 '
        operations += '`doc.external` 或 `functions`，确认上层接口实际存在；未暴露时报告缺口，不把源代码函数名直接当成工具。\n'
        if item['upstreamSkill']:
            operations += '\n先阅读 [官方技能适配细则](official-adaptation.md)，其中保留领域关键约束与未捆绑工具的获取方式。\n'
        operations += '\n## 完成判据\n\n' + '\n'.join('- ' + c + '。' for c in item['checks'])
        operations += '\n\n## 官方来源\n\n'
        for repo in item['sources']:
            record = sources[repo]
            paths = [f for f in record['files'] if f['path'].endswith('.ts') or f['path'] in ['SKILL.md', 'cli-for-ai.md']]
            if not paths:
                paths = record['files'][:1]
            operations += f'- [{repo}](https://github.com/easyeda/{repo}/tree/{record["revision"]})，修订 `{record["revision"]}`。\n'
            operations += ''.join(f'  - [{f["path"]}]({f["url"]})\n' for f in paths[:3])
        operations += '\n这些链接是固定版本的知识来源，不会自动安装、运行上游扩展。'
        operations += '文档/源码证据与真实客户端、板卡、制造验证分开记录。\n'
        result[base / 'references/operations.md'] = operations
        result[base / 'agents/openai.yaml'] = (
            'interface:\n  display_name: ' + json.dumps('EasyEDA · ' + name.removeprefix('easyeda-'), ensure_ascii=False)
            + '\n  short_description: ' + json.dumps(item['description'][:64], ensure_ascii=False)
            + '\n  default_prompt: ' + json.dumps('使用 $' + name + ' 处理我的嘉立创 EDA 任务。', ensure_ascii=False)
            + '\n')
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    mismatch = []
    files = outputs()
    for relative, text in files.items():
        target = ROOT / relative
        if target.is_symlink() or not target.resolve().is_relative_to(ROOT.resolve()):
            raise ValueError('技能输出路径越界：' + str(relative))
        if args.check:
            if not target.is_file() or target.read_text() != text:
                mismatch.append(str(relative))
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(text)
    if mismatch:
        raise SystemExit('技能生成结果与目录不一致：' + ', '.join(mismatch))
    print(json.dumps({'ok': True, 'files': len(files), 'checkOnly': args.check}, ensure_ascii=False))


if __name__ == '__main__':
    main()
