# 操作参考

## 第一个工具调用

调用 tools/list 实际返回的原生 `.help`，参数 `{}`，再查询 `doc.api` 帮助。
本工作流首先查询以下类，具体方法、参数、返回以当前客户端帮助为准：

```json
{"path": "doc.api", "input": {"className": "DMT_Project"}}
```

```json
{"path": "doc.api", "input": {"className": "SCH_Netlist"}}
```

```json
{"path": "doc.api", "input": {"className": "PCB_ManufactureData"}}
```

之后在选定会话中通过原生 `invoke` 执行已查询的 API。涉及扩展时先查询 `doc.external` 或 `functions`，确认上层接口实际存在；未暴露时报告缺口，不把源代码函数名直接当成工具。

## 完成判据

- 统计来自实际工程。
- 生成文字不冒充测试报告。
- 文档链接指向有效交付文件。

## 官方来源

- [eext-docs-generator](https://github.com/easyeda/eext-docs-generator/tree/8fa4e175f517f7d6b4c088f295651979db3c1ae6)，修订 `8fa4e175f517f7d6b4c088f295651979db3c1ae6`。
  - [src/index.ts](https://github.com/easyeda/eext-docs-generator/blob/8fa4e175f517f7d6b4c088f295651979db3c1ae6/src/index.ts)
- [eext-note-tools](https://github.com/easyeda/eext-note-tools/tree/4627a6aa190cc4741e46a99745d9d3cf8e69af82)，修订 `4627a6aa190cc4741e46a99745d9d3cf8e69af82`。
  - [src/index.ts](https://github.com/easyeda/eext-note-tools/blob/4627a6aa190cc4741e46a99745d9d3cf8e69af82/src/index.ts)
- [eext-export-design-report](https://github.com/easyeda/eext-export-design-report/tree/31a8cfec95bcae13e981b912c6bc86025062dca0)，修订 `31a8cfec95bcae13e981b912c6bc86025062dca0`。
  - [src/index.ts](https://github.com/easyeda/eext-export-design-report/blob/31a8cfec95bcae13e981b912c6bc86025062dca0/src/index.ts)
- [eext-plm-integration-demo](https://github.com/easyeda/eext-plm-integration-demo/tree/92463b09f41d048b2a96593a8a2b34693c872115)，修订 `92463b09f41d048b2a96593a8a2b34693c872115`。
  - [src/index.ts](https://github.com/easyeda/eext-plm-integration-demo/blob/92463b09f41d048b2a96593a8a2b34693c872115/src/index.ts)

这些链接是固定版本的知识来源，不会自动安装、运行上游扩展。文档/源码证据与真实客户端、板卡、制造验证分开记录。
