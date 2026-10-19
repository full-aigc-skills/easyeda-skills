# 操作参考

## 第一个工具调用

调用 tools/list 实际返回的原生 `.help`，参数 `{}`，再查询 `doc.api` 帮助。
本工作流首先查询以下类，具体方法、参数、返回以当前客户端帮助为准：

```json
{"path": "doc.api", "input": {"className": "PCB_Document"}}
```

```json
{"path": "doc.api", "input": {"className": "PCB_PrimitiveComponent"}}
```

```json
{"path": "doc.api", "input": {"className": "PCB_PrimitivePolyline"}}
```

```json
{"path": "doc.api", "input": {"className": "PCB_PrimitiveRegion"}}
```

之后在选定会话中通过原生 `invoke` 执行已查询的 API。涉及扩展时先查询 `doc.external` 或 `functions`，确认上层接口实际存在；未暴露时报告缺口，不把源代码函数名直接当成工具。

## 完成判据

- 器件与封装数量匹配。
- 固定位置和禁布区未丢失。
- 布局符合约束而非仅 API 返回成功。

## 官方来源

- [eext-pcb-component-grouping](https://github.com/easyeda/eext-pcb-component-grouping/tree/95421773a0180b9c0f48b4fe382419c673bafe2a)，修订 `95421773a0180b9c0f48b4fe382419c673bafe2a`。
  - [src/index.ts](https://github.com/easyeda/eext-pcb-component-grouping/blob/95421773a0180b9c0f48b4fe382419c673bafe2a/src/index.ts)
- [eext-batch-place-components](https://github.com/easyeda/eext-batch-place-components/tree/558e2530856cff42578900922ef66df4be3f7455)，修订 `558e2530856cff42578900922ef66df4be3f7455`。
  - [src/index.ts](https://github.com/easyeda/eext-batch-place-components/blob/558e2530856cff42578900922ef66df4be3f7455/src/index.ts)
- [eext-board-outline-splitter](https://github.com/easyeda/eext-board-outline-splitter/tree/2f5c602391cf4b1702cd808bdeda7d1c9f8ee09c)，修订 `2f5c602391cf4b1702cd808bdeda7d1c9f8ee09c`。
  - [src/index.ts](https://github.com/easyeda/eext-board-outline-splitter/blob/2f5c602391cf4b1702cd808bdeda7d1c9f8ee09c/src/index.ts)
- [easyeda-client-cli](https://github.com/easyeda/easyeda-client-cli/tree/eba951a2c08b7872271b20b463dc7fe1cc5f231d)，修订 `eba951a2c08b7872271b20b463dc7fe1cc5f231d`。
  - [cli-for-ai.md](https://github.com/easyeda/easyeda-client-cli/blob/eba951a2c08b7872271b20b463dc7fe1cc5f231d/cli-for-ai.md)

这些链接是固定版本的知识来源，不会自动安装、运行上游扩展。文档/源码证据与真实客户端、板卡、制造验证分开记录。
