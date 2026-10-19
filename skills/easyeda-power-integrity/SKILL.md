---
name: easyeda-power-integrity
description: "通过已有 PADEN 或 KiPIDA 扩展评估 PCB 电源分配网络或直流压降，并核对提取模型。"
license: Apache-2.0
metadata:
  source-kind: extension-derived
---

# easyeda-power-integrity

通过已有 PADEN 或 KiPIDA 扩展评估 PCB 电源分配网络或直流压降，并核对提取模型。

## 首次使用

读取 [原生 MCP 约定](references/native-mcp.md)，按真实工具返回执行 help、doctor、session.list。
不要把工程为空或扩展未安装解释为需要切换到 WebSocket Gateway。

## 当前任务

需要明确：电源源端、负载与电流；铜厚、叠层与材料；目标压降或阻抗范围。

1. 核对电源网络、铜皮、过孔和电源源端定义。
2. 确认已有分析扩展可用，查询实际调用接口。
3. 按负载设置求解条件并提取模型。
4. 读取求解状态、单位和最差点。
5. 结合具体位置给出可验证的修改建议。

## 验证结果

- 求解模型包含实际导电路径。
- 材料与电流假设写清。
- 结果不外推到未建模频段。

## 容易出错的地方

- WASM 与外部后端不一定具备相同能力。
- DC 压降不能替代全频段电源完整性分析。

## 使用示例

“检查 3.3V 电源从入口到主控的直流压降。”

具体 API 入口、来源和执行范围见 [操作参考](references/operations.md)。

来源性质：从官方扩展与接口提炼的领域工作流。本技能的存在不代表上游扩展已安装或工作流已实测。
