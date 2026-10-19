# 操作参考

## 第一个工具调用

调用 tools/list 实际返回的原生 `.help`，参数 `{}`，再查询 `doc.api` 帮助。
本工作流首先查询以下类，具体方法、参数、返回以当前客户端帮助为准：

```json
{"path": "doc.api", "input": {"className": "PCB_ManufactureData"}}
```

```json
{"path": "doc.api", "input": {"className": "SCH_ManufactureData"}}
```

之后在选定会话中通过原生 `invoke` 执行已查询的 API。涉及扩展时先查询 `doc.external` 或 `functions`，确认上层接口实际存在；未暴露时报告缺口，不把源代码函数名直接当成工具。

## 完成判据

- BOM 数量可追溯到实际器件。
- DNP 与变体正确过滤。
- 坐标原点、镜像及底面旋转明确。

## 官方来源

- [eext-bom-compare](https://github.com/easyeda/eext-bom-compare/tree/4489dd9b857e19505a2f5a0dd383342bb77923d6)，修订 `4489dd9b857e19505a2f5a0dd383342bb77923d6`。
  - [src/index.ts](https://github.com/easyeda/eext-bom-compare/blob/4489dd9b857e19505a2f5a0dd383342bb77923d6/src/index.ts)
- [eext-interactive-bom](https://github.com/easyeda/eext-interactive-bom/tree/3606355f002a9380fe2f7b956b2969b09df65545)，修订 `3606355f002a9380fe2f7b956b2969b09df65545`。
  - [src/index.ts](https://github.com/easyeda/eext-interactive-bom/blob/3606355f002a9380fe2f7b956b2969b09df65545/src/index.ts)
- [eext-interactive-html-bom](https://github.com/easyeda/eext-interactive-html-bom/tree/430ea9d06a1c975ed3d2c6da83a6686a1f737084)，修订 `430ea9d06a1c975ed3d2c6da83a6686a1f737084`。
  - [src/index.ts](https://github.com/easyeda/eext-interactive-html-bom/blob/430ea9d06a1c975ed3d2c6da83a6686a1f737084/src/index.ts)
- [eext-component-box](https://github.com/easyeda/eext-component-box/tree/0390a4c0e9dba6643ca2d18f8ff78328548efa70)，修订 `0390a4c0e9dba6643ca2d18f8ff78328548efa70`。
  - [src/index.ts](https://github.com/easyeda/eext-component-box/blob/0390a4c0e9dba6643ca2d18f8ff78328548efa70/src/index.ts)
- [eext-pcb-price-calculator](https://github.com/easyeda/eext-pcb-price-calculator/tree/5527d29e2e13975652f00f3dc0df3dd5417c597a)，修订 `5527d29e2e13975652f00f3dc0df3dd5417c597a`。
  - [src/index.ts](https://github.com/easyeda/eext-pcb-price-calculator/blob/5527d29e2e13975652f00f3dc0df3dd5417c597a/src/index.ts)

这些链接是固定版本的知识来源，不会自动安装、运行上游扩展。文档/源码证据与真实客户端、板卡、制造验证分开记录。
