# 3D Model Transform 的特殊说明

在器件中，固定 `3D Model Transform` 为 3D 模型为匹配此器件【在顶层】【坐标 0,0】【旋转角度 0】时所需要的变换参数。

## 参数

1. `sizeX`：X 轴尺寸。
2. `sizeY`：Y 轴尺寸。
3. `sizeZ`：Z 轴尺寸。这里有个兼容性处理，如果为 `0`，则自动适应高度。
4. `rotZ`：绕 Z 轴旋转角度。
5. `rotX`：绕 X 轴旋转角度。
6. `rotY`：绕 Y 轴旋转角度。
7. `offX`：X 轴偏移量。
8. `offY`：Y 轴偏移量。
9. `offZ`：Z 轴偏移量。

## 变换矩阵算法

```text
cx = 3D 模型 X 轴中点
cy = 3D 模型 Y 轴中点
bz = 3D 模型 最低 Z 值

wx = 3D 模型 X 轴宽度
wy = 3D 模型 Y 轴宽度
wz = 3D 模型 Z 轴宽度

ORIGIN = translate(-cx, -cy, -bz)
SCALE = scale(sizeX / wx, sizeY / wy, sizeZ / wz)
ROT = rotateZXY(rotZ, rotX, rotY)
OFFSET = translate(offX, offY, offZ)

MATRIX = OFFSET X ROT X SCALE X ORIGIN
```
