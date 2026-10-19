# 操作参考

## 第一个工具调用

调用 tools/list 实际返回的原生 `.help`，参数 `{}`，再查询 `doc.api` 帮助。
本工作流首先查询以下类，具体方法、参数、返回以当前客户端帮助为准：

```json
{"path": "doc.api", "input": {"className": "PCB_PrimitiveLine"}}
```

```json
{"path": "doc.api", "input": {"className": "PCB_PrimitivePad"}}
```

```json
{"path": "doc.api", "input": {"className": "PCB_PrimitivePour"}}
```

之后在选定会话中通过原生 `invoke` 执行已查询的 API。涉及扩展时先查询 `doc.external` 或 `functions`，确认上层接口实际存在；未暴露时报告缺口，不把源代码函数名直接当成工具。

## 完成判据

- 电气参数与实际几何一致。
- 区域与禁布要求保留。
- 补强、阻焊与铜层区别明确。

## 官方来源

- [eext-coil-creator](https://github.com/easyeda/eext-coil-creator/tree/3c897637a52d8f1cbc243e8587cbc5c90c5e35b1)，修订 `3c897637a52d8f1cbc243e8587cbc5c90c5e35b1`。
  - [src/index.ts](https://github.com/easyeda/eext-coil-creator/blob/3c897637a52d8f1cbc243e8587cbc5c90c5e35b1/src/index.ts)
- [eext-pcb-heater-trace-generator](https://github.com/easyeda/eext-pcb-heater-trace-generator/tree/89cf798b176f1f13f0dde29c5024ae4408f3ad1c)，修订 `89cf798b176f1f13f0dde29c5024ae4408f3ad1c`。
  - [src/index.ts](https://github.com/easyeda/eext-pcb-heater-trace-generator/blob/89cf798b176f1f13f0dde29c5024ae4408f3ad1c/src/index.ts)
- [eext-fpc-workshop](https://github.com/easyeda/eext-fpc-workshop/tree/f8a245ab74a5405011bdd98b65b0b2af5f05cdca)，修订 `f8a245ab74a5405011bdd98b65b0b2af5f05cdca`。
  - [src/index.ts](https://github.com/easyeda/eext-fpc-workshop/blob/f8a245ab74a5405011bdd98b65b0b2af5f05cdca/src/index.ts)
- [eext-pad-expand-helper](https://github.com/easyeda/eext-pad-expand-helper/tree/de5b2eb6bd6817bb25025d621c2f6010bc110cab)，修订 `de5b2eb6bd6817bb25025d621c2f6010bc110cab`。
  - [src/index.ts](https://github.com/easyeda/eext-pad-expand-helper/blob/de5b2eb6bd6817bb25025d621c2f6010bc110cab/src/index.ts)
- [eext-nc-pad-converter](https://github.com/easyeda/eext-nc-pad-converter/tree/acbc6436576fd18917a095e45e72aa41cb5d752b)，修订 `acbc6436576fd18917a095e45e72aa41cb5d752b`。
  - [src/index.ts](https://github.com/easyeda/eext-nc-pad-converter/blob/acbc6436576fd18917a095e45e72aa41cb5d752b/src/index.ts)
- [eext-auto-copper-shape](https://github.com/easyeda/eext-auto-copper-shape/tree/98317b6b5941977a3ae90948a05295f9d8b1169f)，修订 `98317b6b5941977a3ae90948a05295f9d8b1169f`。
  - [src/index.ts](https://github.com/easyeda/eext-auto-copper-shape/blob/98317b6b5941977a3ae90948a05295f9d8b1169f/src/index.ts)
- [eext-balance-copper](https://github.com/easyeda/eext-balance-copper/tree/4a52f9021a9df487c9f3d2694f1aa67ef528d5ec)，修订 `4a52f9021a9df487c9f3d2694f1aa67ef528d5ec`。
  - [src/index.ts](https://github.com/easyeda/eext-balance-copper/blob/4a52f9021a9df487c9f3d2694f1aa67ef528d5ec/src/index.ts)

这些链接是固定版本的知识来源，不会自动安装、运行上游扩展。文档/源码证据与真实客户端、板卡、制造验证分开记录。
