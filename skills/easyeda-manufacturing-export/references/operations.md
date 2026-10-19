# 操作参考

## 第一个工具调用

调用 tools/list 实际返回的原生 `.help`，参数 `{}`，再查询 `doc.api` 帮助。
本工作流首先查询以下类，具体方法、参数、返回以当前客户端帮助为准：

```json
{"path": "doc.api", "input": {"className": "PCB_ManufactureData"}}
```

```json
{"path": "doc.api", "input": {"className": "SYS_FileSystem"}}
```

之后在选定会话中通过原生 `invoke` 执行已查询的 API。涉及扩展时先查询 `doc.external` 或 `functions`，确认上层接口实际存在；未暴露时报告缺口，不把源代码函数名直接当成工具。

## 完成判据

- 铜层、板框和钻孔完整。
- BOM 位号与贴片坐标一致。
- 文件可以重新读取和预览。

## 官方来源

- [easyeda-client-cli](https://github.com/easyeda/easyeda-client-cli/tree/eba951a2c08b7872271b20b463dc7fe1cc5f231d)，修订 `eba951a2c08b7872271b20b463dc7fe1cc5f231d`。
  - [cli-for-ai.md](https://github.com/easyeda/easyeda-client-cli/blob/eba951a2c08b7872271b20b463dc7fe1cc5f231d/cli-for-ai.md)
- [eext-batch-data-export](https://github.com/easyeda/eext-batch-data-export/tree/16c0b33ca318abf162d21a287e5695ed1d8c1e73)，修订 `16c0b33ca318abf162d21a287e5695ed1d8c1e73`。
  - [src/index.ts](https://github.com/easyeda/eext-batch-data-export/blob/16c0b33ca318abf162d21a287e5695ed1d8c1e73/src/index.ts)
- [eext-export-gencad](https://github.com/easyeda/eext-export-gencad/tree/aba4dff5b0fb8e1c5ad8288b07eb56b01dd0ab9e)，修订 `aba4dff5b0fb8e1c5ad8288b07eb56b01dd0ab9e`。
  - [src/index.ts](https://github.com/easyeda/eext-export-gencad/blob/aba4dff5b0fb8e1c5ad8288b07eb56b01dd0ab9e/src/index.ts)
- [eext-export-hyperlynx](https://github.com/easyeda/eext-export-hyperlynx/tree/39acea28a1d3fb1628b48c08954723fecaa81f3b)，修订 `39acea28a1d3fb1628b48c08954723fecaa81f3b`。
  - [src/index.ts](https://github.com/easyeda/eext-export-hyperlynx/blob/39acea28a1d3fb1628b48c08954723fecaa81f3b/src/index.ts)
- [eext-export-pcb-to-svg](https://github.com/easyeda/eext-export-pcb-to-svg/tree/f68898d18c8279e2aaf84a5b2ff07969ebeb005e)，修订 `f68898d18c8279e2aaf84a5b2ff07969ebeb005e`。
  - [src/index.ts](https://github.com/easyeda/eext-export-pcb-to-svg/blob/f68898d18c8279e2aaf84a5b2ff07969ebeb005e/src/index.ts)
- [eext-gerber-viewer](https://github.com/easyeda/eext-gerber-viewer/tree/085eb879b61ee84dfc7288852b490990282327e5)，修订 `085eb879b61ee84dfc7288852b490990282327e5`。
  - [src/index.ts](https://github.com/easyeda/eext-gerber-viewer/blob/085eb879b61ee84dfc7288852b490990282327e5/src/index.ts)
- [eext-gencad-viewer](https://github.com/easyeda/eext-gencad-viewer/tree/b537e0cc0dfcf5be544e2d0589f457f719fb21a1)，修订 `b537e0cc0dfcf5be544e2d0589f457f719fb21a1`。
  - [src/index.ts](https://github.com/easyeda/eext-gencad-viewer/blob/b537e0cc0dfcf5be544e2d0589f457f719fb21a1/src/index.ts)
- [online-gencad-viewer](https://github.com/easyeda/online-gencad-viewer/tree/cdc76cdaa520765831bf7e3674e47cb213c975f8)，修订 `cdc76cdaa520765831bf7e3674e47cb213c975f8`。
  - [README.md](https://github.com/easyeda/online-gencad-viewer/blob/cdc76cdaa520765831bf7e3674e47cb213c975f8/README.md)
- [easyeda-viewer](https://github.com/easyeda/easyeda-viewer/tree/d2e1a71676a19780189d2fc99c6153de1f8f8f6a)，修订 `d2e1a71676a19780189d2fc99c6153de1f8f8f6a`。
  - [README.md](https://github.com/easyeda/easyeda-viewer/blob/d2e1a71676a19780189d2fc99c6153de1f8f8f6a/README.md)

这些链接是固定版本的知识来源，不会自动安装、运行上游扩展。文档/源码证据与真实客户端、板卡、制造验证分开记录。
