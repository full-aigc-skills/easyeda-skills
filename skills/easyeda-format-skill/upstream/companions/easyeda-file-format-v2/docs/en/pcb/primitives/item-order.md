# ITEM_ORDER

Provides a suggested drawing order for PCB primitives. This information can appear only once.

## Format

```json
["ITEM_ORDER", ["e1", "e10", "e50", "e40e23", "e6"]]
```

## Field Descriptions

1. `ITEM_ORDER`: item order identifier.
2. Primitive IDs, in two forms:
   - Regular: `/^[a-z]+\d+$/i`, e.g., `e1`, `e123`.
   - Footprint instance: `/^[a-z]+\d+[a-z]+\d+$/i`, e.g., `e1e5`, `e12e22`.

This is a "suggestion" because, for example, if `e1` is on the top layer and `e2` is on the bottom layer, then:

```json
["ITEM_ORDER", ["e2", "e1"]]
```

`e1` is still on top by default unless a special operation places the bottom layer on top.
