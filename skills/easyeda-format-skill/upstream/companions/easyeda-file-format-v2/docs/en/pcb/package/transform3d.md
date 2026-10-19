# 3D Model Transform Notes

In a component, the fixed `3D Model Transform` gives the transformation parameters required for the 3D model to match this component at the top layer, position `0,0`, and rotation angle `0`.

## Parameters

1. `sizeX`: X-axis size.
2. `sizeY`: Y-axis size.
3. `sizeZ`: Z-axis size. For compatibility, if `0`, the height is automatically adapted.
4. `rotZ`: rotation around the Z-axis.
5. `rotX`: rotation around the X-axis.
6. `rotY`: rotation around the Y-axis.
7. `offX`: X-axis offset.
8. `offY`: Y-axis offset.
9. `offZ`: Z-axis offset.

## Transformation Matrix Algorithm

```text
cx = 3D model X-axis midpoint
cy = 3D model Y-axis midpoint
bz = 3D model minimum Z value

wx = 3D model X-axis width
wy = 3D model Y-axis width
wz = 3D model Z-axis width

ORIGIN = translate(-cx, -cy, -bz)
SCALE = scale(sizeX / wx, sizeY / wy, sizeZ / wz)
ROT = rotateZXY(rotZ, rotX, rotY)
OFFSET = translate(offX, offY, offZ)

MATRIX = OFFSET X ROT X SCALE X ORIGIN
```
