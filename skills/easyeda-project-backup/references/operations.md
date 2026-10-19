# 操作参考

## 第一个工具调用

调用 tools/list 实际返回的原生 `.help`，参数 `{}`，再查询 `doc.api` 帮助。
本工作流首先查询以下类，具体方法、参数、返回以当前客户端帮助为准：

```json
{"path": "doc.api", "input": {"className": "DMT_Project"}}
```

```json
{"path": "doc.api", "input": {"className": "SYS_FileSystem"}}
```

之后在选定会话中通过原生 `invoke` 执行已查询的 API。涉及扩展时先查询 `doc.external` 或 `functions`，确认上层接口实际存在；未暴露时报告缺口，不把源代码函数名直接当成工具。

## 完成判据

- 备份包含预期工程和库。
- 目标文件可读取。
- 只读归档与写回 PLM 分别授权。

## 官方来源

- [eext-export-design-archive](https://github.com/easyeda/eext-export-design-archive/tree/9f1e7b5aa5f53c730ed801fa3bd7e56de44a5f0d)，修订 `9f1e7b5aa5f53c730ed801fa3bd7e56de44a5f0d`。
  - [src/index.ts](https://github.com/easyeda/eext-export-design-archive/blob/9f1e7b5aa5f53c730ed801fa3bd7e56de44a5f0d/src/index.ts)
- [eext-batch-data-export](https://github.com/easyeda/eext-batch-data-export/tree/16c0b33ca318abf162d21a287e5695ed1d8c1e73)，修订 `16c0b33ca318abf162d21a287e5695ed1d8c1e73`。
  - [src/index.ts](https://github.com/easyeda/eext-batch-data-export/blob/16c0b33ca318abf162d21a287e5695ed1d8c1e73/src/index.ts)
- [eext-plm-integration-demo](https://github.com/easyeda/eext-plm-integration-demo/tree/92463b09f41d048b2a96593a8a2b34693c872115)，修订 `92463b09f41d048b2a96593a8a2b34693c872115`。
  - [src/index.ts](https://github.com/easyeda/eext-plm-integration-demo/blob/92463b09f41d048b2a96593a8a2b34693c872115/src/index.ts)
- [easyeda-viewer](https://github.com/easyeda/easyeda-viewer/tree/d2e1a71676a19780189d2fc99c6153de1f8f8f6a)，修订 `d2e1a71676a19780189d2fc99c6153de1f8f8f6a`。
  - [README.md](https://github.com/easyeda/easyeda-viewer/blob/d2e1a71676a19780189d2fc99c6153de1f8f8f6a/README.md)

这些链接是固定版本的知识来源，不会自动安装、运行上游扩展。文档/源码证据与真实客户端、板卡、制造验证分开记录。
