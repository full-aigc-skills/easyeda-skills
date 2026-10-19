# 内置 MCP 调用约定

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
