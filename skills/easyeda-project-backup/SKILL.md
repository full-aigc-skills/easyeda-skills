---
name: easyeda-project-backup
description: "备份、批量归档或导出 EasyEDA 工程与库，明确目录范围并验证可重新打开。"
license: Apache-2.0
metadata:
  source-kind: extension-derived
---

# easyeda-project-backup

备份、批量归档或导出 EasyEDA 工程与库，明确目录范围并验证可重新打开。

## 首次使用

读取 [原生 MCP 约定](references/native-mcp.md)，按真实工具返回执行 help、doctor、session.list。
不要把工程为空或扩展未安装解释为需要切换到 WebSocket Gateway。

## 当前任务

需要明确：指定工程或库；备份目录与格式；版本和是否允许保存当前修改。

1. 列明需要备份的具体工程与库，不默认全量。
2. 检查保存状态，遵循授权决定是否保存。
3. 使用原生导出或已安装归档扩展。
4. 检查文件数量、非空内容和压缩包条目。
5. 在可行时以独立会话重新打开备份，不覆盖源工程。

## 验证结果

- 备份包含预期工程和库。
- 目标文件可读取。
- 只读归档与写回 PLM 分别授权。

## 容易出错的地方

- PLM 演示不意味着已对接真实业务系统。
- 压缩包存在不代表库引用和工程完整。

## 使用示例

“备份指定工程及其库到新的归档目录。”

具体 API 入口、来源和执行范围见 [操作参考](references/operations.md)。

来源性质：从官方扩展与接口提炼的领域工作流。本技能的存在不代表上游扩展已安装或工作流已实测。
