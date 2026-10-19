# FOOTPRINT File Format

`FOOTPRINT` is basically the same as `PCB`, but the available primitives are limited. The exact allowed primitives depend on requirements; the format does not restrict them too much.

Except that `DEVICE`, `FOOTPRINT`, and `COMPONENT` primitives must not exist, footprints should not recursively reference other footprints.

## Header

```json
["DOCTYPE", "FOOTPRINT", "1.0"]
["HEAD", {"editorVersion": "4.7.8", "importFlag": 0}]
["CANVAS", 0, 0, "mm", 10, 10]
["LAYER", 0, "TOP", "Top Layer", 1, "#FF0000", 0.5, "#880000", 0.3]
```

## Body Example

```json
["PAD", "e100", 1, "GND", 0, "1", 100, 200, 15, [], [], [[0, 1, []]], 10, -5, 30, 1, 0, null, 0.5, 0.4, null, 0]
```
