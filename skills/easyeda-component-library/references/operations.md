# 操作参考

## 第一个工具调用

调用 tools/list 实际返回的原生 `.help`，参数 `{}`，再查询 `doc.api` 帮助。
本工作流首先查询以下类，具体方法、参数、返回以当前客户端帮助为准：

```json
{"path": "doc.api", "input": {"className": "LIB_Device"}}
```

```json
{"path": "doc.api", "input": {"className": "LIB_Symbol"}}
```

```json
{"path": "doc.api", "input": {"className": "LIB_Footprint"}}
```

之后在选定会话中通过原生 `invoke` 执行已查询的 API。涉及扩展时先查询 `doc.external` 或 `functions`，确认上层接口实际存在；未暴露时报告缺口，不把源代码函数名直接当成工具。

## 完成判据

- 引脚号与封装焊盘一一对应。
- 属性修改不覆盖无关用户字段。
- 模型生成内容经数据手册复核。

## 官方来源

- [eext-ai-library-builder](https://github.com/easyeda/eext-ai-library-builder/tree/27731deb50a3ca855874d5b70c32c5e2dc6888e0)，修订 `27731deb50a3ca855874d5b70c32c5e2dc6888e0`。
  - [src/index.ts](https://github.com/easyeda/eext-ai-library-builder/blob/27731deb50a3ca855874d5b70c32c5e2dc6888e0/src/index.ts)
- [eext-ai-symbol-builder](https://github.com/easyeda/eext-ai-symbol-builder/tree/e9fb3b167356c85077307712f09e3133bd632585)，修订 `e9fb3b167356c85077307712f09e3133bd632585`。
  - [src/index.ts](https://github.com/easyeda/eext-ai-symbol-builder/blob/e9fb3b167356c85077307712f09e3133bd632585/src/index.ts)
- [eext-ai-device-standardization](https://github.com/easyeda/eext-ai-device-standardization/tree/89abac48075bd4e0ebc2a30bee55939251f8660f)，修订 `89abac48075bd4e0ebc2a30bee55939251f8660f`。
  - [src/index.ts](https://github.com/easyeda/eext-ai-device-standardization/blob/89abac48075bd4e0ebc2a30bee55939251f8660f/src/index.ts)
- [eext-device-attribute-editor](https://github.com/easyeda/eext-device-attribute-editor/tree/e1f10265743c17a34ba065bba46d4c1bcdc6b690)，修订 `e1f10265743c17a34ba065bba46d4c1bcdc6b690`。
  - [src/index.ts](https://github.com/easyeda/eext-device-attribute-editor/blob/e1f10265743c17a34ba065bba46d4c1bcdc6b690/src/index.ts)
- [eext-update-components-attributes](https://github.com/easyeda/eext-update-components-attributes/tree/b26080edcc9e5e3dddadadda33d4e329973f2fc0)，修订 `b26080edcc9e5e3dddadadda33d4e329973f2fc0`。
  - [src/index.ts](https://github.com/easyeda/eext-update-components-attributes/blob/b26080edcc9e5e3dddadadda33d4e329973f2fc0/src/index.ts)
- [eext-component-box](https://github.com/easyeda/eext-component-box/tree/0390a4c0e9dba6643ca2d18f8ff78328548efa70)，修订 `0390a4c0e9dba6643ca2d18f8ff78328548efa70`。
  - [src/index.ts](https://github.com/easyeda/eext-component-box/blob/0390a4c0e9dba6643ca2d18f8ff78328548efa70/src/index.ts)

这些链接是固定版本的知识来源，不会自动安装、运行上游扩展。文档/源码证据与真实客户端、板卡、制造验证分开记录。
