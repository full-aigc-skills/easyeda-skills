# PCB File Format

## Header

```json
["DOCTYPE", "PCB", "1.0"]
["HEAD", {"editorVersion": "4.7.8", "importFlag": 0}]
["CANVAS", 0, 0, "mm", 10, 10]
["LAYER", 0, "TOP", "Top Layer", 1, "#FF0000", 0.5, "#880000", 0.3]
```

## Body Example

```json
["LINE", "e100", 1, "GND", 1, 100, 200, 400, 300, 0.7, 0]
["ARC", "e100", 3, "GND", 1, 100, 200, 300, 400, -170, 10, 0]
["VIA", "e100", 0, "GND", "asdf", 100, 200, 5, 9, 0, null, null, null, null, 0]
```

The PCB body consists of basic primitives including `NET`, `PRIMITIVE`, `GROUP`, `SILK_OPTS`, `PREFERENCE`, `CONNECT`, `VIA`, `PAD`, `LINE`, `ARC`, `OBJ`, `ITEM_ORDER`, `PROP`, `EQLEN_GRP`, and `EQLEN`.
