# Complex Polygon Definition

```json
[[single polygon 1], [single polygon 2]]
```

A complex polygon can contain multiple single polygons, combined via a fill-rule (refer to SVG path). This enables boolean operations such as subtraction, commonly used for polygons with holes.

Currently the `nonzero` fill-rule is always used.
