---
name: easyeda-documentation
description: "根据实际 EasyEDA 工程生成设计说明、统计报告、Markdown/LaTeX 注释或 PLM 对接资料。"
license: Apache-2.0
metadata:
  source-kind: extension-derived
---

# easyeda-documentation

根据实际 EasyEDA 工程生成设计说明、统计报告、Markdown/LaTeX 注释或 PLM 对接资料。

## 首次使用

读取 [原生 MCP 约定](references/native-mcp.md)，按真实工具返回执行 help、doctor、session.list。
不要把工程为空或扩展未安装解释为需要切换到 WebSocket Gateway。

## 当前任务

需要明确：目标读者和格式；工程范围；允许导出的信息。

1. 读取工程、BOM、网络和必要统计。
2. 区分实测数据、计算结果与未验证设计说明。
3. 按用户需要生成文档、公式或报告。
4. 核对文档中的位号、网络、版本和输出文件。
5. 外发或写入 PLM 只在明确授权后进行。

## 验证结果

- 统计来自实际工程。
- 生成文字不冒充测试报告。
- 文档链接指向有效交付文件。

## 容易出错的地方

- 通用 LLM 生成说明可能包含不存在的功能。
- 报告中的网络长度不能自动当作时序结论。

## 使用示例

“为当前板卡生成含 BOM、接口和供电说明的设计文档。”

具体 API 入口、来源和执行范围见 [操作参考](references/operations.md)。

来源性质：从官方扩展与接口提炼的领域工作流。本技能的存在不代表上游扩展已安装或工作流已实测。
