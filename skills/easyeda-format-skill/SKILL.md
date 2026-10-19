---
name: easyeda-format-skill
description: "读取或生成 EasyEDA 专业版原理图、PCB、符号、封装的底层记录，处理 DOCHEAD、ticket、Schema 和文档类型差异。"
license: Apache-2.0
metadata:
  source-kind: official-adapted
---

# easyeda-format-skill

读取或生成 EasyEDA 专业版原理图、PCB、符号、封装的底层记录，处理 DOCHEAD、ticket、Schema 和文档类型差异。

## 首次使用

读取 [原生 MCP 约定](references/native-mcp.md)，按真实工具返回执行 help、doctor、session.list。
不要把工程为空或扩展未安装解释为需要切换到 WebSocket Gateway。

## 当前任务

需要明确：目标版本与文档类型；需检查或生成的记录；工程副本目录。

1. 先通过 doc.format 查询当前类型并读取官方字段定义。
2. 明确 SCH_PAGE、PCB、SYMBOL 等文档域，按域选 Schema。
3. 生成正确关联文档与记录边界，不从记忆猜字段。
4. 执行与目标版本匹配的校验器；缺依赖时报告而不假称通过。
5. 在工程副本中打开并回读对象与连接。

## 验证结果

- DOCHEAD、CANVAS 适用域正确。
- 记录结束符和 ID 合法。
- 实际对象与网表和目标一致。

## 容易出错的地方

- 同名 LINE 在不同文档类型中 Schema 不同。
- DELETE_DOC 载荷与原子记录删除不可互换；META 不能随意置空。

## 使用示例

“解释这条 PCB_LINE 记录并按当前格式检查字段。”

具体 API 入口、来源和执行范围见 [操作参考](references/operations.md)。

来源性质：官方技能整合，已将传输改为内置 MCP。本技能的存在不代表上游扩展已安装或工作流已实测。
上游技能名：`easyeda-format-skill`；这里为中文整理与原生 MCP 适配版本。
