---
name: easyeda-pcb-layout
description: "把原理图同步到 PCB，设置板框、固定位置和禁布区，并按功能块布局或检查自动布局结果。"
license: Apache-2.0
metadata:
  source-kind: extension-derived
---

# easyeda-pcb-layout

把原理图同步到 PCB，设置板框、固定位置和禁布区，并按功能块布局或检查自动布局结果。

## 首次使用

读取 [原生 MCP 约定](references/native-mcp.md)，按真实工具返回执行 help、doctor、session.list。
不要把工程为空或扩展未安装解释为需要切换到 WebSocket Gateway。

## 当前任务

需要明确：板框、层数与机械尺寸；连接器和安装孔位置；关键器件距离与禁布约束。

1. 读取当前原理图和 PCB 的器件、封装与同步状态。
2. 查询 importChanges 签名并执行授权的同步。
3. 先放置固定器件和关键器件，锁定需要保持的位置。
4. 对剩余器件采用分组或 autoLayout，再回读实际坐标。
5. 检查边界、重叠、去耦距离、天线与机械禁布区。

## 验证结果

- 器件与封装数量匹配。
- 固定位置和禁布区未丢失。
- 布局符合约束而非仅 API 返回成功。

## 容易出错的地方

- autoLayout 无参数签名不能证明支持全部布局约束。
- 板框形状拆分要保留每块板的归属。

## 使用示例

“按 50×40mm 板框布局，USB 接口固定在左边。”

具体 API 入口、来源和执行范围见 [操作参考](references/operations.md)。

来源性质：从官方扩展与接口提炼的领域工作流。本技能的存在不代表上游扩展已安装或工作流已实测。
