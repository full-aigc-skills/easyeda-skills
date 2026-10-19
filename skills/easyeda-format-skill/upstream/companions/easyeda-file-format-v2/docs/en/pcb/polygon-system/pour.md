# POUR Copper Pour Border

Compared to previous copper pours, a major difference is support for complex polygons. That is, the copper-pour region can contain holes, so in theory text paths converted to polygons can be used as copper-pour regions. Copper pours are processed in the order they appear in the format.

## Format

```json
["POUR", "e100", 5, "GND", 1, 1, "TOPGND", 4, <complex polygon>, [<pour type>], 1, 1]
```

## Field Descriptions

1. `POUR`: copper pour identifier.
2. Primitive ID.
3. Group ID: `0` no group, non-`0` group marker.
4. Net.
5. Layer.
6. Line width.
7. Copper pour name.
8. Copper pour priority.
9. See Complex Polygon chapter.
10. See Pour Type chapter.
11. Whether to retain islands.
12. Locked.

## Pour Types

### SOLID Solid Fill

```json
["SOLID", 2]
```

1. `SOLID`: solid fill identifier.
2. Minimum copper-pour neck width (manufacturing optimization, like AD's Neck); `0` disables optimization.

```json
["POUR", "e100", "GND", 1, "BOTGND", 2, <complex polygon>, ["SOLID", 2], 1, 0]
["POUR", "e100", "GND", 1, "BOTGND", 2, <complex polygon>, ["SOLID", 0], 1, 0]
```

### LINE Line Fill

```json
["LINE", 0, 0, 10, 20]
```

1. `LINE`: line fill identifier.
2. Fill mode: `0` grid fill, `1` horizontal line fill, `2` vertical line fill.
3. Rotation angle.
4. Line width.
5. Line spacing.

```json
["POUR", "e100", "GND", 1, "", 9, <complex polygon>, ["LINE", 0, 0, 10, 20], 0.6, 1, 0, 0]
```
