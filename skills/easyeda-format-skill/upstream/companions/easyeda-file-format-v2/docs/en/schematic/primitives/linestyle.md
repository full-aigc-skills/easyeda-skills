# LINESTYLE

Like font styles, line styles are file-scoped abstractions used to compress format content size.

## Format

```json
["LINESTYLE", "st004", "#880000", 0, "#664400", 1]
```

## Field Descriptions

1. `LINESTYLE`: style identifier.
2. Line style ID: unique within the file.
3. Color.
4. Style: `0` solid, `1` dashed, `2` dotted, `3` dash-dot.
5. Fill color: `""` means no fill; when filled, start and end points are closed automatically.
6. Width.

## Examples

```json
["LINESTYLE", "st005", "#880000", 1, "", 1]
["LINESTYLE", "st006", "#880000", 0, "#664400", 5]
```
