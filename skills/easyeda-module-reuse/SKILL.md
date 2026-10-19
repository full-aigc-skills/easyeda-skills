---
name: easyeda-module-reuse
description: "检索 EasyEDA 个人、团队或本地复用模块，并放置、检查模块之间的接口连接。"
license: Apache-2.0
metadata:
  source-kind: extension-derived
---

# easyeda-module-reuse

检索 EasyEDA 个人、团队或本地复用模块，并放置、检查模块之间的接口连接。

## 首次使用

读取 [原生 MCP 约定](references/native-mcp.md)，按真实工具返回执行 help、doctor、session.list。
不要把工程为空或扩展未安装解释为需要切换到 WebSocket Gateway。

## 当前任务

需要明确：模块功能与参数；目标图页、板子或工程；已有模块目录。

1. 从实际目录搜索或推荐模块，不编造 cbbUuid。
2. 读取模块器件、接口和存储来源。
3. 确认当前图页、目标放置形式及范围。
4. 执行模块放置并记录实际落点与新增对象。
5. 核对模块间电源、网络命名和接口参数。

## 验证结果

- 模块实际存在于所选库。
- 新增对象和图页属于目标工程。
- 连接按实际网表复核。

## 容易出错的地方

- 工程库内嵌副本不一定能作为可放置源。
- 模块放置不等于模块间已连接。

## 使用示例

“复用已有 USB 供电模块，接到当前 MCU 板。”

具体 API 入口、来源和执行范围见 [操作参考](references/operations.md)。

来源性质：从官方扩展与接口提炼的领域工作流。本技能的存在不代表上游扩展已安装或工作流已实测。
