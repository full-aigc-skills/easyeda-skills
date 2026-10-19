# FONTSTYLE

The style mechanism is only an abstraction for compressing format content size and has no entity mapping in XTools. Styles can appear before being referenced. All styles are file-scoped (e.g., styles inside a `PART` do not belong to that `PART`). All style contents except the style identifier and ID can be `null` to use default styles.

## Format

```json
["FONTSTYLE", "st001", "#880000", "#880000", null, 7, null, 0, 0, 0, 1, 0]
```

## Field Descriptions

1. `FONTSTYLE`: style identifier.
2. Font style ID: unique within the file.
3. Color.
4. Background color.
5. Font name.
6. Font size, same unit as coordinates.
7. Italic.
8. Bold.
9. Underline.
10. Strikethrough.
11. Vertical alignment: `0` top, `1` middle, `2` bottom.
12. Horizontal alignment: `0` left, `1` center, `2` right.

## Examples

```json
["FONTSTYLE", "st002", "#880000", "", "Consolas", 7, 1, 0, 0, 1, 1, 2]
["FONTSTYLE", "st003", "#880000", "", "Consolas", 7, 1, 0, 0, 0, 0, 2]
```
