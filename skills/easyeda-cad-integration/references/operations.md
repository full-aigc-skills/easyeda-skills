# 操作参考

## 第一个工具调用

调用 tools/list 实际返回的原生 `.help`，参数 `{}`，再查询 `doc.api` 帮助。
本工作流首先查询以下类，具体方法、参数、返回以当前客户端帮助为准：

```json
{"path": "doc.api", "input": {"className": "PCB_ManufactureData"}}
```

```json
{"path": "doc.api", "input": {"className": "PCB_Document"}}
```

之后在选定会话中通过原生 `invoke` 执行已查询的 API。涉及扩展时先查询 `doc.external` 或 `functions`，确认上层接口实际存在；未暴露时报告缺口，不把源代码函数名直接当成工具。

## 完成判据

- 机械尺寸与 PCB 对应。
- 模型缺失被明确报告。
- 导回修改没有覆盖电气设计。

## 官方来源

- [eext-mcad-integration-with-freecad](https://github.com/easyeda/eext-mcad-integration-with-freecad/tree/e3c30a527194d34def8ada4f84451de298caa048)，修订 `e3c30a527194d34def8ada4f84451de298caa048`。
  - [src/index.ts](https://github.com/easyeda/eext-mcad-integration-with-freecad/blob/e3c30a527194d34def8ada4f84451de298caa048/src/index.ts)
- [eext-mcad-integration-with-solidworks](https://github.com/easyeda/eext-mcad-integration-with-solidworks/tree/1368d185950b07492737eab27e542b631f3199f5)，修订 `1368d185950b07492737eab27e542b631f3199f5`。
  - [src/index.ts](https://github.com/easyeda/eext-mcad-integration-with-solidworks/blob/1368d185950b07492737eab27e542b631f3199f5/src/index.ts)
- [mcad-integration-with-fusion360](https://github.com/easyeda/mcad-integration-with-fusion360/tree/50745428f53363e27628395751d211bfffdcaf15)，修订 `50745428f53363e27628395751d211bfffdcaf15`。
  - [README.md](https://github.com/easyeda/mcad-integration-with-fusion360/blob/50745428f53363e27628395751d211bfffdcaf15/README.md)
- [eext-pcb-render-with-blender](https://github.com/easyeda/eext-pcb-render-with-blender/tree/6c8aef2be34d7733eb5e684f80af1059864013d1)，修订 `6c8aef2be34d7733eb5e684f80af1059864013d1`。
  - [src/index.ts](https://github.com/easyeda/eext-pcb-render-with-blender/blob/6c8aef2be34d7733eb5e684f80af1059864013d1/src/index.ts)
- [eext-dwg-importer](https://github.com/easyeda/eext-dwg-importer/tree/cdf3814c8b775d6e5ee19f4f9d8f027b74ec5825)，修订 `cdf3814c8b775d6e5ee19f4f9d8f027b74ec5825`。
  - [src/index.ts](https://github.com/easyeda/eext-dwg-importer/blob/cdf3814c8b775d6e5ee19f4f9d8f027b74ec5825/src/index.ts)

这些链接是固定版本的知识来源，不会自动安装、运行上游扩展。文档/源码证据与真实客户端、板卡、制造验证分开记录。
