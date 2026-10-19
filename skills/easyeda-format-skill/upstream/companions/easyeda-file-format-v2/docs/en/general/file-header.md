# Common File Header Format

The common file header identifies the document type and version to facilitate forward compatibility.

## Format

```json
["DOCTYPE", "SCH", "1.0"]
```

## Field Descriptions

1. `DOCTYPE`: Document type identifier.
2. Document type: possible values include `SCH`, `SYMBOL`, `INSTANCE`, `PCB`, `FOOTPRINT`, `PANEL`, etc.
3. Document format version: updated whenever the design format changes.

With a version number, forward compatibility can be handled by version rather than requiring every primitive to be forward compatible. For example, changing:

```json
["ARC", "e5", 340, 210, ...]
```

to:

```json
["ARC", "e5", [340, 210], ...]
```

only requires updating the version number; no old positions need to be reserved.

## HEAD Header

```json
["HEAD", {"editorVersion": "4.7.8", "importFlag": 0}]
```

1. `HEAD`: Header identifier.
2. Internal Key-Value parameters: optional editor metadata for data analysis.
