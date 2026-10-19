# RECT

A rectangle is defined by two diagonal points; its rotation is around point 1.

## Format

```json
["RECT", "e172", 340, 210, 100, 200, 40, 30, 90, "st006", 0]
```

## Field Descriptions

1. `RECT`: primitive name.
2. ID: unique within the file.
3. Point 1 X.
4. Point 1 Y.
5. Point 2 X.
6. Point 2 Y.
7. Corner radius X: `0` means no rounding.
8. Corner radius Y: `0` means no rounding.
9. Rotation angle: around point 1.
10. Line style ID.
11. Locked.
