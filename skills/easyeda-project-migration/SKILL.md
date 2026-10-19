---
name: easyeda-project-migration
description: "将 KiCad 或旧版 EasyEDA 工程转换到目标专业版格式，核对器件、网络、层与几何的迁移损失。"
license: Apache-2.0
metadata:
  source-kind: extension-derived
---

# easyeda-project-migration

将 KiCad 或旧版 EasyEDA 工程转换到目标专业版格式，核对器件、网络、层与几何的迁移损失。

## 首次使用

读取 [原生 MCP 约定](references/native-mcp.md)，按真实工具返回执行 help、doctor、session.list。
不要把工程为空或扩展未安装解释为需要切换到 WebSocket Gateway。

## 当前任务

需要明确：源工程与目标版本；新目录；允许的格式损失。

1. 识别真实源格式和对应转换器。
2. 保留源工程，在新位置转换。
3. 比较器件、封装、网络、层、板框和规则。
4. 在目标客户端打开并运行相关检查。
5. 报告不支持项和人工修复范围。

## 验证结果

- 源工程受到保护。
- 关键对象与连接数量可比较。
- 目标客户端可继续编辑。

## 容易出错的地方

- 格式可解析不等于行为和规则等价。
- 不能用 .eprj3 操作脚本处理旧 SQLite .eprj2。

## 使用示例

“将这份 KiCad 工程转换为新的嘉立创工程并报告损失。”

具体 API 入口、来源和执行范围见 [操作参考](references/operations.md)。

来源性质：从官方扩展与接口提炼的领域工作流。本技能的存在不代表上游扩展已安装或工作流已实测。
