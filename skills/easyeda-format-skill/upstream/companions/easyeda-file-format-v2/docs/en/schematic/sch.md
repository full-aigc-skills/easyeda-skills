# SCH Schematic Document

The `SCH` document describes the content of a schematic page.

## Header

```json
["DOCTYPE", "SCH", "1.0"]
["HEAD", {"ORIGIN_X": 0, "ORIGIN_Y": 0, "editorVersion": "4.7.8", "importFlag": 0}]
```

## HEAD Field Descriptions

1. `HEAD`: header identifier.
2. Internal Key-Value parameters:
   - `ORIGIN_X`, `ORIGIN_Y`: reserved for canvas origin offset, optional.
   - Other optional editor metadata for data analysis.

## Body Example

```json
["FONTSTYLE", "st001", "#880000", "Consolas", 7, 1, 0, 0, 0, 0, 0]
["FONTSTYLE", "st002", "#880000", "Consolas", 7, 1, 0, 0, 0, 0, 2]
["FONTSTYLE", "st003", "#880000", "Consolas", 7, 1, 0, 0, 0, 0, 2]
["LINESTYLE", "st004", "#880000", 0, "#664400", 1]
["LINESTYLE", "st005", "#880000", 1, "", 1]
["LINESTYLE", "st006", "#880000", 0, "#664400", 5]
["WIRE", "e112", [455, 265, 455, 485, 720, 485], "st005", 0]
["ATTR", "e111", "e112", "NET", "+5V", 1, 1, 108, 804.5, 0, "st002", 1]
["BUS", "e106", [455, 265, 455, 485, 720, 485], "st005", 0]
["ATTR", "e111", "e106", "NET", "+5V", 1, 1, 108, 804.5, 0, "st002", 1]
```

The schematic body consists of basic primitives such as `FONTSTYLE`, `LINESTYLE`, `WIRE`, `BUS`, and `COMPONENT`.
