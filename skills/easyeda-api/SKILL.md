---
name: easyeda-api
description: "查询并使用 EasyEDA 专业版 eda.* API，读取对象与引脚、执行原生 invoke，替代官方 Skill 的独立 Bridge 传输。"
license: Apache-2.0
metadata:
  source-kind: official-adapted
---

# easyeda-api

查询并使用 EasyEDA 专业版 eda.* API，读取对象与引脚、执行原生 invoke，替代官方 Skill 的独立 Bridge 传输。

## 首次使用

读取 [原生 MCP 约定](references/native-mcp.md)，按真实工具返回执行 help、doctor、session.list。
不要把工程为空或扩展未安装解释为需要切换到 WebSocket Gateway。

## 当前任务

需要明确：目标会话和文档；要操作的对象与动作。

1. 调用原生 help 查看真实命令。
2. 用 doc.api 渐进查询类、方法、参数、返回和枚举。
3. 通过 invoke 在选定会话执行最小操作，读写按用户范围区分。
4. 使用返回 primitiveId 定位对象；引脚坐标由 API 回读。
5. 检查原生 ok、MCP isError 和业务结果后再继续。

## 验证结果

- API 在目标客户端存在。
- 返回对象和数量符合请求。
- 写入后回读目标对象。

## 容易出错的地方

- 返回 undefined 可能是契约也可能是错误，须查签名。
- MCP 外层成功不能覆盖内层失败。

## 使用示例

“查询放置元件 API，读取 R1 的实际引脚坐标。”

具体 API 入口、来源和执行范围见 [操作参考](references/operations.md)。

来源性质：官方技能整合，已将传输改为内置 MCP。本技能的存在不代表上游扩展已安装或工作流已实测。
上游技能名：`easyeda-api`；这里为中文整理与原生 MCP 适配版本。
