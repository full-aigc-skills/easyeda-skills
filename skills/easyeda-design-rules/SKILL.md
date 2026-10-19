---
name: easyeda-design-rules
description: "按明确板厂工艺、叠层和网络要求生成或修改 EasyEDA PCB 线宽、间距、网络类和差分规则。"
license: Apache-2.0
metadata:
  source-kind: extension-derived
---

# easyeda-design-rules

按明确板厂工艺、叠层和网络要求生成或修改 EasyEDA PCB 线宽、间距、网络类和差分规则。

## 首次使用

读取 [原生 MCP 约定](references/native-mcp.md)，按真实工具返回执行 help、doctor、session.list。
不要把工程为空或扩展未安装解释为需要切换到 WebSocket Gateway。

## 当前任务

需要明确：板材、板厚、铜厚和叠层；电流、阻抗和目标工艺；要修改的网络范围。

1. 读取现有规则和网络类，保存可恢复副本。
2. 核对叠层与计算模型适用范围，不套用未知材料。
3. 形成针对目标网络的规则变更。
4. 应用后回读规则、差分对与网络类。
5. 检查失败则恢复或报告未确定状态，不继续布线。

## 验证结果

- 规则数值和单位与输入匹配。
- 未覆盖无关用户规则。
- 差分正负网络确实存在。

## 容易出错的地方

- 模型拟合不替代板厂工艺确认。
- 仅保存配置不代表实际网络已使用该规则。

## 使用示例

“为 1A 电源和普通信号分别配置 PCB 规则。”

具体 API 入口、来源和执行范围见 [操作参考](references/operations.md)。

来源性质：从官方扩展与接口提炼的领域工作流。本技能的存在不代表上游扩展已安装或工作流已实测。
