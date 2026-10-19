# 操作参考

## 第一个工具调用

调用 tools/list 实际返回的原生 `.help`，参数 `{}`，再查询 `doc.api` 帮助。
本工作流首先查询以下类，具体方法、参数、返回以当前客户端帮助为准：

```json
{"path": "doc.api", "input": {"className": "PCB_ManufactureData"}}
```

```json
{"path": "doc.api", "input": {"className": "PCB_Document"}}
```

```json
{"path": "doc.api", "input": {"className": "PCB_Drc"}}
```

之后在选定会话中通过原生 `invoke` 执行已查询的 API。涉及扩展时先查询 `doc.external` 或 `functions`，确认上层接口实际存在；未暴露时报告缺口，不把源代码函数名直接当成工具。

## 完成判据

- DSN 与结果对应同一板卡。
- 原工程和人工走线受到保护。
- SES 导入成功与 DRC 通过分别判断。

## 官方来源

- [eext-freerouting-intergration](https://github.com/easyeda/eext-freerouting-intergration/tree/dab07252c22b408759693ee82845fd550243c3b5)，修订 `dab07252c22b408759693ee82845fd550243c3b5`。
  - [src/index.ts](https://github.com/easyeda/eext-freerouting-intergration/blob/dab07252c22b408759693ee82845fd550243c3b5/src/index.ts)
  - [src/router/FreeRoutingRouter.ts](https://github.com/easyeda/eext-freerouting-intergration/blob/dab07252c22b408759693ee82845fd550243c3b5/src/router/FreeRoutingRouter.ts)
  - [src/types/index.ts](https://github.com/easyeda/eext-freerouting-intergration/blob/dab07252c22b408759693ee82845fd550243c3b5/src/types/index.ts)
- [easyeda-pcb-router](https://github.com/easyeda/easyeda-pcb-router/tree/caa8137a851376d113971a1fee8fe22d40b2ba31)，修订 `caa8137a851376d113971a1fee8fe22d40b2ba31`。
  - [README.md](https://github.com/easyeda/easyeda-pcb-router/blob/caa8137a851376d113971a1fee8fe22d40b2ba31/README.md)

这些链接是固定版本的知识来源，不会自动安装、运行上游扩展。文档/源码证据与真实客户端、板卡、制造验证分开记录。
