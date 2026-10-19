# 操作参考

## 第一个工具调用

调用 tools/list 实际返回的原生 `.help`，参数 `{}`，再查询 `doc.api` 帮助。
本工作流首先查询以下类，具体方法、参数、返回以当前客户端帮助为准：

```json
{"path": "doc.api", "input": {"className": "DMT_Project"}}
```

```json
{"path": "doc.api", "input": {"className": "DMT_SelectControl"}}
```

之后在选定会话中通过原生 `invoke` 执行已查询的 API。涉及扩展时先查询 `doc.external` 或 `functions`，确认上层接口实际存在；未暴露时报告缺口，不把源代码函数名直接当成工具。

## 完成判据

- 会话、工程和目标文档匹配。
- 没有将静态文档当成执行结果。
- 交付包含可继续编辑的工程。

## 官方来源

- [easyeda-client-cli](https://github.com/easyeda/easyeda-client-cli/tree/eba951a2c08b7872271b20b463dc7fe1cc5f231d)，修订 `eba951a2c08b7872271b20b463dc7fe1cc5f231d`。
  - [cli-for-ai.md](https://github.com/easyeda/easyeda-client-cli/blob/eba951a2c08b7872271b20b463dc7fe1cc5f231d/cli-for-ai.md)
- [easyeda-api-skill](https://github.com/easyeda/easyeda-api-skill/tree/d5a0b1c68304ec60fc9387570ffb912764f937b1)，修订 `d5a0b1c68304ec60fc9387570ffb912764f937b1`。
  - [SKILL.md](https://github.com/easyeda/easyeda-api-skill/blob/d5a0b1c68304ec60fc9387570ffb912764f937b1/SKILL.md)

这些链接是固定版本的知识来源，不会自动安装、运行上游扩展。文档/源码证据与真实客户端、板卡、制造验证分开记录。
