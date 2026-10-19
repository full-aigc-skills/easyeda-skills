# 官方完整技能资源验收

日期：2026-10-19；版本：0.1.0-dev.20261019.6。

## 资源与来源

5 个官方技能完整跟踪文件与配套格式依赖已随包携带：9 份固定快照、2,769 文件。API 参考 422 文件；格式技能有 297 个独立 Schema、291 份图元说明、302 份样例；扩展开发包含 46 个 recipes。eprj3 内独立携带完整格式依赖，因此物理 Schema 副本为 594 个。

上游原文保持字节不变，逐文件 SHA-256 见 official-assets.json。旧 Bridge 脚本仅作完整来源参考，默认配置、中文入口及实际客户端调用继续使用内置 MCP；未启动 Bridge，也未安装其 ws 依赖。

## 已执行验证

| 层次 | 实际结果 |
|---|---|
| 源包回归 | 12 项通过，包括缺失/篡改、符号链接、污染、打包、缺省字段适配与真实 Schema 正反例 |
| 插件回归 | 5 项通过，包括快照漂移保护、打包和已安装格式工具正反例 |
| 原版 eprj3 smoke | 121/121 检查通过 |
| 原版 SDK 查询测试 | 2/2 测试通过，使用测试要求的 pro-api-types 0.2.58；未把 skip 算为通过 |
| Schema | 297 个全部经 Ajv 编译；正确 DOCHEAD 返回 0/valid=true，非法 docType/client 返回 1/valid=false |
| 实际安装 | codex plugin add 安装 .6；新的 app-server 读取 installed=true/enabled=true，并发现 33 个 easyeda:* 技能 |
| 安装快照 | 2,925 个快照文件全部匹配源包摘要；校验器从安装目录执行 |
| 当前 SDK 查询 | 安装目录的 eda-api.js 对真实扩展工程查询 doctor/autoRouting 类型闭包；pro-api-types 0.4.26、TypeScript 5.9.3 |
| 原版脚本生成工程 | 从安装目录运行 10 个生成/验证命令，创建独立 Official-Assets-Acceptance 工程；未改用户原工程 |
| 客户端原生 MCP | 激活新工程图页后，插件领域接口读到原理图 4 对象（实际 R1 一个、旗标两个、图框一个）、2 组导线及完整网表；PCB R1 一个，焊盘网为 VCC/GND，writeEnabled=false |

生成工程及详细调用结果保留在开发机忽略目录 .local/host-acceptance/，依赖缓存、临时工程和 node_modules 不提交或打包。公开源码与 ZIP 另外进行干净解包校验。

## 实测发现与处理

- 原版格式审计器硬编码 `<格式目录>/node_modules/ajv`。audit_format.py 在可写临时目录暂存格式资料并链接依赖；原版脚本和 Schema 不修改，退出码原样返回。
- 固定版本的原版审计仍返回 1：SCH COMPONENT 缺少 groupId/locked。此结果保留为上游兼容性问题，未记为成功。
- 对新生成工程显式运行 normalize_component_defaults.py，仅补缺失字段，保留已有值、UUID、ticket、网络与库关联。4 个实际记录补齐后，对应官方 Schema 全部通过，工程结构为 0 错误/0 警告。原版测试生成器的源码未改写。
- 本机 npm 拒绝锁文件中的跨 registry tarball 地址。依赖安装适配仅在可写缓存里将 npmmirror URL 映射到 npm 官方 registry，版本与 integrity 不变，不放宽 npm 安全配置。
- 冷启动的 openDocument/getCurrentProjectInfo 在当前客户端有超时或未激活现象；本次用客户端界面激活独立文档后再执行原生 MCP 读取，未声称全程无界面。

本次验收证明资源完整、离线工具可达、Codex 安装生效，以及原生 MCP 可读取独立生成工程。未重新执行全套制造验收，也不代表仿真、外部布线器及 97 个上游插件全部运行通过。
