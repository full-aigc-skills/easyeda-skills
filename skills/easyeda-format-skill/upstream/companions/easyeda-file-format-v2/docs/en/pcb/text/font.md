# FONT Font Cache

To achieve consistent font paths across devices, the format saves a cache of text paths.

## Format

```json
["FONT", "asdf", "Arial", 50, 10, 1, 1, 1, -1, 300, 100, <complex polygon>]
```

## Field Descriptions

1. `FONT`: font cache identifier.
2. Text content.
3. Font name.
4. Font size.
5. Weight.
6. Whether bold.
7. Whether italic.
8. Whether inverse expansion.
9. Inverse expansion size; supports negative values.
10. Width.
11. Height.
12. Text cache: array of complex polygons. See Complex Polygon. The path always expresses the following state:
    - origin at `0,0`
    - rotation angle `0`
    - alignment mode left-bottom
    - not mirrored

The font path cache is not refreshed when text is moved, rotated, or mirrored (including moving from top to bottom layer).
