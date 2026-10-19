---
name: easyeda-knowledge-base
description: "在已有 EasyEDA 本地 RAG 知识库中检索设计资料，检查引用来源与更新范围。"
license: Apache-2.0
metadata:
  source-kind: extension-derived
---

# easyeda-knowledge-base

在已有 EasyEDA 本地 RAG 知识库中检索设计资料，检查引用来源与更新范围。

## 首次使用

读取 [原生 MCP 约定](references/native-mcp.md)，按真实工具返回执行 help、doctor、session.list。
不要把工程为空或扩展未安装解释为需要切换到 WebSocket Gateway。

## 当前任务

需要明确：查询问题或指定资料；已有知识库与模型；是否允许新增索引。

1. 确认扩展、模型和索引是否实际可用。
2. 默认先检索已有资料。
3. 读取命中文段的文件、位置和版本。
4. 用原文复核关键结论并指出冲突。
5. 新增资料或重建索引只在用户要求范围内进行。

## 验证结果

- 回答能追溯到实际命中文段。
- 缺失信息不由模型补造。
- 本地检索与外发数据区分。

## 容易出错的地方

- Embedding 相似度不证明技术结论正确。
- 已有知识库不一定覆盖当前器件版本。

## 使用示例

“从本地知识库找出这个电源模块的设计依据。”

具体 API 入口、来源和执行范围见 [操作参考](references/operations.md)。

来源性质：从官方扩展与接口提炼的领域工作流。本技能的存在不代表上游扩展已安装或工作流已实测。
