# 操作参考

## 第一个工具调用

调用 tools/list 实际返回的原生 `.help`，参数 `{}`，再查询 `doc.api` 帮助。
本工作流首先查询以下类，具体方法、参数、返回以当前客户端帮助为准：

```json
{"path": "doc.api", "input": {"className": "DMT_Project"}}
```

之后在选定会话中通过原生 `invoke` 执行已查询的 API。涉及扩展时先查询 `doc.external` 或 `functions`，确认上层接口实际存在；未暴露时报告缺口，不把源代码函数名直接当成工具。

先阅读 [官方技能适配细则](official-adaptation.md)，其中保留领域关键约束与未捆绑工具的获取方式。

## 完成判据

- DOCHEAD、CANVAS 适用域正确。
- 记录结束符和 ID 合法。
- 实际对象与网表和目标一致。

## 官方来源

- [easyeda-format-skill](https://github.com/easyeda/easyeda-format-skill/tree/9e42727cc4cf13a8e442140e8e7794ae94d5f41b)，修订 `9e42727cc4cf13a8e442140e8e7794ae94d5f41b`。
  - [SKILL.md](https://github.com/easyeda/easyeda-format-skill/blob/9e42727cc4cf13a8e442140e8e7794ae94d5f41b/SKILL.md)
- [easyeda-file-format](https://github.com/easyeda/easyeda-file-format/tree/9186c4ac43e67d1bb111ada3f5cc020b76bc543a)，修订 `9186c4ac43e67d1bb111ada3f5cc020b76bc543a`。
  - [README.md](https://github.com/easyeda/easyeda-file-format/blob/9186c4ac43e67d1bb111ada3f5cc020b76bc543a/README.md)
- [easyeda-file-format-v2](https://github.com/easyeda/easyeda-file-format-v2/tree/63f38c2758cbe2456e8b5c7e76469369430d94af)，修订 `63f38c2758cbe2456e8b5c7e76469369430d94af`。
  - [README.md](https://github.com/easyeda/easyeda-file-format-v2/blob/63f38c2758cbe2456e8b5c7e76469369430d94af/README.md)

这些链接是固定版本的知识来源，不会自动安装、运行上游扩展。文档/源码证据与真实客户端、板卡、制造验证分开记录。
