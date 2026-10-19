# SHELL Shell

## Format

```json
["SHELL", "e33", 0, "T&B", 100, 50, 10, <complex polygon>, {}, 0]
```

## Field Descriptions

1. `SHELL`: shell identifier.
2. Primitive ID.
3. Group ID: `0` no group, non-`0` group marker.
4. Shell type:
   - `T&B`: top and bottom shell
   - `DRAWER`: drawer
   - `CLAM`: clam shell
5. Shell height.
6. PCB height.
7. Line width (deprecated).
8. See Complex Polygon.
9. Custom properties: each shell type has its own custom properties.
10. Locked.

## Custom Properties

### T&B

- `Thickness`: shell thickness.
- `BottomHeight`: bottom shell height.
- `TopInnerHeight`: top shell inner wall height.
- `TopInnerThickness`: top shell inner wall thickness.

### DRAWER

- `Thickness`: shell thickness.
- `Direction`: drawer direction.
  - `1`: positive X
  - `2`: negative X
  - `4`: positive Y
  - `8`: negative Y
