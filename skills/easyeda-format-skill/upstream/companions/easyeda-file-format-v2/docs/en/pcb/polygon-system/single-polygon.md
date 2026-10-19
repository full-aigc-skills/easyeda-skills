# Single Polygon Definition

A single polygon is a region described by an uninterrupted line whose start and end coincide. If the start and end do not coincide, they are automatically connected.

```json
[300, 200, "L", 400, 200, "ARC", 400, 220, 15, "C", 200, 500, 400, 300, 100, 100]
["R", 100, 200, 300, 300, 0]
["CIRCLE", 100, 200, 5, 1]
```

## L Line Mode

```text
X Y L X Y X Y ...
```

Line mode: all coordinates are connected one by one with straight lines.

## ARC/CARC Arc Mode

```text
startX startY ARC angle endX endY
```

- `startX/startY`: start coordinate.
- `angle`: arc angle, positive counter-clockwise, negative clockwise.
- `endX/endY`: end coordinate.

Center arc interaction mode:

```text
startX startY CARC angle endX endY
```

## C Cubic Bezier Mode

```text
X1 Y1 C X2 Y2 X3 Y3 X4 Y4 ...
```

Cubic Bezier mode: the coordinates are control points.

## R Rectangle Mode

```json
["R", 100, 200, 300, 300, 0]
```

```text
R X Y width height rot isCCW round
```

Rectangle mode is incompatible with the others and is a standalone mode.

- `X/Y`: top-left coordinate.
- `width`: width.
- `height`: height.
- `rot`: rotation angle.
- `isCCW`: whether counter-clockwise.
- `round`: corner radius.

## CIRCLE Circle Mode

```json
["CIRCLE", 100, 200, 5, 1]
```

```text
CIRCLE cx cy r isCCW
```

Circle mode is incompatible with the others and is a standalone mode.

- `cx/cy`: center coordinate.
- `r`: radius.
- `isCCW`: whether counter-clockwise.
