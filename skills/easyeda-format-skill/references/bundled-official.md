# 包内官方完整资源

| 资源 | 包内位置 |
|---|---|
| 完整类型索引 | [types-index.md](../upstream/types-index.md) |
| 原版校验器 | `upstream/validate.js` |
| JSON Schema | `upstream/schemas/`，297 文件 |
| 图元字段说明 | `upstream/primitives/`，291 文件 |
| 真实记录样例 | `upstream/examples/`，302 文件 |
| 文档类型说明 | `upstream/documents/` |
| 原文件格式及 V2 文档 | `upstream/companions/easyeda-file-format/`、`upstream/companions/easyeda-file-format-v2/` |

```bash
python3 <当前技能绝对路径>/scripts/validate_format.py --install-deps --runtime-dir <可写缓存>
python3 <当前技能绝对路径>/scripts/validate_format.py --runtime-dir <可写缓存> -- DOCHEAD '<JSON>'
python3 <当前技能绝对路径>/scripts/validate_format.py --runtime-dir <可写缓存> -- --doc PCB LINE '<JSON>'
```

-- 后的参数原样传给官方 validate.js，保留有效返回 0、无效返回 1 的语义。仅显式 --install-deps 安装 package-lock 锁定的 ajv；使用 --ignore-scripts，依赖位于指定可写缓存或用户缓存，不污染不可变插件。无需 EDA 或 Bridge 即可做离线格式检查。生成后仍须通过内置 MCP 在客户端打开并验证实际网表、图元与 DRC。

这些是固定修订的完整原文快照。官方原文的旧路径和远程链接保持原样；执行和读取使用本页对应的包内位置。来源及逐文件 SHA-256 见发布包 official-assets.json。

官方原文若要求把结果写到技能目录或默认 format/，请改写到用户已授权的工作目录；技能安装资源保持不变。
