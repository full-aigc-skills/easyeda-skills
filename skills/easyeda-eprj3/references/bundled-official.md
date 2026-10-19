# 包内官方完整资源

| 资源 | 包内位置 |
|---|---|
| 全部工具脚本 | `upstream/scripts/`（包括 init、建库、连接、布线和验证工具） |
| 模板、工程样例、测试 | `upstream/templates/`、`upstream/examples/`、`upstream/test/` |
| 必需配套格式技能 | [完整格式技能](../upstream/companions/easyeda-format-skill/SKILL.md) |
| 配套 Schema、图元及样例 | `upstream/companions/easyeda-format-skill/{schemas,primitives,examples}/` |
| 官方工程真值样例 | [格式工程介绍](../upstream/companions/easyeda-eprj3-format/README.md) |
| 依赖隔离的官方格式校验入口 | `scripts/validate_format.py` |

原版提到的 easyeda-pro-format-skill 旧名称在此映射到包内 companions/easyeda-format-skill，无需 sibling 技能。必须先读取上述完整配套格式再离线生成，不凭摘要猜字段。

```bash
node <当前技能绝对路径>/upstream/scripts/init.js --dir <授权的新工程目录> --name <名称>
node <当前技能绝对路径>/upstream/scripts/validate.js --help
python3 <当前技能绝对路径>/scripts/validate_format.py --install-deps --runtime-dir <可写缓存>
python3 <当前技能绝对路径>/scripts/validate_format.py --runtime-dir <可写缓存> -- DOCHEAD '<JSON>'
```

init、cleanup 等会写工程，仅操作已授权目录。依赖安装需授权，node_modules 不写入技能安装目录。客户端打开仍使用内置 MCP open；不调用上游 open.js 的文件关联安装或全局配置修改。离线脚本的通过不代表客户端、电气或制造验收。

这些是固定修订的完整原文快照。官方原文的旧路径和远程链接保持原样；执行和读取使用本页对应的包内位置。来源及逐文件 SHA-256 见发布包 official-assets.json。

## 原版脚本兼容性

- 原版 audit-format.js 硬编码 `<格式目录>/node_modules/ajv`，不能直接对只读安装目录使用。运行 `python3 <当前技能>/scripts/audit_format.py --runtime-dir <依赖缓存>`：临时复制格式资料并链接缓存，原版脚本与 Schema 不变；退出码原样保留。
- 固定版本的原版审计会报告 SCH COMPONENT 缺少 groupId/locked。不要把审计结果改为成功。对已授权的生成工程，可先运行 `python3 <当前技能>/scripts/normalize_component_defaults.py --project <新工程>` 预览，再加 `--apply` 仅补缺失字段；已有字段、ID、ticket、网络与库关联保持不变。补齐后重新运行官方结构校验与相关 Schema 校验，并在客户端读取验证。

官方原文若要求把结果写到技能目录或默认 format/，请改写到用户已授权的工作目录；技能安装资源保持不变。
