# Proposal

## Why

现有技能仅提供官方工作流摘要，缺少原版脚本、Schema 和参考资料，安装后无法独立完成格式校验与 SDK 查询。用户要求完整补齐并保持客户端内置 MCP。

## What Changes

- 固定官方五个技能及格式依赖的修订，随技能携带完整已跟踪资源、来源和校验摘要。
- 中文入口指向包内原文、脚本、Schema 与参考资料；运行 EDA 继续使用原生 MCP，不启动旧 Bridge。
- 补充可实际执行的格式验证依赖安装入口，依赖缓存与不可变插件资源分离。
- 同步源技能、插件快照与版本；Codex 安装后进行脚本、格式和原生 MCP 验证。

## Capabilities

### New Capabilities

- `official-assets`: 可追溯、自包含的官方技能资源和内置 MCP 执行约定。

### Modified Capabilities

无。

## Impact

影响 easyeda-skills 的资源管理、入口生成和验证，以及 easyeda-plugin 的快照、打包与安装。无需修改 EDA 内部扩展或用户原工程。

针对实际发现的生成器字段缺省与审计依赖路径问题，新增独立适配脚本；不修改官方快照，不降低 Schema 约束。默认预览、仅显式应用到独立工程，审计器原始失败仍如实报告。
