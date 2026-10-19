# 单多边形的定义

单多边形为首尾重合的一条不间断的线所描述的区域。如果首尾不重合需要将其自动重合。

```json
[300, 200, "L", 400, 200, "ARC", 400, 220, 15, "C", 200, 500, 400, 300, 100, 100]
["R", 100, 200, 300, 300, 0]
["CIRCLE", 100, 200, 5, 1]
```

## L 直线模式

```text
X Y L X Y X Y ...
```

模式为直线模式，所有坐标将用直线将其连一一连起来。

## ARC/CARC 圆弧模式

```text
startX startY ARC angle endX endY
```

- `startX/startY`：开始坐标。
- `angle`：圆弧角，逆时针正，顺时针负。
- `endX/endY`：结束坐标。

中心圆弧交互模式：

```text
startX startY CARC angle endX endY
```

## C 三阶贝塞尔模式

```text
X1 Y1 C X2 Y2 X3 Y3 X4 Y4 ...
```

模式为三阶贝塞尔模式，所有坐标为其控制点。

## R 矩形模式

```json
["R", 100, 200, 300, 300, 0]
```

```text
R X Y width height rot isCCW round
```

矩形模式与其它都不兼容，是一个独立的模式。

- `X/Y`：左上坐标。
- `width`：宽。
- `height`：高。
- `rot`：旋转角度。
- `isCCW`：是否逆时针。
- `round`：圆角半径。

## CIRCLE 圆形模式

```json
["CIRCLE", 100, 200, 5, 1]
```

```text
CIRCLE cx cy r isCCW
```

圆形模式与其它都不兼容，是一个独立的模式。

- `cx/cy`：中心点坐标。
- `r`：半径。
- `isCCW`：是否逆时针。
