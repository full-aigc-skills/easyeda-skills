# POURED Copper Pour Result Document

For a large PCB, re-pouring copper every time the file is opened is impractical, so the result is stored in the format. Copper pour results support fill and stroke:

- Fill: generally used for the filled part of solid fill.
- Stroke: generally used for thermal relief, grid copper, and solid-fill manufacturing-optimization outlines.

## Format

```json
["DOCTYPE", "POURED", "1.1"]
["POURED", "e105", "e100", 0, 1, <complex polygon>]
```

## Field Descriptions

1. `POURED`: copper pour result identifier.
2. Primitive ID.
3. Parent `POUR` ID.
4. Stroke line width: `0` means no stroke.
5. Whether to fill.
6. Path.

## Examples

```json
["POURED", "e105", "e100", 0, 1, <complex polygon>]
["POURED", "e106", "e100", 0.5, 0, <complex polygon>]
```
