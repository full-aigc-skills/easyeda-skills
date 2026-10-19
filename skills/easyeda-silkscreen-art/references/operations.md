# 操作参考

## 第一个工具调用

调用 tools/list 实际返回的原生 `.help`，参数 `{}`，再查询 `doc.api` 帮助。
本工作流首先查询以下类，具体方法、参数、返回以当前客户端帮助为准：

```json
{"path": "doc.api", "input": {"className": "PCB_PrimitiveString"}}
```

```json
{"path": "doc.api", "input": {"className": "PCB_PrimitiveImage"}}
```

```json
{"path": "doc.api", "input": {"className": "PCB_PrimitivePolyline"}}
```

之后在选定会话中通过原生 `invoke` 执行已查询的 API。涉及扩展时先查询 `doc.external` 或 `functions`，确认上层接口实际存在；未暴露时报告缺口，不把源代码函数名直接当成工具。

## 完成判据

- 丝印未意外进入铜层。
- 二维码或文字在目标尺寸可辨识。
- 彩色丝印格式与目标工艺匹配。

## 官方来源

- [eext-color-silkscreen-generator](https://github.com/easyeda/eext-color-silkscreen-generator/tree/0d36c0495b9100a796337fd08041162a825b66b5)，修订 `0d36c0495b9100a796337fd08041162a825b66b5`。
  - [src/index.ts](https://github.com/easyeda/eext-color-silkscreen-generator/blob/0d36c0495b9100a796337fd08041162a825b66b5/src/index.ts)
- [eext-graffiti-silkscreen](https://github.com/easyeda/eext-graffiti-silkscreen/tree/8d969f1c6e0bb8b913abf9780a26c74961a58669)，修订 `8d969f1c6e0bb8b913abf9780a26c74961a58669`。
  - [src/index.ts](https://github.com/easyeda/eext-graffiti-silkscreen/blob/8d969f1c6e0bb8b913abf9780a26c74961a58669/src/index.ts)
- [eext-dynamic-fill-region-for-silkscreen](https://github.com/easyeda/eext-dynamic-fill-region-for-silkscreen/tree/27f0f4227b4dcaa9d1d03e878cbb3710f2c54fe5)，修订 `27f0f4227b4dcaa9d1d03e878cbb3710f2c54fe5`。
  - [src/index.ts](https://github.com/easyeda/eext-dynamic-fill-region-for-silkscreen/blob/27f0f4227b4dcaa9d1d03e878cbb3710f2c54fe5/src/index.ts)
- [eext-generate-silkscreen](https://github.com/easyeda/eext-generate-silkscreen/tree/f87bf3c725dea2dcb2b825a9faa90cb869dba86b)，修订 `f87bf3c725dea2dcb2b825a9faa90cb869dba86b`。
  - [src/index.ts](https://github.com/easyeda/eext-generate-silkscreen/blob/f87bf3c725dea2dcb2b825a9faa90cb869dba86b/src/index.ts)
- [eext-image-contour-to-pcb](https://github.com/easyeda/eext-image-contour-to-pcb/tree/3bbf294d2f2cfde51fb2f807fc45991f201fb0e7)，修订 `3bbf294d2f2cfde51fb2f807fc45991f201fb0e7`。
  - [src/index.ts](https://github.com/easyeda/eext-image-contour-to-pcb/blob/3bbf294d2f2cfde51fb2f807fc45991f201fb0e7/src/index.ts)
- [eext-qrcode-generator](https://github.com/easyeda/eext-qrcode-generator/tree/29371cdc7aa472a36e56b428db02aab8ffa3bac3)，修订 `29371cdc7aa472a36e56b428db02aab8ffa3bac3`。
  - [src/index.ts](https://github.com/easyeda/eext-qrcode-generator/blob/29371cdc7aa472a36e56b428db02aab8ffa3bac3/src/index.ts)
- [eext-excalidraw](https://github.com/easyeda/eext-excalidraw/tree/448db2cb66f497c26dd1597386759ea0325b6bc8)，修订 `448db2cb66f497c26dd1597386759ea0325b6bc8`。
  - [src/index.ts](https://github.com/easyeda/eext-excalidraw/blob/448db2cb66f497c26dd1597386759ea0325b6bc8/src/index.ts)

这些链接是固定版本的知识来源，不会自动安装、运行上游扩展。文档/源码证据与真实客户端、板卡、制造验证分开记录。
