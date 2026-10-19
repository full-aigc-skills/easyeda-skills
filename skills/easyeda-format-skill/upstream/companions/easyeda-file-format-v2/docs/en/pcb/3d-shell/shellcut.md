# SHELLCUT Shell Cutout Region (Deprecated)

A `SHELLCUT` not associated with `CREASE` via `CONNECT` cuts vertically through the top and bottom shells.

## Format

```json
["SHELLCUT", "e35", 0, 50, 10, 10, <complex polygon>, 0]
```

## Field Descriptions

1. `SHELLCUT`: shell cutout region identifier.
2. Primitive ID.
3. Group ID: `0` no group, non-`0` group marker.
4. Layer number.
5. Depth.
6. Line width.
7. See Complex Polygon.
8. Locked.
