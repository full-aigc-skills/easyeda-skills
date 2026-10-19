# PREFERENCE

## Format

```json
["PREFERENCE", 1, 1.2, 1, 5, 10, 1, 1, "R45", 1, 0, 0, 1]
```

## Field Descriptions

1. `PREFERENCE`: preference identifier.
2. Whether routing follows the last setting.
3. Last routing width.
4. Whether via size follows the last setting.
5. Last via inner diameter.
6. Last via outer diameter.
7. Whether snap is enabled.
8. Routing mode: `0` none, `1` push, `2` hug, `3` block.
9. Routing corner mode:
   - `"L45"`: line 45 degrees
   - `"L90"`: line 90 degrees
   - `"R45"`: arc 45 degrees
   - `"R90"`: arc 90 degrees
   - `"L"`: line free angle
   - `"R"`: arc free angle
10. Whether routing automatically removes loops.
11. Whether single-object rotation is enabled.
12. Whether traces follow footprint movement.
13. Minimum trace corner ratio (relative to trace width).
