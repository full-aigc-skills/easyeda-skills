# ATTR Attribute

Attributes describe properties of a PCB or FOOTPRINT that may need to be displayed on the drawing.

## Format

```json
["ATTR", "e100", 0, "", 1, 200, 150, "DESIGNATOR", "U1", 0, 1, "SimSun", 50, 10, 0, 0, 5, 15, 1, 0, 1, 1]
```

## Field Descriptions

1. `ATTR`: attribute identifier.
2. Primitive ID.
3. Group ID: `0` no group, non-`0` group marker.
4. Parent ID; empty means the current block-level primitive.
5. Layer.
6. Position X: `null` for attributes that have never been displayed.
7. Position Y: `null` for attributes that have never been displayed.
8. Key.
9. Value.
10. Whether to display Key.
11. Whether to display Value.
12. Font name.
13. Font size.
14. Weight.
15. Whether bold.
16. Whether italic.
17. Alignment mode: `0` left-top, `1` center-top, `2` right-top, `3` left-center, `4` center-center, `5` right-center, `6` left-bottom, `7` center-bottom, `8` right-bottom.
18. Rotation angle.
19. Whether inverse expansion.
20. Inverse expansion size: supports negative values.
21. Whether mirrored. Generally, when text appears on the bottom layer, this should be set to `1`.
22. Locked.
