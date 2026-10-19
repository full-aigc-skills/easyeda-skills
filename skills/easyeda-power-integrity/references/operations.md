# 操作参考

## 第一个工具调用

调用 tools/list 实际返回的原生 `.help`，参数 `{}`，再查询 `doc.api` 帮助。
本工作流首先查询以下类，具体方法、参数、返回以当前客户端帮助为准：

```json
{"path": "doc.api", "input": {"className": "PCB_Layer"}}
```

```json
{"path": "doc.api", "input": {"className": "PCB_Net"}}
```

```json
{"path": "doc.api", "input": {"className": "PCB_ManufactureData"}}
```

之后在选定会话中通过原生 `invoke` 执行已查询的 API。涉及扩展时先查询 `doc.external` 或 `functions`，确认上层接口实际存在；未暴露时报告缺口，不把源代码函数名直接当成工具。

## 完成判据

- 求解模型包含实际导电路径。
- 材料与电流假设写清。
- 结果不外推到未建模频段。

## 官方来源

- [eext-paden-integration](https://github.com/easyeda/eext-paden-integration/tree/0bb14f58712100eb5b84db5be7bd0c0ef318ea88)，修订 `0bb14f58712100eb5b84db5be7bd0c0ef318ea88`。
  - [src/index.ts](https://github.com/easyeda/eext-paden-integration/blob/0bb14f58712100eb5b84db5be7bd0c0ef318ea88/src/index.ts)
- [eext-paden-integration-wasm](https://github.com/easyeda/eext-paden-integration-wasm/tree/92c75f057ede5b9c8e7a5db36ae79f8014f5a26b)，修订 `92c75f057ede5b9c8e7a5db36ae79f8014f5a26b`。
  - [src/index.ts](https://github.com/easyeda/eext-paden-integration-wasm/blob/92c75f057ede5b9c8e7a5db36ae79f8014f5a26b/src/index.ts)
- [eext-kipida-integration](https://github.com/easyeda/eext-kipida-integration/tree/af11ba17b6b1487efc1b87fc580a0ff6f97b1f81)，修订 `af11ba17b6b1487efc1b87fc580a0ff6f97b1f81`。
  - [src/index.ts](https://github.com/easyeda/eext-kipida-integration/blob/af11ba17b6b1487efc1b87fc580a0ff6f97b1f81/src/index.ts)

这些链接是固定版本的知识来源，不会自动安装、运行上游扩展。文档/源码证据与真实客户端、板卡、制造验证分开记录。
