---
name: easyeda-datasheet-analysis
description: "从器件数据手册提取引脚、电源、封装尺寸和参考电路，供 EasyEDA 选型、建库或设计验证。"
license: Apache-2.0
metadata:
  source-kind: extension-derived
---

# easyeda-datasheet-analysis

从器件数据手册提取引脚、电源、封装尺寸和参考电路，供 EasyEDA 选型、建库或设计验证。

## 首次使用

读取 [原生 MCP 约定](references/native-mcp.md)，按真实工具返回执行 help、doctor、session.list。
不要把工程为空或扩展未安装解释为需要切换到 WebSocket Gateway。

## 当前任务

需要明确：数据手册文件及器件完整型号；需要提取的参数；允许使用的本地识别工具。

1. 核对文档版本、型号后缀和封装变体。
2. 提取引脚表、电气额定值与机械尺寸。
3. 对图片或 OCR 结果回看原表格和图例。
4. 形成可用于器件或电路的结构化结果。
5. 对不清晰的符号和尺寸标明待核实。

## 验证结果

- 每个关键参数带页码或章节来源。
- 单位与典型值、最大值区分。
- 引脚方向与底视/顶视核对。

## 容易出错的地方

- VLM 识别可能误读小数、极性和引脚号。
- 未经授权不把保密数据手册发送给外部服务。

## 使用示例

“从这份数据手册提取引脚和推荐供电电路。”

具体 API 入口、来源和执行范围见 [操作参考](references/operations.md)。

来源性质：从官方扩展与接口提炼的领域工作流。本技能的存在不代表上游扩展已安装或工作流已实测。
