# COMPONENT 器件实例

## 格式

```json
["COMPONENT", "e8", 5, 1, 150, 200, 45, {"3D Model": "uuid", "3D Model Transform": "20,10,0,0,15,45,0,0,20"}, 0]
```

## 字段说明

1. `COMPONENT`：实例标识。
2. 图元编号。
3. 分组编号：`0` 不分组，非 `0` 为组标志，相同组标志的为一组。
4. 层（只有顶层底层）。
5. 位置 X。
6. 位置 Y。
7. 旋转角度。
8. 自定义属性。
9. 是否锁定。

## 自定义属性

- 固定 `3D Model` 为 3D 模型的 uuid，此 uuid 代表 components 表中 doctype = 16 的一条记录。
- 固定 `3D Model Transform` 为 3D 模型变换参数。

## 属性示例

```json
["ATTR", "e102", 0, "e8", 1, "Designator", "U1", 0, 1, "宋体", 50, 10, 0, 0, 0, 1, 2, 15, 1, 1]
["ATTR", "e103", 0, "e8", 1, "Footprint", "footprint-uuid", 0, 1, "宋体", 50, 10, 0, 0, 0, 1, 2, 15, 1, 1]
["ATTR", "e104", 0, "e8", 1, "Device", "device-uuid", 0, 1, "宋体", 50, 10, 0, 0, 0, 1, 2, 15, 1, 1]
```

## PAD_NET

```json
["PAD_NET", "e8", "a1", "GND", "e125"]
```

1. `PAD_NET`：焊盘实例网络映射标识。
2. 所属器件实例编号。
3. 焊盘编号。
4. 网络名。
5. 封装内焊盘 ID（可选）。

## REUSE_BLOCK

```json
["REUSE_BLOCK", "e8", "$1e16", "$2e5_$4e3"]
```

1. `REUSE_BLOCK`：复用图块信息标识。
2. 所属器件实例编号。
3. 分组 ID。
4. 通道 ID。
