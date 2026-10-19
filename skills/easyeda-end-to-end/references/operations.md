# 操作参考

## 第一个工具调用

调用 tools/list 实际返回的原生 `.help`，参数 `{}`，再查询 `doc.api` 帮助。
本工作流首先查询以下类，具体方法、参数、返回以当前客户端帮助为准：

```json
{"path": "doc.api", "input": {"className": "DMT_Project"}}
```

```json
{"path": "doc.api", "input": {"className": "SCH_Drc"}}
```

```json
{"path": "doc.api", "input": {"className": "PCB_Document"}}
```

```json
{"path": "doc.api", "input": {"className": "PCB_Drc"}}
```

```json
{"path": "doc.api", "input": {"className": "PCB_ManufactureData"}}
```

之后在选定会话中通过原生 `invoke` 执行已查询的 API。涉及扩展时先查询 `doc.external` 或 `functions`，确认上层接口实际存在；未暴露时报告缺口，不把源代码函数名直接当成工具。

## 完成判据

- 每一阶段使用当前版本的实际结果。
- 失败或部分检查不被下游导出掩盖。
- 可编辑工程和制造包对应同一设计。

## 官方来源

- [easyeda-client-cli](https://github.com/easyeda/easyeda-client-cli/tree/eba951a2c08b7872271b20b463dc7fe1cc5f231d)，修订 `eba951a2c08b7872271b20b463dc7fe1cc5f231d`。
  - [cli-for-ai.md](https://github.com/easyeda/easyeda-client-cli/blob/eba951a2c08b7872271b20b463dc7fe1cc5f231d/cli-for-ai.md)
- [eext-ai-reuse-block-placement](https://github.com/easyeda/eext-ai-reuse-block-placement/tree/0a1b7536e9528b9e268861add2623eb7e33e47c3)，修订 `0a1b7536e9528b9e268861add2623eb7e33e47c3`。
  - [src/index.ts](https://github.com/easyeda/eext-ai-reuse-block-placement/blob/0a1b7536e9528b9e268861add2623eb7e33e47c3/src/index.ts)
  - [src/agent/tools.ts](https://github.com/easyeda/eext-ai-reuse-block-placement/blob/0a1b7536e9528b9e268861add2623eb7e33e47c3/src/agent/tools.ts)
  - [src/cbb.ts](https://github.com/easyeda/eext-ai-reuse-block-placement/blob/0a1b7536e9528b9e268861add2623eb7e33e47c3/src/cbb.ts)
- [eext-design-rule-generator](https://github.com/easyeda/eext-design-rule-generator/tree/2cf9635b335bf8c15cd046a1c2cf08f8b9118f88)，修订 `2cf9635b335bf8c15cd046a1c2cf08f8b9118f88`。
  - [src/index.ts](https://github.com/easyeda/eext-design-rule-generator/blob/2cf9635b335bf8c15cd046a1c2cf08f8b9118f88/src/index.ts)
  - [src/eda/runtime.ts](https://github.com/easyeda/eext-design-rule-generator/blob/2cf9635b335bf8c15cd046a1c2cf08f8b9118f88/src/eda/runtime.ts)
- [eext-jlc-order-dfm-checker](https://github.com/easyeda/eext-jlc-order-dfm-checker/tree/afd538786d510f537ad4fa47c6329e6a99dc7625)，修订 `afd538786d510f537ad4fa47c6329e6a99dc7625`。
  - [src/index.ts](https://github.com/easyeda/eext-jlc-order-dfm-checker/blob/afd538786d510f537ad4fa47c6329e6a99dc7625/src/index.ts)

这些链接是固定版本的知识来源，不会自动安装、运行上游扩展。文档/源码证据与真实客户端、板卡、制造验证分开记录。
