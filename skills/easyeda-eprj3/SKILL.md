---
name: easyeda-eprj3
description: "创建、检查或编辑 EasyEDA 文件夹式 .eprj3 工程，优先通过内置 MCP 操作，直接写格式时核对完整格式依赖。"
license: Apache-2.0
metadata:
  source-kind: official-adapted
---

# easyeda-eprj3

创建、检查或编辑 EasyEDA 文件夹式 .eprj3 工程，优先通过内置 MCP 操作，直接写格式时核对完整格式依赖。

## 首次使用

读取 [原生 MCP 约定](references/native-mcp.md)，按真实工具返回执行 help、doctor、session.list。
不要把工程为空或扩展未安装解释为需要切换到 WebSocket Gateway。

## 当前任务

需要明确：新工程目录或现有工程；图页与 PCB 需求；实际器件库来源。

1. 区分 .eprj3 文件夹工程与旧 .eprj2 SQLite 工程。
2. 优先由原生 API 创建骨架、保存与重新打开。
3. 直接生成记录前读取格式规范、Schema 和真实样例。
4. 保留嵌入 SYMBOL、FOOTPRINT、DEVICE 等文档的关联与顺序。
5. 校验格式、在客户端打开并回读网表和 PCB。

## 验证结果

- 项目索引、文档和库引用完整。
- 文件格式校验与电气验证分别报告。
- 旧工程未被强制转换。

## 容易出错的地方

- 上游文档的 companion 仓库旧名称可能失效，不能盲目 clone。
- 格式脚本只覆盖部分契约，不能代替真实客户端验证。

## 使用示例

“创建一个新的 .eprj3 工程骨架，保留原有项目。”

具体 API 入口、来源和执行范围见 [操作参考](references/operations.md)。

来源性质：官方技能整合，已将传输改为内置 MCP。本技能的存在不代表上游扩展已安装或工作流已实测。
上游技能名：`easyeda-eprj3`；这里为中文整理与原生 MCP 适配版本。
