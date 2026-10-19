# 操作参考

## 第一个工具调用

调用 tools/list 实际返回的原生 `.help`，参数 `{}`，再查询 `doc.api` 帮助。
本工作流首先查询以下类，具体方法、参数、返回以当前客户端帮助为准：

```json
{"path": "doc.api", "input": {"className": "SYS_ExternalApi"}}
```

之后在选定会话中通过原生 `invoke` 执行已查询的 API。涉及扩展时先查询 `doc.external` 或 `functions`，确认上层接口实际存在；未暴露时报告缺口，不把源代码函数名直接当成工具。

## 完成判据

- 回答能追溯到实际命中文段。
- 缺失信息不由模型补造。
- 本地检索与外发数据区分。

## 官方来源

- [eext-knowledge-base](https://github.com/easyeda/eext-knowledge-base/tree/5c666fe9ce711284f9a52dba24c3040ed7f57535)，修订 `5c666fe9ce711284f9a52dba24c3040ed7f57535`。
  - [src/index.ts](https://github.com/easyeda/eext-knowledge-base/blob/5c666fe9ce711284f9a52dba24c3040ed7f57535/src/index.ts)

这些链接是固定版本的知识来源，不会自动安装、运行上游扩展。文档/源码证据与真实客户端、板卡、制造验证分开记录。
