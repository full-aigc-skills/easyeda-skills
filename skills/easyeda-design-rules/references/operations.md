# 操作参考

## 第一个工具调用

调用 tools/list 实际返回的原生 `.help`，参数 `{}`，再查询 `doc.api` 帮助。
本工作流首先查询以下类，具体方法、参数、返回以当前客户端帮助为准：

```json
{"path": "doc.api", "input": {"className": "PCB_Drc"}}
```

```json
{"path": "doc.api", "input": {"className": "PCB_Layer"}}
```

之后在选定会话中通过原生 `invoke` 执行已查询的 API。涉及扩展时先查询 `doc.external` 或 `functions`，确认上层接口实际存在；未暴露时报告缺口，不把源代码函数名直接当成工具。

## 完成判据

- 规则数值和单位与输入匹配。
- 未覆盖无关用户规则。
- 差分正负网络确实存在。

## 官方来源

- [eext-design-rule-generator](https://github.com/easyeda/eext-design-rule-generator/tree/2cf9635b335bf8c15cd046a1c2cf08f8b9118f88)，修订 `2cf9635b335bf8c15cd046a1c2cf08f8b9118f88`。
  - [src/index.ts](https://github.com/easyeda/eext-design-rule-generator/blob/2cf9635b335bf8c15cd046a1c2cf08f8b9118f88/src/index.ts)
  - [src/eda/runtime.ts](https://github.com/easyeda/eext-design-rule-generator/blob/2cf9635b335bf8c15cd046a1c2cf08f8b9118f88/src/eda/runtime.ts)
- [eext-diff-pair-assistant](https://github.com/easyeda/eext-diff-pair-assistant/tree/99fc251f2a4a550d72609a54bd1d96dade84cf1f)，修订 `99fc251f2a4a550d72609a54bd1d96dade84cf1f`。
  - [src/index.ts](https://github.com/easyeda/eext-diff-pair-assistant/blob/99fc251f2a4a550d72609a54bd1d96dade84cf1f/src/index.ts)

这些链接是固定版本的知识来源，不会自动安装、运行上游扩展。文档/源码证据与真实客户端、板卡、制造验证分开记录。
