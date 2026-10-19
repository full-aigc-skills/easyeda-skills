---
name: easyeda-extension-use
description: "通过嘉立创 EDA 内置 MCP 调用 EasyEDA MCP 的 .eext 领域接口，发现能力、只读检查工程，并按授权设计、布线和导出。"
license: Apache-2.0
metadata:
  source-kind: extension-derived
---

# easyeda-extension-use

通过嘉立创 EDA 内置 MCP 调用 EasyEDA MCP 的 .eext 领域接口，发现能力、只读检查工程，并按授权设计、布线和导出。

## 首次使用

读取 [原生 MCP 约定](references/native-mcp.md)，按真实工具返回执行 help、doctor、session.list。
不要把工程为空或扩展未安装解释为需要切换到 WebSocket Gateway。

## 当前任务

需要明确：目标会话及已安装的 easyeda-mcp 扩展；目标工程和活动文档的真实 UUID；只读、工程修改或输出文件的授权范围。

1. 先确认 functions 中 easyeda-mcp 已启用，不把 Agent 插件安装视为 .eext 已安装。
2. 先查询 doc.external 的 easyedaMcp 组；BRIDGE_NOT_READY 时通过 invoke 调用 eda.sys_Help.help("external","easyedaMcp")。
3. 用 invoke 调用 external.easyedaMcp.getCapabilities({}) 和 inspectProject({})，逐层检查返回值。
4. no_project 表示没有工程，project_only 表示工程已打开但没有活动图页；修改需要明确 projectUuid 和 documentUuid。
5. 根据任务调用已发现的领域接口；修改模式由用户在 EDA 确认，参数不能开启权限。
6. 用器件、引脚、网表和 DRC 回读；导出检查真实文件，超时后先核对已发生的变化。

## 验证结果

- 已确认内部扩展 UUID、版本、启用状态与接口目录。
- 只读任务没有调用工程修改、保存或制造导出。
- 工程、文档、对象和实际输出分别验证。

## 容易出错的地方

- doc.external 在某些主页 render 不可用，不能据此认为实际 external 接口断开。
- 原理图坐标为 10mil、PCB 为 mil，创建返回值不等于电气或制造通过。
- filesystem 需要客户端外部交互权限；保存窗口取消不能报告为落盘成功。

## 使用示例

“使用已安装的 EasyEDA MCP 扩展，只读检查当前工程和原理图器件。”

具体 API 入口、来源和执行范围见 [操作参考](references/operations.md)。

来源性质：从官方扩展与接口提炼的领域工作流。本技能的存在不代表上游扩展已安装或工作流已实测。

先读 [内部扩展调用](references/eext-integration.md)，包含 14 个领域接口与实测帮助查询替代路径。
