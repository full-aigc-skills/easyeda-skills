# 操作参考

## 第一个工具调用

调用 tools/list 实际返回的原生 `.help`，参数 `{}`，再查询 `doc.api` 帮助。
本工作流首先查询以下类，具体方法、参数、返回以当前客户端帮助为准：

```json
{"path": "doc.api", "input": {"className": "SYS_ExternalApi"}}
```

```json
{"path": "doc.api", "input": {"className": "SYS_MessageBus"}}
```

```json
{"path": "doc.api", "input": {"className": "SYS_IFrame"}}
```

之后在选定会话中通过原生 `invoke` 执行已查询的 API。涉及扩展时先查询 `doc.external` 或 `functions`，确认上层接口实际存在；未暴露时报告缺口，不把源代码函数名直接当成工具。

先阅读 [官方技能适配细则](official-adaptation.md)，其中保留领域关键约束与未捆绑工具的获取方式。

## 完成判据

- 编译使用的是目标项目 SDK。
- 外部工具能发现真实注册接口。
- 导入无日志错误不等于功能验收通过。

## 官方来源

- [extension-dev-skill](https://github.com/easyeda/extension-dev-skill/tree/d9148cba524149d17afcbfd196fab3226a8df5da)，修订 `d9148cba524149d17afcbfd196fab3226a8df5da`。
  - [SKILL.md](https://github.com/easyeda/extension-dev-skill/blob/d9148cba524149d17afcbfd196fab3226a8df5da/SKILL.md)
- [easyeda-api-sdk](https://github.com/easyeda/easyeda-api-sdk/tree/f83525eb54f86f131cf90780ed3fa0237dbb75aa)，修订 `f83525eb54f86f131cf90780ed3fa0237dbb75aa`。
  - [README.md](https://github.com/easyeda/easyeda-api-sdk/blob/f83525eb54f86f131cf90780ed3fa0237dbb75aa/README.md)
- [extension-dev-mcp-tools](https://github.com/easyeda/extension-dev-mcp-tools/tree/edce042465fcccb6dc9cce8c17179de121bbb1a1)，修订 `edce042465fcccb6dc9cce8c17179de121bbb1a1`。
  - [README.md](https://github.com/easyeda/extension-dev-mcp-tools/blob/edce042465fcccb6dc9cce8c17179de121bbb1a1/README.md)
- [eext-extension-demo](https://github.com/easyeda/eext-extension-demo/tree/739c9a33aeb03a2715966c4ad5cf3af919b599ef)，修订 `739c9a33aeb03a2715966c4ad5cf3af919b599ef`。
  - [src/index.ts](https://github.com/easyeda/eext-extension-demo/blob/739c9a33aeb03a2715966c4ad5cf3af919b599ef/src/index.ts)
- [eext-api-debug-tool](https://github.com/easyeda/eext-api-debug-tool/tree/e7bf7376bcac92879f5eb2414ceef7fb7078b586)，修订 `e7bf7376bcac92879f5eb2414ceef7fb7078b586`。
  - [src/index.ts](https://github.com/easyeda/eext-api-debug-tool/blob/e7bf7376bcac92879f5eb2414ceef7fb7078b586/src/index.ts)
- [eext-api-test-tool](https://github.com/easyeda/eext-api-test-tool/tree/317bd75e32f0248285fd9d4551e70ed046ef443f)，修订 `317bd75e32f0248285fd9d4551e70ed046ef443f`。
  - [src/index.ts](https://github.com/easyeda/eext-api-test-tool/blob/317bd75e32f0248285fd9d4551e70ed046ef443f/src/index.ts)
- [eext-external-tool-integration-demo](https://github.com/easyeda/eext-external-tool-integration-demo/tree/9b6e6f325a2d4210205f4904389871155a058f11)，修订 `9b6e6f325a2d4210205f4904389871155a058f11`。
  - [src/index.ts](https://github.com/easyeda/eext-external-tool-integration-demo/blob/9b6e6f325a2d4210205f4904389871155a058f11/src/index.ts)

这些链接是固定版本的知识来源，不会自动安装、运行上游扩展。文档/源码证据与真实客户端、板卡、制造验证分开记录。
