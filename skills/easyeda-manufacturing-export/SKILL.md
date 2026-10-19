---
name: easyeda-manufacturing-export
description: "从已核对的 EasyEDA PCB 导出 Gerber、钻孔、BOM、贴片坐标或 STEP，并检查制造包完整性。"
license: Apache-2.0
metadata:
  source-kind: extension-derived
---

# easyeda-manufacturing-export

从已核对的 EasyEDA PCB 导出 Gerber、钻孔、BOM、贴片坐标或 STEP，并检查制造包完整性。

## 首次使用

读取 [原生 MCP 约定](references/native-mcp.md)，按真实工具返回执行 help、doctor、session.list。
不要把工程为空或扩展未安装解释为需要切换到 WebSocket Gateway。

## 当前任务

需要明确：目标 PCB 和输出目录；制板或贴片所需格式；单位、层及钻孔选项。

1. 确认目标板及当前保存状态，不静默保存未授权修改。
2. 查询 getGerberFile、getBomFile、getPickAndPlaceFile 等当前签名。
3. 分别生成请求的文件，拒绝 undefined 或空结果。
4. 写入授权输出位置并检查实际文件与压缩包。
5. 预览层、钻孔、板框和坐标，报告遗漏。

## 验证结果

- 铜层、板框和钻孔完整。
- BOM 位号与贴片坐标一致。
- 文件可以重新读取和预览。

## 容易出错的地方

- JSON-RPC 成功不代表 File 对象有效。
- 自定义 objects/layers 可能误删必要制造数据。

## 使用示例

“导出当前板的 Gerber、钻孔、BOM 和贴片坐标到新目录。”

具体 API 入口、来源和执行范围见 [操作参考](references/operations.md)。

来源性质：从官方扩展与接口提炼的领域工作流。本技能的存在不代表上游扩展已安装或工作流已实测。
