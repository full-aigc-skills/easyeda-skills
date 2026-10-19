# 包内官方完整资源

| 资源 | 包内位置 |
|---|---|
| 完整 API 索引 | [references/_index.md](../upstream/references/_index.md) |
| 全部参考文档 | `upstream/references/`（422 文件） |
| 文档源格式 | [format/index.md](../upstream/format/index.md) |
| 开发指南 | `upstream/guide/`、`upstream/user-guide/` |
| 原版代码 | `upstream/scripts/bridge-server.mjs`，仅归档参考，不启动 |

本包保留原版 package.json/package-lock.json 作为溯源；其 npm server 命令属于旧 Bridge，不属于本插件执行入口。原版 API 示例中的 eda.* 代码通过原生 invoke 执行，不向旧 HTTP /execute 发送。查询目标客户端真实签名后使用，不把旧静态参考版本等同于当前 SDK。

这些是固定修订的完整原文快照。官方原文的旧路径和远程链接保持原样；执行和读取使用本页对应的包内位置。来源及逐文件 SHA-256 见发布包 official-assets.json。

官方原文若要求把结果写到技能目录或默认 format/，请改写到用户已授权的工作目录；技能安装资源保持不变。
