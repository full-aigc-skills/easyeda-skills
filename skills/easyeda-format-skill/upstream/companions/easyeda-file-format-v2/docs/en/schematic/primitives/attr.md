# ATTR

`ATTR` is a generic primitive that:

1. Represents one of multiple key-value attributes.
2. Can be displayed on the canvas, controlling what is shown, the style, position, etc.

When the parent ID is not specified, it belongs to the current block-level primitive by default.

## Format

```json
["ATTR", "e177", "", "UUID", "432143214321", 1, 1, 300, 200, 0, "st002", 1]
```

## Field Descriptions

1. `ATTR`: attribute identifier.
2. ID: unique within the file.
3. Parent ID: the primitive it belongs to; `""` means the current block (default block is the file).
4. Attribute key.
5. Attribute value.
6. Whether to show the key.
7. Whether to show the value.
8. Position X: `null` if the attribute has never been displayed.
9. Position Y: `null` if the attribute has never been displayed.
10. Rotation angle, around the position.
11. Font style ID.
12. Locked.

## Overline Syntax

When the attribute value contains `~` characters, XTools renders text between odd and even `~` pairs with an overline.

Example:

```json
["ATTR", "e198", "", "ABCD", "kk~AB~Bb~233~dd", 0, 1, 300, 200, 0, "st002", 1]
```

## Example

```json
["ATTR", "e199", "", "_LTSPICE_PROGRAM_", ".tran 10m", 0, 1, 300, 200, 0, "st002", 1]
```
