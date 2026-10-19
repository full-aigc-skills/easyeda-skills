# 操作参考

## 第一个工具调用

调用 tools/list 实际返回的原生 `.help`，参数 `{}`，再查询 `doc.api` 帮助。
本工作流首先查询以下类，具体方法、参数、返回以当前客户端帮助为准：

```json
{"path": "doc.api", "input": {"className": "SCH_PrimitiveComponent"}}
```

```json
{"path": "doc.api", "input": {"className": "SCH_PrimitiveWire"}}
```

```json
{"path": "doc.api", "input": {"className": "SCH_PrimitiveRectangle"}}
```

之后在选定会话中通过原生 `invoke` 执行已查询的 API。涉及扩展时先查询 `doc.external` 或 `functions`，确认上层接口实际存在；未暴露时报告缺口，不把源代码函数名直接当成工具。

先阅读 [官方技能适配细则](official-adaptation.md)，其中保留领域关键约束与未捆绑工具的获取方式。

## 完成判据

- 无元件与标识符遮挡。
- 没有遗留旧网络标签。
- 电气连接与映射一致。

## 官方来源

- [easyeda-enhanced-schematic-skill](https://github.com/easyeda/easyeda-enhanced-schematic-skill/tree/0c4b9a0ad94d532923dee5c828a6efa7444f4506)，修订 `0c4b9a0ad94d532923dee5c828a6efa7444f4506`。
  - [SKILL.md](https://github.com/easyeda/easyeda-enhanced-schematic-skill/blob/0c4b9a0ad94d532923dee5c828a6efa7444f4506/SKILL.md)

这些链接是固定版本的知识来源，不会自动安装、运行上游扩展。文档/源码证据与真实客户端、板卡、制造验证分开记录。
