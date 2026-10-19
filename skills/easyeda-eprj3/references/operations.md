# 操作参考

## 第一个工具调用

调用 tools/list 实际返回的原生 `.help`，参数 `{}`，再查询 `doc.api` 帮助。
本工作流首先查询以下类，具体方法、参数、返回以当前客户端帮助为准：

```json
{"path": "doc.api", "input": {"className": "DMT_Project"}}
```

```json
{"path": "doc.api", "input": {"className": "DMT_Board"}}
```

之后在选定会话中通过原生 `invoke` 执行已查询的 API。涉及扩展时先查询 `doc.external` 或 `functions`，确认上层接口实际存在；未暴露时报告缺口，不把源代码函数名直接当成工具。

先阅读 [官方技能适配细则](official-adaptation.md)，其中保留领域关键约束与未捆绑工具的获取方式。

## 完成判据

- 项目索引、文档和库引用完整。
- 文件格式校验与电气验证分别报告。
- 旧工程未被强制转换。

## 官方来源

- [easyeda-eprj3-skill](https://github.com/easyeda/easyeda-eprj3-skill/tree/40c94e129df18e94232f8c94260134bfcac6cabf)，修订 `40c94e129df18e94232f8c94260134bfcac6cabf`。
  - [SKILL.md](https://github.com/easyeda/easyeda-eprj3-skill/blob/40c94e129df18e94232f8c94260134bfcac6cabf/SKILL.md)
- [easyeda-eprj3-format](https://github.com/easyeda/easyeda-eprj3-format/tree/3adee06f510b2d5181b80ff850c40b0bccbf75f0)，修订 `3adee06f510b2d5181b80ff850c40b0bccbf75f0`。
  - [README.md](https://github.com/easyeda/easyeda-eprj3-format/blob/3adee06f510b2d5181b80ff850c40b0bccbf75f0/README.md)
- [easyeda-client-cli](https://github.com/easyeda/easyeda-client-cli/tree/eba951a2c08b7872271b20b463dc7fe1cc5f231d)，修订 `eba951a2c08b7872271b20b463dc7fe1cc5f231d`。
  - [cli-for-ai.md](https://github.com/easyeda/easyeda-client-cli/blob/eba951a2c08b7872271b20b463dc7fe1cc5f231d/cli-for-ai.md)

这些链接是固定版本的知识来源，不会自动安装、运行上游扩展。文档/源码证据与真实客户端、板卡、制造验证分开记录。
