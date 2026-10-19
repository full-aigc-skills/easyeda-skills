# VIA

Vias connect circuits between layers. For multilayer boards there are three patterns:

- Through-hole: spans top to bottom.
- Blind via: only one end is top or bottom.
- Buried via: neither end is top nor bottom.

## Format

```json
["VIA", "e100", 0, "GND", "asdf", 100, 200, 5, 9, 0, null, null, null, null, 0]
```

## Field Descriptions

1. `VIA`: via identifier.
2. Primitive ID.
3. Group ID: `0` no group, non-`0` group marker.
4. Net.
5. Via layer type: design rule name defining start and end layers.
6. X coordinate.
7. Y coordinate.
8. Hole diameter.
9. Pad diameter.
10. Via type: `0` regular via, `1` stitching via.
11. Top solder mask expansion: `null` follows rules.
12. Bottom solder mask expansion: `null` follows rules.
13. Locked.

## Example

```json
["VIA", "e101", 1, "VCC", "fdsa", 100, 200, 5, 9, 1, null, 0.5, 0.4, null, 0]
```
