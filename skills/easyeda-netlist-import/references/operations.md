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

之后在选定会话中通过原生 `invoke` 执行已查询的 API。涉及扩展时先查询 `doc.external` 或 `functions`，确认上层接口实际存在；未暴露时报告缺口，不把源代码函数名直接当成工具。

## 完成判据

- 没有静默遗漏器件或引脚。
- 位号和封装匹配。
- 全部预期连接得到验证。

## 官方来源

- [eext-generate-schematic-from-netlist](https://github.com/easyeda/eext-generate-schematic-from-netlist/tree/35679a0f1e6b1ee2cca8fe0479fdd7def5e75f8d)，修订 `35679a0f1e6b1ee2cca8fe0479fdd7def5e75f8d`。
  - [src/index.ts](https://github.com/easyeda/eext-generate-schematic-from-netlist/blob/35679a0f1e6b1ee2cca8fe0479fdd7def5e75f8d/src/index.ts)
  - [src/enetImporter.ts](https://github.com/easyeda/eext-generate-schematic-from-netlist/blob/35679a0f1e6b1ee2cca8fe0479fdd7def5e75f8d/src/enetImporter.ts)
- [easyeda-netlist-format](https://github.com/easyeda/easyeda-netlist-format/tree/4e3997215e3241ba75d7287fbd4743231e32f7a6)，修订 `4e3997215e3241ba75d7287fbd4743231e32f7a6`。
  - [README.md](https://github.com/easyeda/easyeda-netlist-format/blob/4e3997215e3241ba75d7287fbd4743231e32f7a6/README.md)

这些链接是固定版本的知识来源，不会自动安装、运行上游扩展。文档/源码证据与真实客户端、板卡、制造验证分开记录。
