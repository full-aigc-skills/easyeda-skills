---
name: easyeda-simulation
description: "对 EasyEDA 原理图使用已有 NGspice、LTspice、SimulIDE 或 CircuitJS 集成做明确目标的电路仿真。"
license: Apache-2.0
metadata:
  source-kind: extension-derived
---

# easyeda-simulation

对 EasyEDA 原理图使用已有 NGspice、LTspice、SimulIDE 或 CircuitJS 集成做明确目标的电路仿真。

## 首次使用

读取 [原生 MCP 约定](references/native-mcp.md)，按真实工具返回执行 help、doctor、session.list。
不要把工程为空或扩展未安装解释为需要切换到 WebSocket Gateway。

## 当前任务

需要明确：电路与仿真模型；分析类型、激励和指标；已安装仿真引擎。

1. 核对模型、引脚映射、供电和地参考。
2. 按目标选择已有引擎并查询扩展上层接口。
3. 设置 DC、AC 或瞬态等参数。
4. 执行后读取引擎状态、收敛问题与波形。
5. 对目标指标计算结果，并说明模型边界。

## 验证结果

- 没有把启动引擎当成仿真完成。
- 曲线单位、时间和激励正确。
- 结果对应当前电路版本。

## 容易出错的地方

- 缺少模型时不能用随意占位模型宣称功能通过。
- 电路仿真不涵盖真实 PCB 的全部寄生效应。

## 使用示例

“验证 RC 滤波器截止频率并输出实际曲线。”

具体 API 入口、来源和执行范围见 [操作参考](references/operations.md)。

来源性质：从官方扩展与接口提炼的领域工作流。本技能的存在不代表上游扩展已安装或工作流已实测。
