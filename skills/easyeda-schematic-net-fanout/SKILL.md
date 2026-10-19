---
name: easyeda-schematic-net-fanout
description: "按实际引脚方向排列原理图元件、生成电源标识符和信号端口，或修改已有引脚扇出。"
license: Apache-2.0
metadata:
  source-kind: official-adapted
---

# easyeda-schematic-net-fanout

按实际引脚方向排列原理图元件、生成电源标识符和信号端口，或修改已有引脚扇出。

## 首次使用

读取 [原生 MCP 约定](references/native-mcp.md)，按真实工具返回执行 help、doctor、session.list。
不要把工程为空或扩展未安装解释为需要切换到 WebSocket Gateway。

## 当前任务

需要明确：库器件 ID 与位号；引脚到网络的映射；图页和功能块位置。

1. 查询并批量获取器件，核对型号与封装。
2. 按元件实际包围盒布置功能块，预留扇出空间。
3. 读取每个引脚的坐标和方向后创建短线与相应标识符。
4. 修改元件时只清理与该元件相关的旧短线与标识符。
5. 导出网表比对同名网络的实际连通性。

## 验证结果

- 无元件与标识符遮挡。
- 没有遗留旧网络标签。
- 电气连接与映射一致。

## 容易出错的地方

- 原理图坐标单位为 10mil，不能沿用 PCB 的 mil。
- 删除元件不会自动删除全部相关导线和标识符。

## 使用示例

“整理 ESP32 原理图，将电源与信号引脚扇出到网络标识符。”

具体 API 入口、来源和执行范围见 [操作参考](references/operations.md)。

来源性质：官方技能整合，已将传输改为内置 MCP。本技能的存在不代表上游扩展已安装或工作流已实测。
上游技能名：`easyeda-schematic-net-fanout`；这里为中文整理与原生 MCP 适配版本。
