# EQLEN

## Format

```json
["EQLEN", 1, ["U1:1", "U2:3"]]
```

## Field Descriptions

1. `EQLEN`: equal-length configuration identifier.
2. Equal-length group ID.
3. Array of pads in `designator:pad_number` form.

## Examples

```json
["EQLEN", 1, ["U1:2", "U1:a"]]
["EQLEN", 2, ["U1:2", "C2:1"]]
```
