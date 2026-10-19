# LAYER Layer Configuration

The order in which `SIGNAL`, `PLANE`, and `SUBSTRATE` layers appear implies their physical stacking order. The format does not limit the number of `SIGNAL`, `PLANE`, and `SUBSTRATE` layers. It also does not assume a stable relationship between layer number and layer meaning; the implementation decides.

## Format

```json
["LAYER", 0, "TOP", "Top Layer", 1, "#FF0000", 0.5, "#880000", 0.3]
```

## Field Descriptions

1. `LAYER`: layer identifier.
2. Layer number: unique.
3. Layer type.
4. Layer alias: must be unique.
5. State: `1` used, `2` visible, `4` locked; can be combined by addition.
   - Used and visible: `3 = 1 + 2`
   - Used and locked but not visible: `5 = 1 + 4`
   - Used, visible, and locked: `7 = 1 + 2 + 4`
6. Active color.
7. Active opacity.
8. Inactive color.
9. Inactive opacity.

## Examples

```json
["LAYER", 0, "TOP", "Top Layer", 1, "#FF0000", 0.5, "#880000", 0.3]
["LAYER", 2, "BOTTOM", "Bottom Layer", 1, "#0000ff", 1, "#00007f", 1]
["LAYER", 3, "TOP_SILK", "Top Silkscreen Layer", 1, "#ffcc00", 1, "#7f6600", 1]
["LAYER", 4, "BOT_SILK", "Bottom Silkscreen Layer", 1, "#66cc33", 1, "#336619", 1]
["LAYER", 5, "TOP_SOLDER_MASK", "Top Solder Mask Layer", 1, "#800080", 1, "#400040", 1]
["LAYER", 6, "BOT_SOLDER_MASK", "Bottom Solder Mask Layer", 1, "#aa00ff", 1, "#55007f", 1]
["LAYER", 7, "TOP_PASTE_MASK", "Top Paste Mask Layer", 1, "#808080", 1, "#404040", 1]
["LAYER", 8, "BOT_PASTE_MASK", "Bottom Paste Mask Layer", 1, "#800000", 1, "#400000", 1]
["LAYER", 9, "TOP_ASSEMBLY", "Top Assembly Layer", 1, "#33cc99", 1, "#19664c", 1]
["LAYER", 10, "BOT_ASSEMBLY", "Bottom Assembly Layer", 1, "#5555ff", 1, "#2a2a7f", 1]
["LAYER", 11, "OUTLINE", "Board Outline Layer", 1, "#ff00ff", 1, "#7f007f", 1]
["LAYER", 12, "MULTI", "Multi-Layer", 1, "#c0c0c0", 1, "#606060", 1]
["LAYER", 13, "DOCUMENT", "Document Layer", 1, "#ffffff", 1, "#7f7f7f", 1]
["LAYER", 14, "MECHANICAL", "Mechanical Layer", 1, "#f022f0", 1, "#781178", 1]
["LAYER", 50, "SUBSTRATE", "Dialectric1", 3, "#999966", 1, "#4c4c33", 1]
```
