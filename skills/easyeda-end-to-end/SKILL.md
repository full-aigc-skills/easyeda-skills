---
name: easyeda-end-to-end
description: "协调 EasyEDA 原理图设计、PCB 布局布线、DRC/DFM 和制造导出的完整流程，逐阶段验证实际产物。"
license: Apache-2.0
metadata:
  source-kind: extension-derived
---

# easyeda-end-to-end

协调 EasyEDA 原理图设计、PCB 布局布线、DRC/DFM 和制造导出的完整流程，逐阶段验证实际产物。

## 首次使用

读取 [原生 MCP 约定](references/native-mcp.md)，按真实工具返回执行 help、doctor、session.list。
不要把工程为空或扩展未安装解释为需要切换到 WebSocket Gateway。

## 当前任务

需要明确：明确功能和接口；板框、叠层及制造工艺；输出目录与修改范围。

1. 把需求落实为器件、连接和机械约束。
2. 生成原理图并对比实际网表；存在歧义先解决。
3. 同步 PCB，按固定位置、禁布区和关键回路布局。
4. 应用规则、布线、检查实际失败网络和 DRC/DFM。
5. 保存授权工程并重新打开，检查制造文件完整性。

## 验证结果

- 每一阶段使用当前版本的实际结果。
- 失败或部分检查不被下游导出掩盖。
- 可编辑工程和制造包对应同一设计。

## 容易出错的地方

- 不要让 AI 凭外观判断电路正确。
- 高级高速、射频或电源设计需要专项验证，不能以通用布线替代。

## 使用示例

“从明确的传感器板需求开始，交付可编辑工程和制造文件。”

具体 API 入口、来源和执行范围见 [操作参考](references/operations.md)。

来源性质：从官方扩展与接口提炼的领域工作流。本技能的存在不代表上游扩展已安装或工作流已实测。
