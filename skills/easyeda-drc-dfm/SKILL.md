---
name: easyeda-drc-dfm
description: "检查原理图、PCB DRC 与嘉立创制造约束，区分完整通过、部分检查和执行失败。"
license: Apache-2.0
metadata:
  source-kind: extension-derived
---

# easyeda-drc-dfm

检查原理图、PCB DRC 与嘉立创制造约束，区分完整通过、部分检查和执行失败。

## 首次使用

读取 [原生 MCP 约定](references/native-mcp.md)，按真实工具返回执行 help、doctor、session.list。
不要把工程为空或扩展未安装解释为需要切换到 WebSocket Gateway。

## 当前任务

需要明确：检查的板卡与图页；目标工艺和材料；只读或允许修复的范围。

1. 等待目标文档计算稳定后运行相应 DRC。
2. 获取详细违规并关联位号、网络和坐标。
3. 按实际工艺运行可用 DFM 扩展或明确缺失项。
4. 检查项异常时标记 partial 或 failed，保留未检查项。
5. 修复后只复查受影响范围，最终读取完整结果。

## 验证结果

- 检查范围与当前工程一致。
- 未检查项目未被当成通过。
- 检查报告可定位具体对象。

## 容易出错的地方

- 上游 DFM 集合可能捕获异常后返回部分结果。
- 零 DRC 不证明电路功能或板厂最终审单通过。

## 使用示例

“只读检查当前 PCB，列出阻碍制造的项目。”

具体 API 入口、来源和执行范围见 [操作参考](references/operations.md)。

来源性质：从官方扩展与接口提炼的领域工作流。本技能的存在不代表上游扩展已安装或工作流已实测。
