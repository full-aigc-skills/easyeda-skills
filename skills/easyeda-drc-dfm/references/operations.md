# 操作参考

## 第一个工具调用

调用 tools/list 实际返回的原生 `.help`，参数 `{}`，再查询 `doc.api` 帮助。
本工作流首先查询以下类，具体方法、参数、返回以当前客户端帮助为准：

```json
{"path": "doc.api", "input": {"className": "SCH_Drc"}}
```

```json
{"path": "doc.api", "input": {"className": "PCB_Drc"}}
```

之后在选定会话中通过原生 `invoke` 执行已查询的 API。涉及扩展时先查询 `doc.external` 或 `functions`，确认上层接口实际存在；未暴露时报告缺口，不把源代码函数名直接当成工具。

## 完成判据

- 检查范围与当前工程一致。
- 未检查项目未被当成通过。
- 检查报告可定位具体对象。

## 官方来源

- [eext-jlc-order-dfm-checker](https://github.com/easyeda/eext-jlc-order-dfm-checker/tree/afd538786d510f537ad4fa47c6329e6a99dc7625)，修订 `afd538786d510f537ad4fa47c6329e6a99dc7625`。
  - [src/index.ts](https://github.com/easyeda/eext-jlc-order-dfm-checker/blob/afd538786d510f537ad4fa47c6329e6a99dc7625/src/index.ts)
- [eext-signal-absence-detection](https://github.com/easyeda/eext-signal-absence-detection/tree/78f8ca3437e34c2f7976860a8e61adc511e36dd9)，修订 `78f8ca3437e34c2f7976860a8e61adc511e36dd9`。
  - [README.md](https://github.com/easyeda/eext-signal-absence-detection/blob/78f8ca3437e34c2f7976860a8e61adc511e36dd9/README.md)

这些链接是固定版本的知识来源，不会自动安装、运行上游扩展。文档/源码证据与真实客户端、板卡、制造验证分开记录。
