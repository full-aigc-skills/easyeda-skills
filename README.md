# EasyEDA Skills

面向嘉立创 EDA / EasyEDA **专业版**的 33 个中文 Agent Skills，执行使用客户端内置 MCP。包含 5 个官方技能的中文整理与传输适配，以及 28 个从官方扩展和接口提炼的工作流。当前版本 `0.1.0-dev.20261019.6`，GitHub 开发候选，尚未创建正式 Release。

该包独立维护知识；`easyeda-plugin` 通过可校验的文件快照携带这些技能。每个技能都有自己的 references，无需依赖兄弟目录。不是嘉立创官方发行包。

## 首次使用

在支持本地 Skill 的 Agent 宿主中加载 `skills/easyeda-use/SKILL.md`，说“只读检查当前工程，先报告连接状态和工程名称”。宿主必须实际提供原生 MCP，单独加载 Markdown 不会自动新增工具。

客户端专业版需支持内置 MCP（官方说明要求 4.1.60+）。默认地址 `http://127.0.0.1:31637/mcp`。本机实测原生工具名为 `LCEDA-Pro.help`、`LCEDA-Pro.discover`、`LCEDA-Pro.call`，以服务发现结果为准。

```bash
python3 -B skills/easyeda-mcp-setup/scripts/native_mcp.py doctor
python3 -B skills/easyeda-mcp-setup/scripts/native_mcp.py sessions
python3 -B skills/easyeda-mcp-setup/scripts/native_mcp.py current-project
```

这些命令相对于本包根目录。多会话需要 `--session 实际ID`。只有用户要求启动客户端时才运行 `.../native_mcp.py start`，macOS 使用 LaunchServices，避免直接二进制子进程遇到文稿目录权限错误。本包不安装客户端、不修改系统权限。

可从 [full-aigc-skills/easyeda-skills](https://github.com/full-aigc-skills/easyeda-skills) 按名称安装：`npx skills add full-aigc-skills/easyeda-skills --skill easyeda-use`。默认从 main 分支安装；尚未创建版本标签。

## 技能目录

| 技能 | 用途 | 来源 |
|---|---|---|
| `easyeda-use` | 使用嘉立创 EDA / EasyEDA 完成设计、检查或导出时选择对应技能；执行入口为客户端内置 MCP。 | 扩展/接口提炼 |
| `easyeda-extension-use` | 读取 EDA 内部扩展能力、工程、器件、引脚与网表，按授权调用设计和导出接口。 | 扩展/接口提炼 |
| `easyeda-mcp-setup` | 连接或排查嘉立创 EDA 内置 MCP，诊断 macOS 启动 EPERM、会话为空和原生工具发现问题。 | 扩展/接口提炼 |
| `easyeda-api` | 查询并使用 EasyEDA 专业版 eda.* API，读取对象与引脚、执行原生 invoke，替代官方 Skill 的独立 Bridge 传输。 | 官方技能适配 |
| `easyeda-schematic-design` | 将明确的电路需求转成器件、引脚连接与可编辑原理图；适用于 MCU 最小系统、电源和传感器接口设计。 | 扩展/接口提炼 |
| `easyeda-schematic-net-fanout` | 按实际引脚方向排列原理图元件、生成电源标识符和信号端口，或修改已有引脚扇出。 | 官方技能适配 |
| `easyeda-netlist-import` | 把已知 EasyEDA 网表重建为原理图，并处理器件查找、引脚映射和部分导入失败。 | 扩展/接口提炼 |
| `easyeda-netlist-review` | 分析原理图网表、器件连接关系、电源网络和悬空引脚；默认只读检查。 | 扩展/接口提炼 |
| `easyeda-component-library` | 查询、匹配或维护 EasyEDA 器件、符号、封装与扩展属性，包括 AI 建库结果的复核。 | 扩展/接口提炼 |
| `easyeda-module-reuse` | 检索 EasyEDA 个人、团队或本地复用模块，并放置、检查模块之间的接口连接。 | 扩展/接口提炼 |
| `easyeda-eprj3` | 创建、检查或编辑 EasyEDA 文件夹式 .eprj3 工程，优先通过内置 MCP 操作，直接写格式时核对完整格式依赖。 | 官方技能适配 |
| `easyeda-format-skill` | 读取或生成 EasyEDA 专业版原理图、PCB、符号、封装的底层记录，处理 DOCHEAD、ticket、Schema 和文档类型差异。 | 官方技能适配 |
| `easyeda-extension-development` | 开发或调试嘉立创 EDA .eext 扩展，查询目标 SDK 类型、注册菜单或上层接口并打包。 | 官方技能适配 |
| `easyeda-pcb-layout` | 把原理图同步到 PCB，设置板框、固定位置和禁布区，并按功能块布局或检查自动布局结果。 | 扩展/接口提炼 |
| `easyeda-pcb-routing` | 使用 EasyEDA 内置 autoRouting 布线，设置网络、启用层与规则并验证失败网络和实际连通性。 | 扩展/接口提炼 |
| `easyeda-freerouting` | 将 EasyEDA PCB 导出 DSN，调用已有 Freerouting 服务并导入 SES；适用于内置布线之外的备选路径。 | 扩展/接口提炼 |
| `easyeda-kirouting` | 评估或调用已有 KiRouting 桥接，对 EasyEDA PCB 执行外部布线并验证坐标、层和规则转换。 | 扩展/接口提炼 |
| `easyeda-design-rules` | 按明确板厂工艺、叠层和网络要求生成或修改 EasyEDA PCB 线宽、间距、网络类和差分规则。 | 扩展/接口提炼 |
| `easyeda-drc-dfm` | 检查原理图、PCB DRC 与嘉立创制造约束，区分完整通过、部分检查和执行失败。 | 扩展/接口提炼 |
| `easyeda-simulation` | 对 EasyEDA 原理图使用已有 NGspice、LTspice、SimulIDE 或 CircuitJS 集成做明确目标的电路仿真。 | 扩展/接口提炼 |
| `easyeda-power-integrity` | 通过已有 PADEN 或 KiPIDA 扩展评估 PCB 电源分配网络或直流压降，并核对提取模型。 | 扩展/接口提炼 |
| `easyeda-timing-analysis` | 分析 PCB 信号路径延迟、Setup/Hold 和时序余量，或在原理图中生成 WaveDrom 时序说明。 | 扩展/接口提炼 |
| `easyeda-silkscreen-art` | 制作 EasyEDA 文字、二维码、图片轮廓、涂鸦或彩色丝印，保持制造层与实际导电图形分离。 | 扩展/接口提炼 |
| `easyeda-special-pcb` | 生成 NFC/无线充电线圈、电热膜蛇形线路或 FPC 特殊结构，并核对电气目标和工艺限制。 | 扩展/接口提炼 |
| `easyeda-manufacturing-export` | 从已核对的 EasyEDA PCB 导出 Gerber、钻孔、BOM、贴片坐标或 STEP，并检查制造包完整性。 | 扩展/接口提炼 |
| `easyeda-bom-assembly` | 比较或导出 EasyEDA BOM，使用交互式 BOM 核对装配位号、封装和贴片坐标。 | 扩展/接口提炼 |
| `easyeda-cad-integration` | 将 EasyEDA PCB 与 FreeCAD、SolidWorks、Fusion 360 对接，导入 DWG 或使用 Blender 渲染板卡。 | 扩展/接口提炼 |
| `easyeda-project-migration` | 将 KiCad 或旧版 EasyEDA 工程转换到目标专业版格式，核对器件、网络、层与几何的迁移损失。 | 扩展/接口提炼 |
| `easyeda-project-backup` | 备份、批量归档或导出 EasyEDA 工程与库，明确目录范围并验证可重新打开。 | 扩展/接口提炼 |
| `easyeda-end-to-end` | 协调 EasyEDA 原理图设计、PCB 布局布线、DRC/DFM 和制造导出的完整流程，逐阶段验证实际产物。 | 扩展/接口提炼 |
| `easyeda-datasheet-analysis` | 从器件数据手册提取引脚、电源、封装尺寸和参考电路，供 EasyEDA 选型、建库或设计验证。 | 扩展/接口提炼 |
| `easyeda-knowledge-base` | 在已有 EasyEDA 本地 RAG 知识库中检索设计资料，检查引用来源与更新范围。 | 扩展/接口提炼 |
| `easyeda-documentation` | 根据实际 EasyEDA 工程生成设计说明、统计报告、Markdown/LaTeX 注释或 PLM 对接资料。 | 扩展/接口提炼 |

## 官方整合方法

官方 API、原理图扇出、eprj3、格式和扩展开发技能的完整原文与全部跟踪文件已分别随对应技能携带于 `upstream/`。共 9 份固定来源快照、2,769 个文件；格式技能有 297 个 Schema、291 份图元说明、302 份样例，eprj3 技能内再携带独立格式依赖，按单技能安装也完整。

- [逐文件来源与 SHA-256](official-assets.json)：包含原始仓库、固定修订、相对路径和许可依据。
- API 参考共 422 文件，`.eprj3` 脚本/模板/样例、格式校验器及扩展开发 46 个 recipes 全部在包内。
- 实时编辑继续只用客户端内置 MCP；原版 Bridge 脚本仅为来源快照，不启动、不配置第二个服务。
- 原版工具不附带 node_modules。格式校验通过技能内 `scripts/validate_format.py` 显式把锁定依赖安装到可写缓存；保留版本及 integrity，只将镜像下载 URL 映射到 npm 官方 registry。
- 中文入口和 `references/bundled-official.md` 指向包内实际资源。上游原文保持原始字节，旧安装路径/仓库名按适配说明映射；不声称每个上游历史链接都仍有效。

[仓库覆盖表](docs/source-analysis.md) 列出全部 97 个组织仓库、对应技能及未纳入执行的原因。[source-lock.json](source-lock.json) 记录固定 commit、实际读取文件与 SHA-256；这代表所列文件的静态检查，不代表 97 个仓库的全部源码或真实运行均已审计。

## 维护

```bash
python3 -B scripts/render_skills.py --check
python3 -B scripts/validate_package.py
python3 -B -m unittest discover -s tests -v
```

修改 `catalog.json` 后执行 `python3 -B scripts/render_skills.py`。官方五项适配细则单独维护，不被渲染器覆盖。更新固定 checkout 后运行 `python3 -B scripts/vendor_official.py --source-root .local/official-sources`，再用 `--check` 比对全部原始文件。`scripts/refresh_upstream.py` 是显式联网刷新，需要现有 `gh` 和访问权限；它不执行上游脚本。刷新后先审查修订差异，再重新生成技能和插件快照。

## 已验证与限制

包校验覆盖 33 个技能及完整官方资源，缺失、篡改、符号链接和依赖污染均会失败。官方脚本、格式正反例、SDK 查询、Codex 安装和内置 MCP 实测结果见 [官方资源验收](docs/official-assets-validation.md)。

此前独立 LED 测试已完成原理图创建到制造导出；官方快速入门 Demo 完成原理图源码重放、PCB 重布及修复、严格 DRC 0 和保存重开。缓存 UUID 的逐器件放置超时，不能称为该示例从空白逐器件设计成功。其他官方示例、仿真、外部布线器等没有因资源补齐而自动获得运行验收。

许可与来源见 [NOTICE](NOTICE)。不提供自动下单与付款流程。

本地 ZIP：`python3 -B scripts/build_package.py`；产物位于 dist，不包含来源采集缓存。

新增 `easyeda-extension-use`：使用内部 .eext 的 14 个领域接口，包括 doc.external 的实测兼容查询路线，以及工程信息 API 超时的只读降级说明。

本机独立 LED 电路已实际验证原理图设计、PCB 同步与自动布线、保存重开及 Gerber/BOM/坐标输出；仅覆盖该测试电路，不代表全部来源插件已执行。调用时需核对真实 extUuid 和复制后变化的工程 UUID，详见 easyeda-extension-use 技能。
