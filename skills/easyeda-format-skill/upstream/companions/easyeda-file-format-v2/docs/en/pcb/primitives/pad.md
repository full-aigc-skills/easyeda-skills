# PAD

Pads connect components to the board. A pad either goes through the entire board or exists only on the top or bottom layer, so only top, bottom, and multilayer are valid.

## Format

```json
["PAD", "e100", 1, "GND", 0, "1", 100, 200, 15, ["ROUND", 5, 6], ["RECT", 7], [[0, 1, ["NGON", 6, 8]]], 10, -5, 30, 1, 0, null, 0.5, 0.4, null, 0, 0, 10, 5, 45]
```

## Field Descriptions

1. `PAD`: pad identifier.
2. Primitive ID.
3. Group ID: `0` no group, non-`0` group marker.
4. Net.
5. Layer (top, bottom, or multilayer).
6. Pad number.
7. Pad origin X.
8. Pad origin Y.
9. Pad rotation angle.
10. Hole: hole definition, `null` means no hole.
11. Default pad: pad shape definition.
12. Special pad (multiple groups):
    - start layer
    - end layer
    - pad shape definition
13. Hole offset X.
14. Hole offset Y.
15. Hole rotation relative to the pad.
16. plated: whether the hole wall is metallized.
17. Pad function: `0` regular pad, `1` test point, `2` fiducial.
18. Top solder mask expansion: `null` follows rules.
19. Bottom solder mask expansion: `null` follows rules.
20. Top paste mask expansion: `null` follows rules.
21. Bottom paste mask expansion: `null` follows rules.
22. Locked.
23. Thermal relief connection mode: `null` follows rules.
24. Thermal relief spoke spacing: `null` follows rules.
25. Thermal relief spoke width: `null` follows rules.
26. Thermal relief spoke angle: `null` follows rules.

## Hole Shapes

### Round slot

```json
["ROUND", 5, 6]
```

- `ROUND`: round slot.
- width.
- height.

### Rectangular slot

```json
["RECT", 7]
```

- `RECT`: rectangular slot.
- width.
- height.

Hole rotation is independent of pad rotation.

## Pad Shapes

### Round pad

```json
["ROUND", 5, 6]
```

### Rectangular pad

```json
["RECT", 5, 6, 2]
```

### Regular polygon pad

```json
["NGON", 6, 8]
```

- `NGON`: regular polygon pad (name from 3DSMAX).
- diameter.
- number of sides (> 2).

### Polygon pad

```json
["POLY", [["L", 1, 1, 3, 3, -5, 0]]]
```

- `POLY`: polygon pad.
- complex polygon relative to the hole origin.

## Example

```json
[
  "PAD",
  "e100",
  2,
  "GND",
  0,
  "1",
  100,
  200,
  15,
  ["ROUND", 5, 6],
  [
    [0, 1, ["RECT", 7]],
    [2, 4, ["NGON", 6, 8]],
    [2, 4, ["POLY", [["L", 1, 1, 3, 3, -5, 0]]]]
  ],
  10,
  -5,
  30,
  0,
  1,
  null,
  null,
  null,
  null,
  0
]
```
