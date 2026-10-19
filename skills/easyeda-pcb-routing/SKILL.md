---
name: easyeda-pcb-routing
description: "使用 EasyEDA 内置 autoRouting 布线，设置网络、启用层与规则并验证失败网络和实际连通性。"
license: Apache-2.0
metadata:
  source-kind: extension-derived
---

# easyeda-pcb-routing

使用 EasyEDA 内置 autoRouting 布线，设置网络、启用层与规则并验证失败网络和实际连通性。

## 首次使用

读取 [原生 MCP 约定](references/native-mcp.md)，按真实工具返回执行 help、doctor、session.list。
不要把工程为空或扩展未安装解释为需要切换到 WebSocket Gateway。

## 当前任务

需要明确：布局完成的 PCB；线宽、间距、层及过孔规则；保留已有走线与关键网络要求。

1. 读取并检查板框、器件布局、启用层和现有走线。
2. 查询 IPCB_AutoRoutingProps 与返回类型，明确保留或重布方式。
3. 关键网络按约束先处理，其余网络调用 autoRouting。
4. 检查 failedNets、成功数量和实际几何，不只检查 success。
5. 重算连接并运行 PCB DRC，报告无法自动解决的网络。

## 验证结果

- 全部目标网络布通或明确列出失败。
- 没有损坏已有人工布线。
- DRC 结果真实读取。

## 容易出错的地方

- 接口存在 900 秒上限的版本限制，增加 CLI timeout 不一定解决。
- 网页示例 nets 与实际 RoutingNets 可能不同，按目标类型查询。

## 使用示例

“保留电源走线，只给剩余信号自动布线。”

具体 API 入口、来源和执行范围见 [操作参考](references/operations.md)。

来源性质：从官方扩展与接口提炼的领域工作流。本技能的存在不代表上游扩展已安装或工作流已实测。
