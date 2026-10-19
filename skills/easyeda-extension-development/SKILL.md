---
name: easyeda-extension-development
description: "开发或调试嘉立创 EDA .eext 扩展，查询目标 SDK 类型、注册菜单或上层接口并打包。"
license: Apache-2.0
metadata:
  source-kind: official-adapted
---

# easyeda-extension-development

开发或调试嘉立创 EDA .eext 扩展，查询目标 SDK 类型、注册菜单或上层接口并打包。

## 首次使用

读取 [原生 MCP 约定](references/native-mcp.md)，按真实工具返回执行 help、doctor、session.list。
不要把工程为空或扩展未安装解释为需要切换到 WebSocket Gateway。

## 当前任务

需要明确：目标 SDK 项目；扩展功能与适用编辑器；目标客户端版本。

1. 读取目标项目的 @jlceda/pro-api-types 版本和类型声明。
2. 按需查询 eda mount、方法、重载及枚举，Markdown 示例仅供流程参考。
3. 配置 extension.json 菜单、UUID、入口与权限。
4. 需要供外部 Agent 调用时用 SYS_ExternalApi 注册有帮助信息的上层接口。
5. 构建 .eext 后在目标客户端导入并调用具体功能。

## 验证结果

- 编译使用的是目标项目 SDK。
- 外部工具能发现真实注册接口。
- 导入无日志错误不等于功能验收通过。

## 容易出错的地方

- 浏览器沙箱不能直接当 Node.js 使用。
- 插件包与 EDA 内部 .eext 是不同交付物。

## 使用示例

“创建一个只读列出当前 PCB 元件的 .eext 扩展。”

具体 API 入口、来源和执行范围见 [操作参考](references/operations.md)。

来源性质：官方技能整合，已将传输改为内置 MCP。本技能的存在不代表上游扩展已安装或工作流已实测。
上游技能名：`extension-dev-skill`；这里为中文整理与原生 MCP 适配版本。

## 已随包携带的官方完整资源

先读 [包内资源与内置 MCP 适配](references/bundled-official.md)，再按任务读取 [完整官方原文](upstream/SKILL.md)。原文、脚本、Schema、样例和配套资料已随本技能携带。
官方原文中的 WebSocket Bridge、旧安装路径或 companion 旧仓库名仅作来源记录；实时编辑始终使用上述原生 MCP，离线工具使用本技能内的实际路径。不要启动 upstream/scripts/bridge-server.mjs。
