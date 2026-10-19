# COMPONENT

`COMPONENT` references a Symbol. Symbols support multiple PARTs, so the part number attribute indicates which one; for a single-part symbol, use the default `""`.

## Format

```json
["COMPONENT", "e176", "1", 300, 200, 15, 0, {}, 0]
```

## Field Descriptions

1. `COMPONENT`: COMPONENT identifier.
2. ID: unique within the file.
3. Part number: default `""`.
4. Position X.
5. Position Y.
6. Rotation angle: around the position.
7. Mirrored.
8. Pure data attributes: additional information for internal editor logic.
9. Locked.

## Transformation Order

The referenced Symbol primitives are transformed in the following order:

1. Rotate counter-clockwise around the origin `(0,0)` by the rotation angle.
2. If mirrored is `1`, mirror horizontally around the Y axis through the origin `(0,0)`.
3. Translate by the position.

## Attribute Overrides

A Component can bind multiple `ATTR`; their behavior is defined by the tool.

### Device Attribute

```json
["ATTR", "e187", "e176", "Device", "device-uuid-1", 1, 1, 300, 200, 0, "st002", 1]
```

Device UUID must match the filename in the `devices` section of `project.json`.

### Symbol Attribute

```json
["ATTR", "e188", "e176", "Symbol", "symbol-uuid-1", 1, 1, 300, 200, 0, "st002", 1]
```

`ATTR` inside `COMPONENT` overrides the same-name attribute in the template. Overriding `Symbol` affects the device's symbol binding.

### Footprint Attribute

```json
["ATTR", "e188", "e176", "Footprint", "footprint-uuid-1", 1, 1, 300, 200, 0, "st002", 1]
```

Overriding `Footprint` affects the device's footprint binding.

### Designator Attribute

```json
["ATTR", "e178", "e176", "Designator", "U1", 1, 1, 300, 200, 0, "st002", 1]
```

### PIN Attribute Override

```json
["ATTR", "e180", "e176e5", "NUMBER", "1", 1, 1, 108, 804.5, 0, "st002", 1]
```

The key is the `ATTR` parent ID. The ID is split: `e176e5` means `e176` is the `COMPONENT` ID and `e5` is the `PIN` ID within the template.
