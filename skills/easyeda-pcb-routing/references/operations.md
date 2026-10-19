# 操作参考

## 第一个工具调用

调用 tools/list 实际返回的原生 `.help`，参数 `{}`，再查询 `doc.api` 帮助。
本工作流首先查询以下类，具体方法、参数、返回以当前客户端帮助为准：

```json
{"path": "doc.api", "input": {"className": "PCB_Document"}}
```

```json
{"path": "doc.api", "input": {"className": "PCB_Drc"}}
```

```json
{"path": "doc.api", "input": {"className": "PCB_Net"}}
```

之后在选定会话中通过原生 `invoke` 执行已查询的 API。涉及扩展时先查询 `doc.external` 或 `functions`，确认上层接口实际存在；未暴露时报告缺口，不把源代码函数名直接当成工具。

## 完成判据

- 全部目标网络布通或明确列出失败。
- 没有损坏已有人工布线。
- DRC 结果真实读取。
- 自动布线报告成功后仍运行 DRC；重建覆铜并检查被遗漏的连通岛。

## 官方来源

- [easyeda-client-cli](https://github.com/easyeda/easyeda-client-cli/tree/eba951a2c08b7872271b20b463dc7fe1cc5f231d)，修订 `eba951a2c08b7872271b20b463dc7fe1cc5f231d`。
  - [cli-for-ai.md](https://github.com/easyeda/easyeda-client-cli/blob/eba951a2c08b7872271b20b463dc7fe1cc5f231d/cli-for-ai.md)
- [easyeda-pcb-router](https://github.com/easyeda/easyeda-pcb-router/tree/caa8137a851376d113971a1fee8fe22d40b2ba31)，修订 `caa8137a851376d113971a1fee8fe22d40b2ba31`。
  - [README.md](https://github.com/easyeda/easyeda-pcb-router/blob/caa8137a851376d113971a1fee8fe22d40b2ba31/README.md)
- [eext-diff-pair-assistant](https://github.com/easyeda/eext-diff-pair-assistant/tree/99fc251f2a4a550d72609a54bd1d96dade84cf1f)，修订 `99fc251f2a4a550d72609a54bd1d96dade84cf1f`。
  - [src/index.ts](https://github.com/easyeda/eext-diff-pair-assistant/blob/99fc251f2a4a550d72609a54bd1d96dade84cf1f/src/index.ts)
- [eext-pad-fanout](https://github.com/easyeda/eext-pad-fanout/tree/7c88e571457e6d63463b7cb391e1e62bdbdd02d7)，修订 `7c88e571457e6d63463b7cb391e1e62bdbdd02d7`。
  - [src/index.ts](https://github.com/easyeda/eext-pad-fanout/blob/7c88e571457e6d63463b7cb391e1e62bdbdd02d7/src/index.ts)

这些链接是固定版本的知识来源，不会自动安装、运行上游扩展。文档/源码证据与真实客户端、板卡、制造验证分开记录。
