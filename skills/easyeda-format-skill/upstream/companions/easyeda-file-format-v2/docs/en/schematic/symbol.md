# SYMBOL Document

## Header

```json
["DOCTYPE", "SYMBOL", "1.0"]
["HEAD", {"symbolType": 2}]
```

## HEAD Field Descriptions

1. `HEAD`: header identifier.
2. Internal Key-Value parameters:
   - `symbolType`: symbol type, used by other tools for recognition. XTools core logic should not rely on this property.
   - Other optional editor metadata for data analysis.

## PART

`PART` is a block-level element. No primitives may be outside the `PART` scope. Even single-part symbols must have a `PART`, using an empty `""` part number.

### Format

```json
["PART", "1", {"BBOX": [-10, -20, 10, 20]}]
```

### Field Descriptions

1. `PART`: sub-library primitive identifier.
2. Part number.
3. Internal Key-Value parameters:
   - `BBOX`: two diagonal points of the bounding box enclosing all primitives in the PART. XTools core logic should not rely on this property.
   - Other optional editor metadata for data analysis.

## Multi-PART Example

```json
["PART", "1", {"BBOX": [-10, -20, 10, 20]}]
["FONTSTYLE", "st002", "#880000", "Consolas", 7, 1, 0, 0, 0, 0, 2]
["ATTR", "e180", "", "NAME", "myname.1", 1, 1, 300, 200, 0, "st002", 1]
["ATTR", "e181", "", "PREFIX", "prefix.1", 1, 1, 300, 200, 0, "st002", 1]
["PIN", "e102", 1, 0, 350, 170, 20, 0, "#880000", 3, 0, 1]
["ATTR", "e184", "e102", "NAME", "VCC", 1, 1, 108, 804.5, 0, "st002", 1]
["ATTR", "e185", "e102", "NUMBER", "1", 1, 1, 108, 804.5, 0, "st002", 1]
["TEXT", "e106", 108, 804.5, 0, "any text", "st002", 1]
["LINESTYLE", "st006", "#880000", 0, "#664400", 5]
["RECT", "e107", 340, 210, 350, 220, 0, 0, 90, "st006", 0]
["POLY", "e108", [390, 260, 450, 300, 560, 280, 540, 320], 0, "st006", 0]
["LINESTYLE", "st005", "#880000", 1, "", 1]
["ARC", "e174", -10, 0, 0, 10, 10, 0, "st005", 0]

["PART", "2", {"BBOX": [-10, -20, 10, 20]}]
["ATTR", "e180", "", "NAME", "myname.1", 1, 1, 300, 200, 0, "st002", 1]
["ATTR", "e181", "", "PREFIX", "prefix.1", 1, 1, 300, 200, 0, "st002", 1]
["PIN", "e102", 1, 0, 350, 170, 20, 0, "#880000", 3, 0, 0, 1]
["ATTR", "e184", "e102", "NAME", "GND", 1, 1, 108, 804.5, 0, "st002", 1]
["ATTR", "e185", "e102", "NUMBER", "2", 1, 1, 108, 804.5, 0, "st002", 1]
["TEXT", "e106", 108, 804.5, 0, "any text", "st002", 1]
["RECT", "e107", 340, 210, 350, 220, 0, 0, 90, "st006", 0]
["POLY", "e108", [390, 260, 450, 300, 560, 280, 540, 320], 0, "st006", 0]
["ARC", "e174", -10, 0, 0, 10, 10, 0, "st005", 0]
```
