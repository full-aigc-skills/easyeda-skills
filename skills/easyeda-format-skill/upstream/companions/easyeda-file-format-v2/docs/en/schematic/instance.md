# INSTANCE Attribute Document

Instance attribute override is a block-level primitive, similar to `PART`.

## Header

```json
["DOCTYPE", "INSTANCE", "1.0"]
```

## OVERRIDE

### Format

```json
['OVERRIDE', ['Schematic ID', '$5e100', '$1e55', '$6e15', '$8'], { 'e176': { 'Designator': 'U15', 'ASDF': '1234' }, '': { 'Author': 'abc' }, 'e176e5': { 'NUMBER': 2 } }]
```

### Field Descriptions

1. `OVERRIDE`: instance attribute override identifier.
2. Instance path:
   - `Schematic ID` is the top-level schematic; it must match the name under `schemtaics` in `project.json`.
   - The last element is the Sheet number.
   - Intermediate elements use combined ID syntax to locate Block Symbols, e.g., `$1e2`, where `1` is the sheet ID and `e2` is the Block Symbol ID.
3. Attribute override data signature: `{ [parentId: string]: { [key: string]: string } }`.

### Non-hierarchical Instance

```json
['OVERRIDE', ['Schematic ID', '$5'], { 'e176': { 'Designator': 'U15', 'ASDF': '1234' }, '': { 'Author': 'abc' }, 'e176e5': { 'NUMBER': 2 } }]
```

This format targets non-hierarchical instance overrides.
