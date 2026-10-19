# IMAGE Image

`IMAGE` is very similar to `REGION`, but in operation `IMAGE` has no control points and cannot be freely reshaped; only global scale, rotate, flip, and translate operations are allowed.

When `IMAGE` is on a signal layer, from the DRC perspective it is an unconnected rectangular region defined by start, end, rotation angle, and whether it is mirrored.

## Format

```json
["IMAGE", "e100", 0, 31, 200, 200, 400, 400, 45, 1, <complex polygon>, 0]
```

## Field Descriptions

1. `IMAGE`: image identifier.
2. Primitive ID.
3. Group ID: `0` no group, non-`0` group marker.
4. Layer.
5. Top-left X.
6. Top-left Y.
7. Width.
8. Height.
9. Rotation angle, around the start point.
10. Whether the original image is mirrored horizontally around its original BBox center.
11. See Complex Polygon chapter; raw data is stored here and does not need adjustment during the lifecycle.
12. Locked.
