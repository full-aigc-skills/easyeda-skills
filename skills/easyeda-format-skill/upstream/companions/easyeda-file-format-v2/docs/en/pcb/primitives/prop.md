# PROP

`PROP` describes optional general-purpose properties of primitives.

## Format

```json
["PROP", "e5", "#22ee44"]
```

## Field Descriptions

1. `PROP`: property identifier.
2. Target primitive ID, in two forms:
   - Regular: `/^[a-z]+\d+$/i`, e.g., `e1`, `e123`.
   - Footprint instance: `/^[a-z]+\d+[a-z]+\d+$/i`, e.g., `e1e5`, `e12e22`.
3. Special color.

## Examples

```json
["PROP", "e5", "#22ee44"]
["PROP", "e7e25", "#22ee44"]
```

To override a primitive inside a footprint, use the compound ID form.
