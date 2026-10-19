# 包内官方完整资源

完整技能见 [upstream/SKILL.md](../upstream/SKILL.md)，全部 46 个配方在 `upstream/recipes/`，经验与开发指南在 `upstream/resources/`，4 个官方查询/测试脚本在 `upstream/scripts/`。

```bash
node <当前技能绝对路径>/upstream/scripts/eda-api.js doctor --project <目标扩展工程>
node <当前技能绝对路径>/upstream/scripts/eda-api.js inspect --project <目标扩展工程> --mount pcb_Document --member autoRouting --closure --format json
node --test <当前技能绝对路径>/upstream/scripts/eda-api.test.js
```

--project 必须指向实际目标扩展工程；TypeScript 和 @jlceda/pro-api-types 从该工程解析，不捆绑 node_modules，也不把缓存写到技能资源目录。生成的 .eext 安装和调试通过原生 MCP 与目标客户端完成，不启动 Bridge。

这些是固定修订的完整原文快照。官方原文的旧路径和远程链接保持原样；执行和读取使用本页对应的包内位置。来源及逐文件 SHA-256 见发布包 official-assets.json。

官方原文若要求把结果写到技能目录或默认 format/，请改写到用户已授权的工作目录；技能安装资源保持不变。
