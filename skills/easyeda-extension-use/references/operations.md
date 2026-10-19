# 操作参考

## 第一个工具调用

调用 tools/list 实际返回的原生 `.help`，参数 `{}`，再查询 `doc.api` 帮助。
本工作流首先查询以下类，具体方法、参数、返回以当前客户端帮助为准：

```json
{"path": "doc.api", "input": {"className": "SYS_ExternalApi"}}
```

```json
{"path": "doc.api", "input": {"className": "SYS_Help"}}
```

之后在选定会话中通过原生 `invoke` 执行已查询的 API。涉及扩展时先查询 `doc.external` 或 `functions`，确认上层接口实际存在；未暴露时报告缺口，不把源代码函数名直接当成工具。

## 完成判据

- 已确认内部扩展 UUID、版本、启用状态与接口目录。
- 只读任务没有调用工程修改、保存或制造导出。
- 工程、文档、对象和实际输出分别验证。

## 官方来源

- [extension-dev-skill](https://github.com/easyeda/extension-dev-skill/tree/d9148cba524149d17afcbfd196fab3226a8df5da)，修订 `d9148cba524149d17afcbfd196fab3226a8df5da`。
  - [SKILL.md](https://github.com/easyeda/extension-dev-skill/blob/d9148cba524149d17afcbfd196fab3226a8df5da/SKILL.md)
- [easyeda-client-cli](https://github.com/easyeda/easyeda-client-cli/tree/eba951a2c08b7872271b20b463dc7fe1cc5f231d)，修订 `eba951a2c08b7872271b20b463dc7fe1cc5f231d`。
  - [cli-for-ai.md](https://github.com/easyeda/easyeda-client-cli/blob/eba951a2c08b7872271b20b463dc7fe1cc5f231d/cli-for-ai.md)

这些链接是固定版本的知识来源，不会自动安装、运行上游扩展。文档/源码证据与真实客户端、板卡、制造验证分开记录。
