# SHELL_ENTITY Shell Entity Region

A `SHELL_ENTITY` not associated with `CREASE` via `CONNECT` fills or cuts the top and bottom shells vertically.

## Format

```json
["SHELL_ENTITY", "e35", 0, 50, 0, 0, 10, 10, <complex polygon>, 0]
```

## Field Descriptions

1. `SHELL_ENTITY`: shell entity region identifier.
2. Primitive ID.
3. Group ID: `0` no group, non-`0` group marker.
4. Layer number.
5. Boolean operation: `0` cut, `1` fill.
6. Belongs to: `0` automatic, `1` top shell, `2` bottom shell, `4` shell border, `8` boss, `16` entity; can be combined by addition.
   - Top and bottom shell: `3 = 1 + 2`
   - Shell border + boss: `12 = 4 + 8`
   - Boss + entity: `24 = 8 + 16`
   - Shell border + boss + entity: `28 = 4 + 8 + 16`
7. Depth.
8. Line width.
9. See Complex Polygon.
10. Locked.
