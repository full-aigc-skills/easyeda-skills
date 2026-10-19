# LAYER_PHYS 层物理特性配置

## 格式

```json
["LAYER_PHYS", 1, "COPPER", 1, 0, 0, 0]
```

## 字段说明

1. `LAYER_PHYS`：层物理特性标识。
2. 层编号。
3. 层材质。
4. 厚度。
5. 介电常数。
6. 损耗切线。
7. 内电层是否保留孤岛。

## 示例

```json
["LAYER_PHYS", 1, "COPPER", 1, 0, 0, 0]
["LAYER_PHYS", 2, "COPPER", 1, 0, 0, 0]
["LAYER_PHYS", 15, "COPPER", 1, 0, 0, 1]
["LAYER_PHYS", 50, "PP", 10, 4.5, 0.02, 0]
```
