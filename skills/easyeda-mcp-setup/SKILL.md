---
name: easyeda-mcp-setup
description: "连接或排查嘉立创 EDA 内置 MCP，诊断 macOS 启动 EPERM、会话为空和原生工具发现问题。"
license: Apache-2.0
metadata:
  source-kind: extension-derived
---

# easyeda-mcp-setup

连接或排查嘉立创 EDA 内置 MCP，诊断 macOS 启动 EPERM、会话为空和原生工具发现问题。

## 首次使用

读取 [原生 MCP 约定](references/native-mcp.md)，按真实工具返回执行 help、doctor、session.list。
不要把工程为空或扩展未安装解释为需要切换到 WebSocket Gateway。

## 当前任务

需要明确：已安装客户端的位置；本机 MCP 地址；期望只读验证的工程。

1. 先用原生 MCP initialize/tools/list 确认服务身份。
2. 调用 help 后查询 doctor 与 session.list。
3. macOS 直接启动出现文稿权限对话框时，显式使用 LaunchServices 启动原生 HTTP 服务。
4. 只读查询选定会话的当前工程与文档。
5. 记录客户端版本、桥接状态和实际返回，不为 null 伪造项目。

## 验证结果

- 服务名为 JLCEDA Pro 或 EasyEDA Pro。
- bridge connected 与 versionMatch 分别检查。
- 保留原有宿主配置。

## 容易出错的地方

- 不得靠增加 timeout 掩盖原生权限对话框。
- 不要同时安装 Gateway 路径来替代原生 MCP 故障定位。

## 使用示例

“连接本地专业版，仅验证能否读取工程。”

具体 API 入口、来源和执行范围见 [操作参考](references/operations.md)。

来源性质：从官方扩展与接口提炼的领域工作流。本技能的存在不代表上游扩展已安装或工作流已实测。

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
