# 官方来源与执行边界

本次获取组织公开仓库清单 97 项，为每项固定 HEAD commit 并记录实际读取的 README、SKILL 或入口源码。对布线导入、网表导入、模块复用、规则生成等关键路径补充了实现文件。文件清单与摘要见 source-lock.json。没有运行上游工程、安装 .eext 或逐项审计所有源码。

## 提炼时保留的关键差异

- 原生 MCP 与 Run API Gateway 是两条连接路线，本包默认只使用原生服务；不启动旧 Bridge。
- 原理图扇出必须基于真实 pin 坐标和位号映射；四脚按键同极引脚的内部连接不能靠视觉猜测。
- 网表导入器可能跳过器件失败，存在按名称首项匹配及网络大写处理；导入后必须回读实际数量和网络，不能只看“执行结束”。
- Freerouting 集成有删除现有线/弧/过孔再导入的路径，并可能在没有消费 DRC 返回值时继续报告 success。先用候选副本，单独判断连通与 DRC。
- DFM 有捕获异常后返回部分结果的路径；缺少某类检查不能当作该类通过。
- 原生自动布线接口及扩展接口版本相关。自动布线任务启动、失败网络列表和全部网络完成需要分别判断。
- 部分扩展仅暴露菜单，不能把 TypeScript 导出函数直接当成原生 MCP 工具。先查询 functions/doc.external；缺少可调用入口时报告或补适配。
- 格式技能、eprj3 脚本与原理图 API 的坐标约定不能混用。完整 Schema 与官方查询脚本没有随本包捆绑。
- 价格计算示例不代表官方实时制造报价；知识库、联网分析和器件服务的可用性依赖真实服务。

## 全量映射

| 官方仓库（固定修订） | 对应技能 | 处理 | 已读文件数 |
|---|---|---|---|
| [circuitjs1-easyeda](https://github.com/easyeda/circuitjs1-easyeda/tree/8db75067d81cfcac180edff910716927f89760df) | `easyeda-simulation` | 领域工作流来源 | 1 |
| [easyeda-api-i18n](https://github.com/easyeda/easyeda-api-i18n/tree/087ac9802636c02539426e5ae5465de69edfff7f) | `easyeda-api` | 领域工作流来源 | 1 |
| [easyeda-api-sdk](https://github.com/easyeda/easyeda-api-sdk/tree/f83525eb54f86f131cf90780ed3fa0237dbb75aa) | `easyeda-extension-development` | 领域工作流来源 | 1 |
| [easyeda-api-skill](https://github.com/easyeda/easyeda-api-skill/tree/d5a0b1c68304ec60fc9387570ffb912764f937b1) | `easyeda-use`, `easyeda-mcp-setup`, `easyeda-api` | 领域工作流来源 | 2 |
| [easyeda-client-cli](https://github.com/easyeda/easyeda-client-cli/tree/eba951a2c08b7872271b20b463dc7fe1cc5f231d) | `easyeda-use`, `easyeda-mcp-setup`, `easyeda-api`, `easyeda-eprj3`, `easyeda-pcb-layout`, `easyeda-pcb-routing`, `easyeda-manufacturing-export`, `easyeda-end-to-end` | 领域工作流来源 | 2 |
| [easyeda-documents](https://github.com/easyeda/easyeda-documents/tree/c5637b5f1fa0df90628032ac8ec3150a1e76d58b) | — | 已归档，仅作历史参考 | 1 |
| [easyeda-enhanced-schematic-skill](https://github.com/easyeda/easyeda-enhanced-schematic-skill/tree/0c4b9a0ad94d532923dee5c828a6efa7444f4506) | `easyeda-schematic-net-fanout` | 领域工作流来源 | 2 |
| [easyeda-eprj3-format](https://github.com/easyeda/easyeda-eprj3-format/tree/3adee06f510b2d5181b80ff850c40b0bccbf75f0) | `easyeda-eprj3`, `easyeda-project-migration` | 领域工作流来源 | 1 |
| [easyeda-eprj3-skill](https://github.com/easyeda/easyeda-eprj3-skill/tree/40c94e129df18e94232f8c94260134bfcac6cabf) | `easyeda-eprj3` | 领域工作流来源 | 2 |
| [easyeda-file-format](https://github.com/easyeda/easyeda-file-format/tree/9186c4ac43e67d1bb111ada3f5cc020b76bc543a) | `easyeda-format-skill` | 领域工作流来源 | 1 |
| [easyeda-file-format-v2](https://github.com/easyeda/easyeda-file-format-v2/tree/63f38c2758cbe2456e8b5c7e76469369430d94af) | `easyeda-format-skill`, `easyeda-project-migration` | 领域工作流来源 | 1 |
| [easyeda-format-skill](https://github.com/easyeda/easyeda-format-skill/tree/9e42727cc4cf13a8e442140e8e7794ae94d5f41b) | `easyeda-format-skill` | 领域工作流来源 | 2 |
| [easyeda-netlist-format](https://github.com/easyeda/easyeda-netlist-format/tree/4e3997215e3241ba75d7287fbd4743231e32f7a6) | `easyeda-netlist-import`, `easyeda-netlist-review` | 领域工作流来源 | 1 |
| [easyeda-pcb-router](https://github.com/easyeda/easyeda-pcb-router/tree/caa8137a851376d113971a1fee8fe22d40b2ba31) | `easyeda-pcb-routing`, `easyeda-freerouting` | 领域工作流来源 | 1 |
| [easyeda-simulation-engine](https://github.com/easyeda/easyeda-simulation-engine/tree/f06a1dd20b60ea37284ab8033269ddf1212f31af) | `easyeda-simulation` | 领域工作流来源 | 1 |
| [easyeda-std-file-format](https://github.com/easyeda/easyeda-std-file-format/tree/8cbccfdd86b82100036044940f142ab85972699c) | `easyeda-project-migration` | 领域工作流来源 | 1 |
| [easyeda-std-i18n](https://github.com/easyeda/easyeda-std-i18n/tree/407b619c72d686bdd2988ba13a7dd1b3948176d9) | — | 已归档，仅作历史参考 | 1 |
| [easyeda-viewer](https://github.com/easyeda/easyeda-viewer/tree/d2e1a71676a19780189d2fc99c6153de1f8f8f6a) | `easyeda-manufacturing-export`, `easyeda-project-backup` | 领域工作流来源 | 1 |
| [eext-ai-device-standardization](https://github.com/easyeda/eext-ai-device-standardization/tree/89abac48075bd4e0ebc2a30bee55939251f8660f) | `easyeda-component-library` | 领域工作流来源 | 2 |
| [eext-ai-library-builder](https://github.com/easyeda/eext-ai-library-builder/tree/27731deb50a3ca855874d5b70c32c5e2dc6888e0) | `easyeda-component-library`, `easyeda-datasheet-analysis` | 领域工作流来源 | 2 |
| [eext-ai-reuse-block-placement](https://github.com/easyeda/eext-ai-reuse-block-placement/tree/0a1b7536e9528b9e268861add2623eb7e33e47c3) | `easyeda-schematic-design`, `easyeda-module-reuse`, `easyeda-end-to-end` | 领域工作流来源 | 4 |
| [eext-ai-symbol-builder](https://github.com/easyeda/eext-ai-symbol-builder/tree/e9fb3b167356c85077307712f09e3133bd632585) | `easyeda-component-library` | 领域工作流来源 | 2 |
| [eext-api-debug-tool](https://github.com/easyeda/eext-api-debug-tool/tree/e7bf7376bcac92879f5eb2414ceef7fb7078b586) | `easyeda-extension-development` | 领域工作流来源 | 2 |
| [eext-api-test-tool](https://github.com/easyeda/eext-api-test-tool/tree/317bd75e32f0248285fd9d4551e70ed046ef443f) | `easyeda-extension-development` | 领域工作流来源 | 2 |
| [eext-auto-copper-shape](https://github.com/easyeda/eext-auto-copper-shape/tree/98317b6b5941977a3ae90948a05295f9d8b1169f) | `easyeda-special-pcb` | 领域工作流来源 | 2 |
| [eext-balance-copper](https://github.com/easyeda/eext-balance-copper/tree/4a52f9021a9df487c9f3d2694f1aa67ef528d5ec) | `easyeda-special-pcb` | 领域工作流来源 | 2 |
| [eext-batch-data-export](https://github.com/easyeda/eext-batch-data-export/tree/16c0b33ca318abf162d21a287e5695ed1d8c1e73) | `easyeda-manufacturing-export`, `easyeda-project-backup` | 领域工作流来源 | 2 |
| [eext-batch-place-components](https://github.com/easyeda/eext-batch-place-components/tree/558e2530856cff42578900922ef66df4be3f7455) | `easyeda-pcb-layout` | 领域工作流来源 | 2 |
| [eext-board-outline-splitter](https://github.com/easyeda/eext-board-outline-splitter/tree/2f5c602391cf4b1702cd808bdeda7d1c9f8ee09c) | `easyeda-pcb-layout` | 领域工作流来源 | 2 |
| [eext-bom-compare](https://github.com/easyeda/eext-bom-compare/tree/4489dd9b857e19505a2f5a0dd383342bb77923d6) | `easyeda-bom-assembly` | 领域工作流来源 | 2 |
| [eext-chat-with-ai-kimi](https://github.com/easyeda/eext-chat-with-ai-kimi/tree/02cd68556e7a74eba645b485735d27959124128c) | `easyeda-api` | 领域工作流来源 | 2 |
| [eext-circuitjs1-simulator](https://github.com/easyeda/eext-circuitjs1-simulator/tree/220a62cc30a21a2c2121fb1037e9ba427e64e8d7) | `easyeda-simulation` | 领域工作流来源 | 2 |
| [eext-coil-creator](https://github.com/easyeda/eext-coil-creator/tree/3c897637a52d8f1cbc243e8587cbc5c90c5e35b1) | `easyeda-special-pcb` | 领域工作流来源 | 2 |
| [eext-color-silkscreen-generator](https://github.com/easyeda/eext-color-silkscreen-generator/tree/0d36c0495b9100a796337fd08041162a825b66b5) | `easyeda-silkscreen-art` | 领域工作流来源 | 2 |
| [eext-component-box](https://github.com/easyeda/eext-component-box/tree/0390a4c0e9dba6643ca2d18f8ff78328548efa70) | `easyeda-component-library`, `easyeda-bom-assembly` | 领域工作流来源 | 2 |
| [eext-datasheet-helper](https://github.com/easyeda/eext-datasheet-helper/tree/6be8cf0b8e28131e011ba11bf887dab4f027bed9) | `easyeda-datasheet-analysis` | 领域工作流来源 | 2 |
| [eext-delete-all-components](https://github.com/easyeda/eext-delete-all-components/tree/51f26554422918eb94617a86b1fa6a0de82b5ec8) | — | 破坏性演示；未形成独立用户工作流 | 2 |
| [eext-design-rule-generator](https://github.com/easyeda/eext-design-rule-generator/tree/2cf9635b335bf8c15cd046a1c2cf08f8b9118f88) | `easyeda-design-rules`, `easyeda-end-to-end` | 领域工作流来源 | 4 |
| [eext-device-attribute-editor](https://github.com/easyeda/eext-device-attribute-editor/tree/e1f10265743c17a34ba065bba46d4c1bcdc6b690) | `easyeda-component-library` | 领域工作流来源 | 2 |
| [eext-diff-pair-assistant](https://github.com/easyeda/eext-diff-pair-assistant/tree/99fc251f2a4a550d72609a54bd1d96dade84cf1f) | `easyeda-pcb-routing`, `easyeda-design-rules` | 领域工作流来源 | 2 |
| [eext-docs-generator](https://github.com/easyeda/eext-docs-generator/tree/8fa4e175f517f7d6b4c088f295651979db3c1ae6) | `easyeda-documentation` | 领域工作流来源 | 2 |
| [eext-dwg-importer](https://github.com/easyeda/eext-dwg-importer/tree/cdf3814c8b775d6e5ee19f4f9d8f027b74ec5825) | `easyeda-cad-integration` | 领域工作流来源 | 2 |
| [eext-dynamic-fill-region-for-silkscreen](https://github.com/easyeda/eext-dynamic-fill-region-for-silkscreen/tree/27f0f4227b4dcaa9d1d03e878cbb3710f2c54fe5) | `easyeda-silkscreen-art` | 领域工作流来源 | 2 |
| [eext-easyeda-api-agent](https://github.com/easyeda/eext-easyeda-api-agent/tree/c54a6f9a30717c327e2c9022aff2fbd9f9b8498e) | `easyeda-schematic-design` | 领域工作流来源 | 2 |
| [eext-excalidraw](https://github.com/easyeda/eext-excalidraw/tree/448db2cb66f497c26dd1597386759ea0325b6bc8) | `easyeda-silkscreen-art` | 领域工作流来源 | 2 |
| [eext-export-design-archive](https://github.com/easyeda/eext-export-design-archive/tree/9f1e7b5aa5f53c730ed801fa3bd7e56de44a5f0d) | `easyeda-project-backup` | 领域工作流来源 | 2 |
| [eext-export-design-report](https://github.com/easyeda/eext-export-design-report/tree/31a8cfec95bcae13e981b912c6bc86025062dca0) | `easyeda-documentation` | 领域工作流来源 | 2 |
| [eext-export-gencad](https://github.com/easyeda/eext-export-gencad/tree/aba4dff5b0fb8e1c5ad8288b07eb56b01dd0ab9e) | `easyeda-manufacturing-export` | 领域工作流来源 | 2 |
| [eext-export-hyperlynx](https://github.com/easyeda/eext-export-hyperlynx/tree/39acea28a1d3fb1628b48c08954723fecaa81f3b) | `easyeda-manufacturing-export` | 领域工作流来源 | 2 |
| [eext-export-pcb-to-svg](https://github.com/easyeda/eext-export-pcb-to-svg/tree/f68898d18c8279e2aaf84a5b2ff07969ebeb005e) | `easyeda-manufacturing-export` | 领域工作流来源 | 2 |
| [eext-extension-demo](https://github.com/easyeda/eext-extension-demo/tree/739c9a33aeb03a2715966c4ad5cf3af919b599ef) | `easyeda-extension-development` | 领域工作流来源 | 2 |
| [eext-external-tool-integration-demo](https://github.com/easyeda/eext-external-tool-integration-demo/tree/9b6e6f325a2d4210205f4904389871155a058f11) | `easyeda-extension-development` | 领域工作流来源 | 2 |
| [eext-fpc-workshop](https://github.com/easyeda/eext-fpc-workshop/tree/f8a245ab74a5405011bdd98b65b0b2af5f05cdca) | `easyeda-special-pcb` | 领域工作流来源 | 2 |
| [eext-freerouting-intergration](https://github.com/easyeda/eext-freerouting-intergration/tree/dab07252c22b408759693ee82845fd550243c3b5) | `easyeda-freerouting` | 领域工作流来源 | 4 |
| [eext-gencad-viewer](https://github.com/easyeda/eext-gencad-viewer/tree/b537e0cc0dfcf5be544e2d0589f457f719fb21a1) | `easyeda-manufacturing-export` | 领域工作流来源 | 2 |
| [eext-generate-schematic-from-netlist](https://github.com/easyeda/eext-generate-schematic-from-netlist/tree/35679a0f1e6b1ee2cca8fe0479fdd7def5e75f8d) | `easyeda-schematic-design`, `easyeda-netlist-import` | 领域工作流来源 | 3 |
| [eext-generate-silkscreen](https://github.com/easyeda/eext-generate-silkscreen/tree/f87bf3c725dea2dcb2b825a9faa90cb869dba86b) | `easyeda-silkscreen-art` | 领域工作流来源 | 2 |
| [eext-gerber-viewer](https://github.com/easyeda/eext-gerber-viewer/tree/085eb879b61ee84dfc7288852b490990282327e5) | `easyeda-manufacturing-export` | 领域工作流来源 | 2 |
| [eext-graffiti-silkscreen](https://github.com/easyeda/eext-graffiti-silkscreen/tree/8d969f1c6e0bb8b913abf9780a26c74961a58669) | `easyeda-silkscreen-art` | 领域工作流来源 | 2 |
| [eext-image-contour-to-pcb](https://github.com/easyeda/eext-image-contour-to-pcb/tree/3bbf294d2f2cfde51fb2f807fc45991f201fb0e7) | `easyeda-silkscreen-art` | 领域工作流来源 | 2 |
| [eext-interactive-bom](https://github.com/easyeda/eext-interactive-bom/tree/3606355f002a9380fe2f7b956b2969b09df65545) | `easyeda-bom-assembly` | 领域工作流来源 | 2 |
| [eext-interactive-html-bom](https://github.com/easyeda/eext-interactive-html-bom/tree/430ea9d06a1c975ed3d2c6da83a6686a1f737084) | `easyeda-bom-assembly` | 领域工作流来源 | 2 |
| [eext-jlc-order-dfm-checker](https://github.com/easyeda/eext-jlc-order-dfm-checker/tree/afd538786d510f537ad4fa47c6329e6a99dc7625) | `easyeda-drc-dfm`, `easyeda-end-to-end` | 领域工作流来源 | 2 |
| [eext-kipida-integration](https://github.com/easyeda/eext-kipida-integration/tree/af11ba17b6b1487efc1b87fc580a0ff6f97b1f81) | `easyeda-power-integrity` | 领域工作流来源 | 2 |
| [eext-kirouting-integration](https://github.com/easyeda/eext-kirouting-integration/tree/d682f9f99f018582450e216f75cd19672b09f031) | `easyeda-kirouting` | 领域工作流来源 | 2 |
| [eext-knowledge-base](https://github.com/easyeda/eext-knowledge-base/tree/5c666fe9ce711284f9a52dba24c3040ed7f57535) | `easyeda-knowledge-base` | 领域工作流来源 | 2 |
| [eext-mcad-integration-with-freecad](https://github.com/easyeda/eext-mcad-integration-with-freecad/tree/e3c30a527194d34def8ada4f84451de298caa048) | `easyeda-cad-integration` | 领域工作流来源 | 2 |
| [eext-mcad-integration-with-solidworks](https://github.com/easyeda/eext-mcad-integration-with-solidworks/tree/1368d185950b07492737eab27e542b631f3199f5) | `easyeda-cad-integration` | 领域工作流来源 | 2 |
| [eext-nc-pad-converter](https://github.com/easyeda/eext-nc-pad-converter/tree/acbc6436576fd18917a095e45e72aa41cb5d752b) | `easyeda-special-pcb` | 领域工作流来源 | 2 |
| [eext-netlist-explorer](https://github.com/easyeda/eext-netlist-explorer/tree/6661961fc8780e13b97a9450a96afbaaf2960bf7) | `easyeda-netlist-review` | 领域工作流来源 | 2 |
| [eext-note-tools](https://github.com/easyeda/eext-note-tools/tree/4627a6aa190cc4741e46a99745d9d3cf8e69af82) | `easyeda-documentation` | 领域工作流来源 | 2 |
| [eext-pad-expand-helper](https://github.com/easyeda/eext-pad-expand-helper/tree/de5b2eb6bd6817bb25025d621c2f6010bc110cab) | `easyeda-special-pcb` | 领域工作流来源 | 2 |
| [eext-pad-fanout](https://github.com/easyeda/eext-pad-fanout/tree/7c88e571457e6d63463b7cb391e1e62bdbdd02d7) | `easyeda-pcb-routing` | 领域工作流来源 | 2 |
| [eext-paden-integration](https://github.com/easyeda/eext-paden-integration/tree/0bb14f58712100eb5b84db5be7bd0c0ef318ea88) | `easyeda-power-integrity` | 领域工作流来源 | 2 |
| [eext-paden-integration-wasm](https://github.com/easyeda/eext-paden-integration-wasm/tree/92c75f057ede5b9c8e7a5db36ae79f8014f5a26b) | `easyeda-power-integrity` | 领域工作流来源 | 2 |
| [eext-pcb-component-grouping](https://github.com/easyeda/eext-pcb-component-grouping/tree/95421773a0180b9c0f48b4fe382419c673bafe2a) | `easyeda-pcb-layout` | 领域工作流来源 | 2 |
| [eext-pcb-heater-trace-generator](https://github.com/easyeda/eext-pcb-heater-trace-generator/tree/89cf798b176f1f13f0dde29c5024ae4408f3ad1c) | `easyeda-special-pcb` | 领域工作流来源 | 2 |
| [eext-pcb-price-calculator](https://github.com/easyeda/eext-pcb-price-calculator/tree/5527d29e2e13975652f00f3dc0df3dd5417c597a) | `easyeda-bom-assembly` | 领域工作流来源 | 2 |
| [eext-pcb-render-with-blender](https://github.com/easyeda/eext-pcb-render-with-blender/tree/6c8aef2be34d7733eb5e684f80af1059864013d1) | `easyeda-cad-integration` | 领域工作流来源 | 2 |
| [eext-plm-integration-demo](https://github.com/easyeda/eext-plm-integration-demo/tree/92463b09f41d048b2a96593a8a2b34693c872115) | `easyeda-project-backup`, `easyeda-documentation` | 领域工作流来源 | 2 |
| [eext-power-net-highlighter](https://github.com/easyeda/eext-power-net-highlighter/tree/ce520393451a1d148b3b354bb5161416fd5ec283) | `easyeda-netlist-review` | 领域工作流来源 | 1 |
| [eext-qrcode-generator](https://github.com/easyeda/eext-qrcode-generator/tree/29371cdc7aa472a36e56b428db02aab8ffa3bac3) | `easyeda-silkscreen-art` | 领域工作流来源 | 2 |
| [eext-run-api-gateway](https://github.com/easyeda/eext-run-api-gateway/tree/e55348027d1008a3d448b8b228fbca7b82dc8381) | — | 替代传输；原生 MCP 路线不依赖 | 2 |
| [eext-schematic-pdf-interaction](https://github.com/easyeda/eext-schematic-pdf-interaction/tree/03d3a6ec6c3d5ecbb6ad0ec55224f0d6ecb480ac) | `easyeda-netlist-review` | 领域工作流来源 | 2 |
| [eext-signal-absence-detection](https://github.com/easyeda/eext-signal-absence-detection/tree/78f8ca3437e34c2f7976860a8e61adc511e36dd9) | `easyeda-netlist-review`, `easyeda-drc-dfm` | 领域工作流来源 | 1 |
| [eext-simulation-with-ltspice](https://github.com/easyeda/eext-simulation-with-ltspice/tree/0fb2afa1816481b50846f55c1c6dbacd5912569b) | `easyeda-simulation` | 领域工作流来源 | 1 |
| [eext-simulation-with-ngspice](https://github.com/easyeda/eext-simulation-with-ngspice/tree/6536f1dac4c44b366777cdb18e344b1603be1ffc) | `easyeda-simulation` | 领域工作流来源 | 1 |
| [eext-simulation-with-simulide](https://github.com/easyeda/eext-simulation-with-simulide/tree/c8eb097e2e87abe80c2235bda2c2d2691fde509e) | `easyeda-simulation` | 领域工作流来源 | 2 |
| [eext-timing-analysis](https://github.com/easyeda/eext-timing-analysis/tree/f5e338b0c5d8f892c0e366067f7b0c60d4039180) | `easyeda-timing-analysis` | 领域工作流来源 | 2 |
| [eext-timing-diagram-tool](https://github.com/easyeda/eext-timing-diagram-tool/tree/596a50fb91d79ba0c99a02af22ad3c42d180b2b8) | `easyeda-timing-analysis` | 领域工作流来源 | 2 |
| [eext-update-components-attributes](https://github.com/easyeda/eext-update-components-attributes/tree/b26080edcc9e5e3dddadadda33d4e329973f2fc0) | `easyeda-component-library` | 领域工作流来源 | 2 |
| [extension-dev-mcp-tools](https://github.com/easyeda/extension-dev-mcp-tools/tree/edce042465fcccb6dc9cce8c17179de121bbb1a1) | `easyeda-extension-development` | 领域工作流来源 | 1 |
| [extension-dev-skill](https://github.com/easyeda/extension-dev-skill/tree/d9148cba524149d17afcbfd196fab3226a8df5da) | `easyeda-extension-development`, `easyeda-extension-use` | 领域工作流来源 | 3 |
| [jlc-mcli](https://github.com/easyeda/jlc-mcli/tree/7286a566efc96ff3f8cd461eedc503807508c8cf) | — | 基础框架参考；不复制 Runtime | 1 |
| [kicad-to-easyeda-eprj3](https://github.com/easyeda/kicad-to-easyeda-eprj3/tree/a16545dd7922455e6a20f69adeb234c924af08b5) | `easyeda-project-migration` | 领域工作流来源 | 1 |
| [mcad-integration-with-fusion360](https://github.com/easyeda/mcad-integration-with-fusion360/tree/50745428f53363e27628395751d211bfffdcaf15) | `easyeda-cad-integration` | 领域工作流来源 | 1 |
| [online-gencad-viewer](https://github.com/easyeda/online-gencad-viewer/tree/cdc76cdaa520765831bf7e3674e47cb213c975f8) | `easyeda-manufacturing-export` | 领域工作流来源 | 1 |

## 自研内部扩展适配

新增 easyeda-extension-use，来源为官方 extension-dev-skill 与 easyeda-client-cli 的注册、帮助和原生调用方式。33 个技能包括 5 个官方适配、28 个提炼技能。自研 .eext 的本机安装与只读结果独立记录在插件包 docs/eda-extension-validation.md，不代表 97 个上游插件均已执行。
