# PIN

All `PIN` position X/Y values are at the endpoint farthest from the black rectangle.

- PIN 1: 0-degree rotation, pin style 0.
- PIN 2: 90-degree rotation, pin style 1.
- PIN 3: 180-degree rotation, pin style 2.
- PIN 4: 270-degree rotation, pin style 3.

## Format

```json
["PIN", "e102", 1, 0, 350, 170, 20, 0, "#880000", 3, 1]
```

## Field Descriptions

1. `PIN`: primitive name.
2. ID: unique within the file.
3. Visible.
4. Electrical type: `0` UNKNOWN, `1` INPUT, `2` OUTPUT, `3` BI.
5. Position X.
6. Position Y.
7. Pin length.
8. Rotation angle: `0`, `90`, `180`, `270`.
9. Pin color.
10. Pin style: `1` Clock, `2` DOT; can be combined with bitwise OR, e.g., `3 = 1 | 2`.
    - `0`: no addition
    - `1`: Clock
    - `2`: DOT
    - `3`: Clock & DOT
11. Locked.

## Required Attributes

A `PIN` must have `NAME` and `NUMBER` attributes:

```json
["ATTR", "e184", "e102", "NAME", "VCC", 1, 1, 108, 804.5, 0, "st002", 1]
["ATTR", "e185", "e102", "NUMBER", "1", 1, 1, 108, 804.5, 0, "st002", 1]
```
