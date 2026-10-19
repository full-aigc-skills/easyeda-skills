# NET

Net information differs from AD in that it is not mandatory. This format only requires it when there is a special net type or net color. The difference comes from whether there is a dedicated net settings interface listing all nets.

## Format

```json
["NET", "A", "High Speed", "#666666", 0, "AASDF", 1, "ABC"]
```

## Field Descriptions

1. `NET`: net identifier.
2. Net name.
3. Net type: `null` means no type.
4. Special color: `null` means no special color.
5. Whether to hide the air wire.
6. Differential pair name: `null` means not a differential pair.
7. Whether this is the positive side of the differential pair.
8. Equal-length group name: `null` means not in a group.

## Examples

```json
["NET", "A", "High Speed", "#666666", 0, "AASDF", 1, "ABC"]
["NET", "B", null, "#666666", 1, "AASDF", 0, "ABC"]
["NET", "C", "High Speed", null, 1, null, 0, null]
```
