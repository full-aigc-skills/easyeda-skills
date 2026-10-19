---
name: easyeda-freerouting
description: "将 EasyEDA PCB 导出 DSN，调用已有 Freerouting 服务并导入 SES；适用于内置布线之外的备选路径。"
license: Apache-2.0
metadata:
  source-kind: extension-derived
---

# easyeda-freerouting

将 EasyEDA PCB 导出 DSN，调用已有 Freerouting 服务并导入 SES；适用于内置布线之外的备选路径。

## 首次使用

读取 [原生 MCP 约定](references/native-mcp.md)，按真实工具返回执行 help、doctor、session.list。
不要把工程为空或扩展未安装解释为需要切换到 WebSocket Gateway。

## 当前任务

需要明确：PCB 候选副本；已安装的 Freerouting 服务；保留原走线范围。

1. 确认外部服务健康状态及实际端口，不自动安装。
2. 导出包含几何和规则的 DSN，核对板框和网络。
3. 提交布线并跟踪实际任务状态。
4. 在候选副本导入 SES 后回读走线、过孔和网络。
5. 实际检查 DRC 返回值，比较采用前后的变化。

## 验证结果

- DSN 与结果对应同一板卡。
- 原工程和人工走线受到保护。
- SES 导入成功与 DRC 通过分别判断。

## 容易出错的地方

- 上游实现导入前会删除走线、圆弧和过孔，不能直接照搬。
- 上游 route 成功不以 DRC 返回值为门禁。

## 使用示例

“用现有 Freerouting 为 PCB 副本布线，保留原稿。”

具体 API 入口、来源和执行范围见 [操作参考](references/operations.md)。

来源性质：从官方扩展与接口提炼的领域工作流。本技能的存在不代表上游扩展已安装或工作流已实测。
