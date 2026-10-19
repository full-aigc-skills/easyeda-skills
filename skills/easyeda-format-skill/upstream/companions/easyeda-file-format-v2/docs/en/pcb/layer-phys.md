# LAYER_PHYS Layer Physical Properties

## Format

```json
["LAYER_PHYS", 1, "COPPER", 1, 0, 0, 0]
```

## Field Descriptions

1. `LAYER_PHYS`: layer physical properties identifier.
2. Layer number.
3. Layer material.
4. Thickness.
5. Dielectric constant.
6. Loss tangent.
7. Whether to retain islands on internal planes.

## Examples

```json
["LAYER_PHYS", 1, "COPPER", 1, 0, 0, 0]
["LAYER_PHYS", 2, "COPPER", 1, 0, 0, 0]
["LAYER_PHYS", 15, "COPPER", 1, 0, 0, 1]
["LAYER_PHYS", 50, "PP", 10, 4.5, 0.02, 0]
```
