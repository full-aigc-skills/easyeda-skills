---
name: easyeda-special-pcb
description: "生成 NFC/无线充电线圈、电热膜蛇形线路或 FPC 特殊结构，并核对电气目标和工艺限制。"
license: Apache-2.0
metadata:
  source-kind: extension-derived
---

# easyeda-special-pcb

生成 NFC/无线充电线圈、电热膜蛇形线路或 FPC 特殊结构，并核对电气目标和工艺限制。

## 首次使用

读取 [原生 MCP 约定](references/native-mcp.md)，按真实工具返回执行 help、doctor、session.list。
不要把工程为空或扩展未安装解释为需要切换到 WebSocket Gateway。

## 当前任务

需要明确：目标阻值、功率或线圈参数；区域、线宽间距与铜厚；FPC 补强和材料要求。

1. 核对需求、公式与适用材料。
2. 检查现有扩展参数和结果格式。
3. 在指定区域生成图形并保留原设计。
4. 回读几何和网络连接，计算目标量。
5. 检查 DRC 与制造参数后报告偏差。

## 验证结果

- 电气参数与实际几何一致。
- 区域与禁布要求保留。
- 补强、阻焊与铜层区别明确。

## 容易出错的地方

- 平衡铜图案不能与信号网络意外相连。
- 估算电流或温升不能当作实物温度验证。

## 使用示例

“在指定区域生成目标阻值的 PCB 电热膜线路。”

具体 API 入口、来源和执行范围见 [操作参考](references/operations.md)。

来源性质：从官方扩展与接口提炼的领域工作流。本技能的存在不代表上游扩展已安装或工作流已实测。
