---
name: easyeda-component-library
description: "查询、匹配或维护 EasyEDA 器件、符号、封装与扩展属性，包括 AI 建库结果的复核。"
license: Apache-2.0
metadata:
  source-kind: extension-derived
---

# easyeda-component-library

查询、匹配或维护 EasyEDA 器件、符号、封装与扩展属性，包括 AI 建库结果的复核。

## 首次使用

读取 [原生 MCP 约定](references/native-mcp.md)，按真实工具返回执行 help、doctor、session.list。
不要把工程为空或扩展未安装解释为需要切换到 WebSocket Gateway。

## 当前任务

需要明确：型号、数据手册或供应商编号；目标个人库或团队库；参数与引脚要求。

1. 查询候选器件并核对型号、封装与来源。
2. 按数据手册建立引脚号、符号引脚和焊盘映射。
3. 批量属性修改限定目标器件与字段。
4. 生成符号或封装后检查几何、焊盘号与单位。
5. 在新图页试放或回读库对象验证。

## 验证结果

- 引脚号与封装焊盘一一对应。
- 属性修改不覆盖无关用户字段。
- 模型生成内容经数据手册复核。

## 容易出错的地方

- AI 建库不证明封装可生产。
- 库存信息与供应商实时库存不是同一数据。

## 使用示例

“按数据手册检查这个器件的符号和封装引脚映射。”

具体 API 入口、来源和执行范围见 [操作参考](references/operations.md)。

来源性质：从官方扩展与接口提炼的领域工作流。本技能的存在不代表上游扩展已安装或工作流已实测。
