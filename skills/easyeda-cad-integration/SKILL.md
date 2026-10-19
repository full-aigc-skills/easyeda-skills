---
name: easyeda-cad-integration
description: "将 EasyEDA PCB 与 FreeCAD、SolidWorks、Fusion 360 对接，导入 DWG 或使用 Blender 渲染板卡。"
license: Apache-2.0
metadata:
  source-kind: extension-derived
---

# easyeda-cad-integration

将 EasyEDA PCB 与 FreeCAD、SolidWorks、Fusion 360 对接，导入 DWG 或使用 Blender 渲染板卡。

## 首次使用

读取 [原生 MCP 约定](references/native-mcp.md)，按真实工具返回执行 help、doctor、session.list。
不要把工程为空或扩展未安装解释为需要切换到 WebSocket Gateway。

## 当前任务

需要明确：目标 CAD 软件和已有桥接；工程与输出模型；坐标原点、单位和同步范围。

1. 确认目标应用和插件实际已安装。
2. 导出或读取 STEP/板框及相关模型。
3. 按目标集成交换并核对方向、原点与尺寸。
4. 双向修改仅限用户指定结构，检查返回差异。
5. 重新打开模型并检查孔位、板厚、器件高度或渲染结果。

## 验证结果

- 机械尺寸与 PCB 对应。
- 模型缺失被明确报告。
- 导回修改没有覆盖电气设计。

## 容易出错的地方

- PCB 渲染不证明机械装配无碰撞。
- 双向同步可能改变板框，不能作为纯只读动作。

## 使用示例

“把当前 PCB 导入 FreeCAD，核对安装孔与外壳。”

具体 API 入口、来源和执行范围见 [操作参考](references/operations.md)。

来源性质：从官方扩展与接口提炼的领域工作流。本技能的存在不代表上游扩展已安装或工作流已实测。
