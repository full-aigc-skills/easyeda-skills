# DIMENSION Dimension Tools

## Format

```json
["DIMENSION", "e101", "RADIUS", 3, "mm", 0.5, 3, 1, [100, 200, 300, 400, 400, 400], 0]
```

## Field Descriptions

1. `DIMENSION`: dimension identifier.
2. Primitive ID.
3. Dimension type: `RADIUS` radius, `LENGTH` length, `ANGLE` angle.
4. Layer.
5. Unit: `mm`, `cm`, `inch`, `mil`.
6. Line width.
7. Precision.
8. Whether text follows: `1` the tool automatically decides text position, `0` always use the `ATTR` position.
9. Coordinate set `X1 Y1 X2 Y2 X3 Y3 ...`; different dimension types interpret coordinates differently.
10. Locked.

## Dimension Properties

`DIMENSION` needs an attached attribute with Key `VALUE` to express the text part of the dimension tool. The EDA tool should ignore unnecessary properties such as whether Key/Value is displayed.

```json
["ATTR", "e102", 0, "e101", 1, 200, 150, "VALUE", "1234mm", 0, 1, "SimSun", 50, 10, 0, 0, 0, 2, 15, 1, 1]
```

## Dimension Types

- Radius tool: the first coordinate is the contact point with the ARC, the last coordinate is the default text position.
- Length tool: the coordinate set needs exactly four points.
- Angle tool: the coordinate set needs exactly three points.
