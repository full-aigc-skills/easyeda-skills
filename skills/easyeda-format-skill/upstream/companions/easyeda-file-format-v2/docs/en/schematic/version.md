# Format Version

Schematic-related document types include:

- `SCH`: schematic document
- `SYMBOL`: symbol document

Current version examples:

```json
["DOCTYPE", "SCH", "1.1"]
["DOCTYPE", "SYMBOL", "1.1"]
```

## Field Descriptions

1. `DOCTYPE`: document type identifier.
2. Document type: `SCH` or `SYMBOL`.
3. Document format version: updated whenever the design format changes.

With a version number, forward compatibility can be handled by version.
