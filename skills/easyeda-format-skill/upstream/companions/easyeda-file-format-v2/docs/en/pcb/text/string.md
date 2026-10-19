# STRING Text

When `STRING` is on a signal layer, from the DRC perspective it is:

1. Unconnected.
2. A BBox at position `0,0`, rotation `0`, and no mirroring.
3. A rectangle after applying position, rotation, and mirroring transformations.

## Format

```json
["STRING", "e100", 0, 1, 300, 600, "text", "SimSun", 50, 10, 0, 0, 5, 15, 1, 0, 1, 1]
```

## Field Descriptions

1. `STRING`: text identifier.
2. Primitive ID.
3. Group ID: `0` no group, non-`0` group marker.
4. Layer.
5. Position X.
6. Position Y.
7. Content.
8. Font name.
9. Font size.
10. Weight.
11. Whether bold.
12. Whether italic.
13. Alignment mode: `0` left-top, `1` center-top, `2` right-top, `3` left-center, `4` center-center, `5` right-center, `6` left-bottom, `7` center-bottom, `8` right-bottom.
14. Rotation angle.
15. Whether inverse expansion.
16. Inverse expansion size: supports negative values.
17. Whether mirrored. Generally, when text appears on the bottom layer, this should be set to `1`.
18. Locked.
