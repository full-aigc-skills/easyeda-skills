# 格式版本

PCB 相关文档类型包括：

- `PCB`：PCB 文档
- `FOOTPRINT`：封装文档
- `POURED`：覆铜结果文档

当前版本示例：

```json
["DOCTYPE", "PCB", "1.6"]
["DOCTYPE", "FOOTPRINT", "1.6"]
["DOCTYPE", "POURED", "1.1"]
```

## 字段说明

1. `DOCTYPE`：文档类型标识。
2. 文档类型：`PCB`、`FOOTPRINT` 或 `POURED`。
3. 文档格式版本号：每次发布设计格式变动的版本前都要调整版本号。
