# BUS

## Format

```json
["BUS", "e271", [[310, 550, 400, 550, 400, 460], [480, 460, 400, 460], [400, 330, 400, 460]], "st005", 0]
```

## Field Descriptions

1. `BUS`: primitive name.
2. ID: unique within the file.
3. Coordinates: split into polylines; each segment is a continuous list `X1 Y1 X2 Y2 X3 Y3 …`.
4. Line style ID.
5. Locked.

## NET Attribute

A bus must carry a `NET` attribute to identify the net name:

```json
["ATTR", "e200", "e271", "NET", "A[1:5]", 1, 1, 300, 200, 0, "st002", 1]
```
