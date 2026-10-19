# POLY Polyline

Polylines are similar to `LINE` and `ARC`, but they maintain the concept of a single continuous line when drawn, allowing conversion with `REGION`, `FILL`, and `POUR`.

## Format

```json
["POLY", "e100", 0, "GND", 1, 0.5, <single polygon>, 0]
```

## Field Descriptions

1. `POLY`: polyline identifier.
2. Primitive ID.
3. Group ID: `0` no group, non-`0` group marker.
4. Net.
5. Layer.
6. Line width.
7. See Single Polygon chapter.
8. Locked.
