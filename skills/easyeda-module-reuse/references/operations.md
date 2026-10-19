# 操作参考

## 第一个工具调用

调用 tools/list 实际返回的原生 `.help`，参数 `{}`，再查询 `doc.api` 帮助。
本工作流首先查询以下类，具体方法、参数、返回以当前客户端帮助为准：

```json
{"path": "doc.api", "input": {"className": "LIB_Cbb"}}
```

```json
{"path": "doc.api", "input": {"className": "DMT_Board"}}
```

```json
{"path": "doc.api", "input": {"className": "DMT_Schematic"}}
```

之后在选定会话中通过原生 `invoke` 执行已查询的 API。涉及扩展时先查询 `doc.external` 或 `functions`，确认上层接口实际存在；未暴露时报告缺口，不把源代码函数名直接当成工具。

## 完成判据

- 模块实际存在于所选库。
- 新增对象和图页属于目标工程。
- 连接按实际网表复核。

## 官方来源

- [eext-ai-reuse-block-placement](https://github.com/easyeda/eext-ai-reuse-block-placement/tree/0a1b7536e9528b9e268861add2623eb7e33e47c3)，修订 `0a1b7536e9528b9e268861add2623eb7e33e47c3`。
  - [src/index.ts](https://github.com/easyeda/eext-ai-reuse-block-placement/blob/0a1b7536e9528b9e268861add2623eb7e33e47c3/src/index.ts)
  - [src/agent/tools.ts](https://github.com/easyeda/eext-ai-reuse-block-placement/blob/0a1b7536e9528b9e268861add2623eb7e33e47c3/src/agent/tools.ts)
  - [src/cbb.ts](https://github.com/easyeda/eext-ai-reuse-block-placement/blob/0a1b7536e9528b9e268861add2623eb7e33e47c3/src/cbb.ts)

这些链接是固定版本的知识来源，不会自动安装、运行上游扩展。文档/源码证据与真实客户端、板卡、制造验证分开记录。
