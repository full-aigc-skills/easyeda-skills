# 操作参考

## 第一个工具调用

调用 tools/list 实际返回的原生 `.help`，参数 `{}`，再查询 `doc.api` 帮助。
本工作流首先查询以下类，具体方法、参数、返回以当前客户端帮助为准：

```json
{"path": "doc.api", "input": {"className": "SCH_Net"}}
```

```json
{"path": "doc.api", "input": {"className": "SCH_Netlist"}}
```

```json
{"path": "doc.api", "input": {"className": "SCH_ManufactureData"}}
```

之后在选定会话中通过原生 `invoke` 执行已查询的 API。涉及扩展时先查询 `doc.external` 或 `functions`，确认上层接口实际存在；未暴露时报告缺口，不把源代码函数名直接当成工具。

## 完成判据

- 报告包含具体位号、引脚和网络。
- 跨板同名网络未被错误合并。
- 未把 NC 引脚当成所有情况下的错误。

## 官方来源

- [eext-netlist-explorer](https://github.com/easyeda/eext-netlist-explorer/tree/6661961fc8780e13b97a9450a96afbaaf2960bf7)，修订 `6661961fc8780e13b97a9450a96afbaaf2960bf7`。
  - [src/index.ts](https://github.com/easyeda/eext-netlist-explorer/blob/6661961fc8780e13b97a9450a96afbaaf2960bf7/src/index.ts)
- [eext-signal-absence-detection](https://github.com/easyeda/eext-signal-absence-detection/tree/78f8ca3437e34c2f7976860a8e61adc511e36dd9)，修订 `78f8ca3437e34c2f7976860a8e61adc511e36dd9`。
  - [README.md](https://github.com/easyeda/eext-signal-absence-detection/blob/78f8ca3437e34c2f7976860a8e61adc511e36dd9/README.md)
- [eext-power-net-highlighter](https://github.com/easyeda/eext-power-net-highlighter/tree/ce520393451a1d148b3b354bb5161416fd5ec283)，修订 `ce520393451a1d148b3b354bb5161416fd5ec283`。
  - [README.md](https://github.com/easyeda/eext-power-net-highlighter/blob/ce520393451a1d148b3b354bb5161416fd5ec283/README.md)
- [easyeda-netlist-format](https://github.com/easyeda/easyeda-netlist-format/tree/4e3997215e3241ba75d7287fbd4743231e32f7a6)，修订 `4e3997215e3241ba75d7287fbd4743231e32f7a6`。
  - [README.md](https://github.com/easyeda/easyeda-netlist-format/blob/4e3997215e3241ba75d7287fbd4743231e32f7a6/README.md)
- [eext-schematic-pdf-interaction](https://github.com/easyeda/eext-schematic-pdf-interaction/tree/03d3a6ec6c3d5ecbb6ad0ec55224f0d6ecb480ac)，修订 `03d3a6ec6c3d5ecbb6ad0ec55224f0d6ecb480ac`。
  - [src/index.ts](https://github.com/easyeda/eext-schematic-pdf-interaction/blob/03d3a6ec6c3d5ecbb6ad0ec55224f0d6ecb480ac/src/index.ts)

这些链接是固定版本的知识来源，不会自动安装、运行上游扩展。文档/源码证据与真实客户端、板卡、制造验证分开记录。
