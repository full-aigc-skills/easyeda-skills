# 操作参考

## 第一个工具调用

调用 tools/list 实际返回的原生 `.help`，参数 `{}`，再查询 `doc.api` 帮助。
本工作流首先查询以下类，具体方法、参数、返回以当前客户端帮助为准：

```json
{"path": "doc.api", "input": {"className": "SYS_FormatConversion"}}
```

```json
{"path": "doc.api", "input": {"className": "DMT_Project"}}
```

之后在选定会话中通过原生 `invoke` 执行已查询的 API。涉及扩展时先查询 `doc.external` 或 `functions`，确认上层接口实际存在；未暴露时报告缺口，不把源代码函数名直接当成工具。

## 完成判据

- 源工程受到保护。
- 关键对象与连接数量可比较。
- 目标客户端可继续编辑。

## 官方来源

- [kicad-to-easyeda-eprj3](https://github.com/easyeda/kicad-to-easyeda-eprj3/tree/a16545dd7922455e6a20f69adeb234c924af08b5)，修订 `a16545dd7922455e6a20f69adeb234c924af08b5`。
  - [README.md](https://github.com/easyeda/kicad-to-easyeda-eprj3/blob/a16545dd7922455e6a20f69adeb234c924af08b5/README.md)
- [easyeda-file-format-v2](https://github.com/easyeda/easyeda-file-format-v2/tree/63f38c2758cbe2456e8b5c7e76469369430d94af)，修订 `63f38c2758cbe2456e8b5c7e76469369430d94af`。
  - [README.md](https://github.com/easyeda/easyeda-file-format-v2/blob/63f38c2758cbe2456e8b5c7e76469369430d94af/README.md)
- [easyeda-std-file-format](https://github.com/easyeda/easyeda-std-file-format/tree/8cbccfdd86b82100036044940f142ab85972699c)，修订 `8cbccfdd86b82100036044940f142ab85972699c`。
  - [README.md](https://github.com/easyeda/easyeda-std-file-format/blob/8cbccfdd86b82100036044940f142ab85972699c/README.md)
- [easyeda-eprj3-format](https://github.com/easyeda/easyeda-eprj3-format/tree/3adee06f510b2d5181b80ff850c40b0bccbf75f0)，修订 `3adee06f510b2d5181b80ff850c40b0bccbf75f0`。
  - [README.md](https://github.com/easyeda/easyeda-eprj3-format/blob/3adee06f510b2d5181b80ff850c40b0bccbf75f0/README.md)

这些链接是固定版本的知识来源，不会自动安装、运行上游扩展。文档/源码证据与真实客户端、板卡、制造验证分开记录。
