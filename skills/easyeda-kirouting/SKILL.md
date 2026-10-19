---
name: easyeda-kirouting
description: "评估或调用已有 KiRouting 桥接，对 EasyEDA PCB 执行外部布线并验证坐标、层和规则转换。"
license: Apache-2.0
metadata:
  source-kind: extension-derived
---

# easyeda-kirouting

评估或调用已有 KiRouting 桥接，对 EasyEDA PCB 执行外部布线并验证坐标、层和规则转换。

## 首次使用

读取 [原生 MCP 约定](references/native-mcp.md)，按真实工具返回执行 help、doctor、session.list。
不要把工程为空或扩展未安装解释为需要切换到 WebSocket Gateway。

## 当前任务

需要明确：已有桥接服务和引擎；PCB 副本；单端或差分等明确约束。

1. 检查 Python 桥接与布线引擎是否实际可用。
2. 读取焊盘、孔、走线、板框和层，保留坐标单位。
3. 在转换后检查 EasyEDA 与 KiCad 的层和几何映射。
4. 执行选定功能并提取新走线与过孔。
5. 回写候选 PCB 后逐项核对连通与规则。

## 验证结果

- mil/mm 和坐标方向一致。
- 异形焊盘、孔与铜层未被静默简化。
- 高级功能有实际板卡验证。

## 容易出错的地方

- README 宣称支持 DDR 或阻抗不等于目标板验证。
- Windows 启动脚本会安装依赖，未授权时不执行。

## 使用示例

“比较 KiRouting 对这个差分接口板的布线结果。”

具体 API 入口、来源和执行范围见 [操作参考](references/operations.md)。

来源性质：从官方扩展与接口提炼的领域工作流。本技能的存在不代表上游扩展已安装或工作流已实测。
