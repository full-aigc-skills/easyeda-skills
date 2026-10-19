# Version

PCB-related document types include:

- `PCB`: PCB document
- `FOOTPRINT`: footprint document
- `POURED`: copper-pour result document

Current version examples:

```json
["DOCTYPE", "PCB", "1.6"]
["DOCTYPE", "FOOTPRINT", "1.6"]
["DOCTYPE", "POURED", "1.1"]
```

## Field Descriptions

1. `DOCTYPE`: document type identifier.
2. Document type: `PCB`, `FOOTPRINT`, or `POURED`.
3. Document format version: bumped whenever the design format changes.
