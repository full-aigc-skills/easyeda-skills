# EasyEDA 技能包协作规范

- catalog.json 为本包领域知识源；修改后运行 scripts/render_skills.py。
- 只使用内置 MCP；未知 API 通过目标客户端 doc.api/doc.external 查询。
- Skill 自包含，跨技能用名称与发布后的安装命令，不使用 ../sibling 链接。
- source-lock.json 记录固定来源；官方适配与原创提炼分开标识。
- skills/easyeda-mcp-setup/scripts/native_mcp.py 只做诊断、显式启动和只读查询，不成为第二套执行引擎。
- 无工程、多会话、部分导入、未检查 DRC、制造文件缺失均不能宣称成功。
