# 操作参考

## 第一个工具调用

调用 tools/list 实际返回的原生 `.help`，参数 `{}`，再查询 `doc.api` 帮助。
本工作流首先查询以下类，具体方法、参数、返回以当前客户端帮助为准：

```json
{"path": "doc.api", "input": {"className": "LIB_Device"}}
```

```json
{"path": "doc.api", "input": {"className": "SCH_PrimitiveComponent"}}
```

```json
{"path": "doc.api", "input": {"className": "SCH_PrimitiveWire"}}
```

```json
{"path": "doc.api", "input": {"className": "SCH_Drc"}}
```

之后在选定会话中通过原生 `invoke` 执行已查询的 API。涉及扩展时先查询 `doc.external` 或 `functions`，确认上层接口实际存在；未暴露时报告缺口，不把源代码函数名直接当成工具。

## 完成判据

- 实际网表与连接描述一致。
- 关键电源、复位、上拉和去耦有明确依据。
- 工程可在客户端继续编辑。

## 官方来源

- [eext-easyeda-api-agent](https://github.com/easyeda/eext-easyeda-api-agent/tree/c54a6f9a30717c327e2c9022aff2fbd9f9b8498e)，修订 `c54a6f9a30717c327e2c9022aff2fbd9f9b8498e`。
  - [src/index.ts](https://github.com/easyeda/eext-easyeda-api-agent/blob/c54a6f9a30717c327e2c9022aff2fbd9f9b8498e/src/index.ts)
- [eext-ai-reuse-block-placement](https://github.com/easyeda/eext-ai-reuse-block-placement/tree/0a1b7536e9528b9e268861add2623eb7e33e47c3)，修订 `0a1b7536e9528b9e268861add2623eb7e33e47c3`。
  - [src/index.ts](https://github.com/easyeda/eext-ai-reuse-block-placement/blob/0a1b7536e9528b9e268861add2623eb7e33e47c3/src/index.ts)
  - [src/agent/tools.ts](https://github.com/easyeda/eext-ai-reuse-block-placement/blob/0a1b7536e9528b9e268861add2623eb7e33e47c3/src/agent/tools.ts)
  - [src/cbb.ts](https://github.com/easyeda/eext-ai-reuse-block-placement/blob/0a1b7536e9528b9e268861add2623eb7e33e47c3/src/cbb.ts)
- [eext-generate-schematic-from-netlist](https://github.com/easyeda/eext-generate-schematic-from-netlist/tree/35679a0f1e6b1ee2cca8fe0479fdd7def5e75f8d)，修订 `35679a0f1e6b1ee2cca8fe0479fdd7def5e75f8d`。
  - [src/index.ts](https://github.com/easyeda/eext-generate-schematic-from-netlist/blob/35679a0f1e6b1ee2cca8fe0479fdd7def5e75f8d/src/index.ts)
  - [src/enetImporter.ts](https://github.com/easyeda/eext-generate-schematic-from-netlist/blob/35679a0f1e6b1ee2cca8fe0479fdd7def5e75f8d/src/enetImporter.ts)

这些链接是固定版本的知识来源，不会自动安装、运行上游扩展。文档/源码证据与真实客户端、板卡、制造验证分开记录。
