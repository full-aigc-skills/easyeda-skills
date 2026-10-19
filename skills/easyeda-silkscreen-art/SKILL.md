---
name: easyeda-silkscreen-art
description: "制作 EasyEDA 文字、二维码、图片轮廓、涂鸦或彩色丝印，保持制造层与实际导电图形分离。"
license: Apache-2.0
metadata:
  source-kind: extension-derived
---

# easyeda-silkscreen-art

制作 EasyEDA 文字、二维码、图片轮廓、涂鸦或彩色丝印，保持制造层与实际导电图形分离。

## 首次使用

读取 [原生 MCP 约定](references/native-mcp.md)，按真实工具返回执行 help、doctor、session.list。
不要把工程为空或扩展未安装解释为需要切换到 WebSocket Gateway。

## 当前任务

需要明确：图像、文字或二维码内容；目标层与物理尺寸；板厂工艺要求。

1. 确认目标是丝印、板框还是导电铜图形。
2. 选择已有扩展或原生图元 API。
3. 按尺寸转换轮廓或文字并限制目标层。
4. 检查焊盘避让、最小线宽、裁切和可读性。
5. 保存并检查实际导出制造图层。

## 验证结果

- 丝印未意外进入铜层。
- 二维码或文字在目标尺寸可辨识。
- 彩色丝印格式与目标工艺匹配。

## 容易出错的地方

- 图片好看不证明制造后可读。
- 轮廓提取结果可能有自交或过多节点。

## 使用示例

“在底部丝印放置产品二维码和版本号。”

具体 API 入口、来源和执行范围见 [操作参考](references/operations.md)。

来源性质：从官方扩展与接口提炼的领域工作流。本技能的存在不代表上游扩展已安装或工作流已实测。
