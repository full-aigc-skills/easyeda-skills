# EasyEDA 技能包与插件设计

用户要求：独立 `easyeda-skills` 包；插件目录 `easyeda-plugin`，显示名称 **EasyEDA**；执行复用客户端内置 MCP；整合官方技能，并从官方扩展提炼可执行工作流。

## 所有权

- 本包维护领域知识、流程、API 查询与验收方法；不实现电路编辑引擎。
- 插件封装本包的自包含快照，维护宿主 manifest 和原生 MCP 地址。
- 客户端内置 MCP 执行真正操作；`Run API Gateway` 不是本包的依赖。
- 诊断脚本仅实现原生 HTTP 客户端、显式启动和只读查询，不启动第二套 Agent Runtime。
- 后续 `easyeda-mcp` 的高级领域工具单独确定交付边界；本版不把拟议接口当作已经存在。

## 工作流

```mermaid
flowchart LR
    A[用户需求] --> B[EasyEDA 技能选择]
    B --> C[原生 MCP help / doc.api]
    C --> D[原生 invoke 与扩展上层接口]
    D --> E[嘉立创 EDA 编辑器]
    E --> F[网表 / DRC / 产物回读]
    F --> B
```

## 连接与范围

默认连接 `http://127.0.0.1:31637/mcp`；可配置其他 loopback HTTP 地址。macOS 通过 LaunchServices 显式启动原生 MCP，避免直接子进程遇到文稿目录 EPERM 后停在原生错误对话框。不修改系统权限、不安装软件、不自动打开最近工程。

MCP 工具前缀由服务实际返回值发现；国内发行版实测为 `LCEDA-Pro`，不能固化成通用 `mcli`。工程为 null 时明确没有当前工程，多会话时要求选择。保留用户给定的只读范围，不以执行 Skill 自动扩大权限。

## 内容与来源

`catalog.json` 是工作流内容源；`scripts/render_skills.py` 渲染自包含 Skill。每个 Skill 单独携带操作参考和来源，不使用跨技能相对路径。官方技能保留原名称映射、固定 Git 修订与许可依据；正文按内置 MCP 路线重新编写，不复制 Bridge Server。

97 个官方组织仓库记录于 `docs/upstream-repositories.json`；映射会区分直接来源、补充参考与归档资料。来源存在不等于相应扩展已安装、可用或通过目标客户端验收。

## 验证

验证 manifest、技能引用、自包含快照一致性；用本地 HTTP fixture 验证原生客户端错误语义与只读行为；通过真实客户端执行 doctor、帮助查询、会话和当前工程读取。功能写入、制造导出和跨宿主安装分开报告，未运行项保留 NOT_RUN。

第一版只创建两个指定目录；不修改参考插件，不创建分支，不自动提交、推送或发布。

## 用户确认后的内部扩展

用户确认更强扩展为 EDA 内部 .eext，主源码位于 easyeda-mcp/extension。新增 easyeda-extension-use 描述安装后的发现、调用与只读边界；Agent 插件继续使用内置 MCP。前期外部 stdio 试作保留，不作为 .eext 交付证明。
