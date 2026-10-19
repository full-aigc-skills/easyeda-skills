# CREASE Side Crease Line

`CREASE` crease primitives must be used with `CONNECT` to associate `SHELL_ENTITY` and `BOSS`, expressing shell cutouts.

## Format

```json
["CREASE", "e34", 0, 49, 20, 30, 40, 50, 90, 0]
```

## Field Descriptions

1. `CREASE`: crease identifier.
2. Primitive ID.
3. Group ID: `0` no group, non-`0` group marker.
4. Layer number.
5. Start X.
6. Start Y.
7. End X.
8. End Y.
9. Fold angle.
10. Locked.
