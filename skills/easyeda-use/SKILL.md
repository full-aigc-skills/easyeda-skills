---
name: easyeda-use
description: "使用嘉立创 EDA / EasyEDA 完成设计、检查或导出时选择对应技能；执行入口为客户端内置 MCP。"
license: Apache-2.0
metadata:
  source-kind: extension-derived
---

# easyeda-use

使用嘉立创 EDA / EasyEDA 完成设计、检查或导出时选择对应技能；执行入口为客户端内置 MCP。

## 首次使用

读取 [原生 MCP 约定](references/native-mcp.md)，按真实工具返回执行 help、doctor、session.list。
不要把工程为空或扩展未安装解释为需要切换到 WebSocket Gateway。

## 当前任务

需要明确：目标工程或新工程位置；只读、修改或生成的范围；希望得到的工程和导出文件。

1. 先发现原生 help/discover/call 工具并查询 doctor。
2. 列出会话，匹配用户指定工程；无工程则报告而不打开最近项。
3. 按任务选择本包对应技能，保持原有授权范围。
4. 在目标客户端查询 API 签名后执行。
5. 按实际操作回读对象、网表或文件，分别报告未完成项。

## 验证结果

- 会话、工程和目标文档匹配。
- 没有将静态文档当成执行结果。
- 交付包含可继续编辑的工程。

## 容易出错的地方

- 标准版与专业版的 API 和格式不同。
- MCP 可连接不代表已经打开工程。

## 使用示例

“只读检查我当前的原理图，先告诉我工程名称。”

具体 API 入口、来源和执行范围见 [操作参考](references/operations.md)。

来源性质：从官方扩展与接口提炼的领域工作流。本技能的存在不代表上游扩展已安装或工作流已实测。

完整任务从 easyeda-end-to-end 开始；专门操作按技能名称分派。单独安装：`npx skills add full-aigc-skills/easyeda-skills --skill easyeda-end-to-end`。
