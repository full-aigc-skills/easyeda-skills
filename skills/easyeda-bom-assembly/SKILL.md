---
name: easyeda-bom-assembly
description: "比较或导出 EasyEDA BOM，使用交互式 BOM 核对装配位号、封装和贴片坐标。"
license: Apache-2.0
metadata:
  source-kind: extension-derived
---

# easyeda-bom-assembly

比较或导出 EasyEDA BOM，使用交互式 BOM 核对装配位号、封装和贴片坐标。

## 首次使用

读取 [原生 MCP 约定](references/native-mcp.md)，按真实工具返回执行 help、doctor、session.list。
不要把工程为空或扩展未安装解释为需要切换到 WebSocket Gateway。

## 当前任务

需要明确：装配版本与 DNP 规则；BOM 或对比文件；贴片坐标的单位和原点要求。

1. 识别表格列、位号展开、数量和装配变体。
2. 导出或读取 BOM 并核对库器件属性。
3. 对比版本差异，区分新增、删除、替代和参数变化。
4. 按需生成交互式 BOM 或贴片坐标。
5. 核对位号、封装、数量、面与旋转。

## 验证结果

- BOM 数量可追溯到实际器件。
- DNP 与变体正确过滤。
- 坐标原点、镜像及底面旋转明确。

## 容易出错的地方

- 不同表格分隔符不可按扩展名猜测。
- 交互式预览不能代替贴片厂坐标规范。
- 自定义 PCB 价格模型不是板厂实时正式报价。

## 使用示例

“比较两版 BOM，列出型号和装配数量变化。”

具体 API 入口、来源和执行范围见 [操作参考](references/operations.md)。

来源性质：从官方扩展与接口提炼的领域工作流。本技能的存在不代表上游扩展已安装或工作流已实测。
