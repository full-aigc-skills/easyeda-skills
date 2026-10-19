# 操作参考

## 第一个工具调用

调用 tools/list 实际返回的原生 `.help`，参数 `{}`，再查询 `doc.api` 帮助。
本工作流首先查询以下类，具体方法、参数、返回以当前客户端帮助为准：

```json
{"path": "doc.api", "input": {"className": "PCB_Net"}}
```

```json
{"path": "doc.api", "input": {"className": "PCB_Drc"}}
```

之后在选定会话中通过原生 `invoke` 执行已查询的 API。涉及扩展时先查询 `doc.external` 或 `functions`，确认上层接口实际存在；未暴露时报告缺口，不把源代码函数名直接当成工具。

## 完成判据

- 路径对应实际 PCB。
- 未忽略器件与时钟参数。
- 余量结论包含假设。

## 官方来源

- [eext-timing-analysis](https://github.com/easyeda/eext-timing-analysis/tree/f5e338b0c5d8f892c0e366067f7b0c60d4039180)，修订 `f5e338b0c5d8f892c0e366067f7b0c60d4039180`。
  - [src/index.ts](https://github.com/easyeda/eext-timing-analysis/blob/f5e338b0c5d8f892c0e366067f7b0c60d4039180/src/index.ts)
- [eext-timing-diagram-tool](https://github.com/easyeda/eext-timing-diagram-tool/tree/596a50fb91d79ba0c99a02af22ad3c42d180b2b8)，修订 `596a50fb91d79ba0c99a02af22ad3c42d180b2b8`。
  - [src/index.ts](https://github.com/easyeda/eext-timing-diagram-tool/blob/596a50fb91d79ba0c99a02af22ad3c42d180b2b8/src/index.ts)

这些链接是固定版本的知识来源，不会自动安装、运行上游扩展。文档/源码证据与真实客户端、板卡、制造验证分开记录。
