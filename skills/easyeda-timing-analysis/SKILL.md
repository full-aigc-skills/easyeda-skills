---
name: easyeda-timing-analysis
description: "分析 PCB 信号路径延迟、Setup/Hold 和时序余量，或在原理图中生成 WaveDrom 时序说明。"
license: Apache-2.0
metadata:
  source-kind: extension-derived
---

# easyeda-timing-analysis

分析 PCB 信号路径延迟、Setup/Hold 和时序余量，或在原理图中生成 WaveDrom 时序说明。

## 首次使用

读取 [原生 MCP 约定](references/native-mcp.md)，按真实工具返回执行 help、doctor、session.list。
不要把工程为空或扩展未安装解释为需要切换到 WebSocket Gateway。

## 当前任务

需要明确：驱动和接收器参数；实际路径与时钟条件；目标余量。

1. 读取目标网络和真实长度。
2. 核对传播模型、单位和器件时序参数。
3. 计算约束下的路径延迟与 Setup/Hold 余量。
4. 需要说明图时根据明确时序生成 WaveDrom。
5. 检查数值与图形一致并导出用户要求的格式。

## 验证结果

- 路径对应实际 PCB。
- 未忽略器件与时钟参数。
- 余量结论包含假设。

## 容易出错的地方

- 画出时序图不是完成时序验证。
- 缺少参数时只能报告待定不能补造数值。

## 使用示例

“分析主控到外设的时钟与数据 Setup/Hold 余量。”

具体 API 入口、来源和执行范围见 [操作参考](references/operations.md)。

来源性质：从官方扩展与接口提炼的领域工作流。本技能的存在不代表上游扩展已安装或工作流已实测。
