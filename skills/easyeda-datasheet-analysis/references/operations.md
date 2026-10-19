# 操作参考

## 第一个工具调用

调用 tools/list 实际返回的原生 `.help`，参数 `{}`，再查询 `doc.api` 帮助。
本工作流首先查询以下类，具体方法、参数、返回以当前客户端帮助为准：

```json
{"path": "doc.api", "input": {"className": "LIB_Device"}}
```

```json
{"path": "doc.api", "input": {"className": "LIB_Symbol"}}
```

```json
{"path": "doc.api", "input": {"className": "LIB_Footprint"}}
```

之后在选定会话中通过原生 `invoke` 执行已查询的 API。涉及扩展时先查询 `doc.external` 或 `functions`，确认上层接口实际存在；未暴露时报告缺口，不把源代码函数名直接当成工具。

## 完成判据

- 每个关键参数带页码或章节来源。
- 单位与典型值、最大值区分。
- 引脚方向与底视/顶视核对。

## 官方来源

- [eext-datasheet-helper](https://github.com/easyeda/eext-datasheet-helper/tree/6be8cf0b8e28131e011ba11bf887dab4f027bed9)，修订 `6be8cf0b8e28131e011ba11bf887dab4f027bed9`。
  - [src/index.ts](https://github.com/easyeda/eext-datasheet-helper/blob/6be8cf0b8e28131e011ba11bf887dab4f027bed9/src/index.ts)
- [eext-ai-library-builder](https://github.com/easyeda/eext-ai-library-builder/tree/27731deb50a3ca855874d5b70c32c5e2dc6888e0)，修订 `27731deb50a3ca855874d5b70c32c5e2dc6888e0`。
  - [src/index.ts](https://github.com/easyeda/eext-ai-library-builder/blob/27731deb50a3ca855874d5b70c32c5e2dc6888e0/src/index.ts)

这些链接是固定版本的知识来源，不会自动安装、运行上游扩展。文档/源码证据与真实客户端、板卡、制造验证分开记录。
