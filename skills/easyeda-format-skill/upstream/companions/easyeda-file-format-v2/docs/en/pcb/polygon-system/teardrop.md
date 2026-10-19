# TEARDROP Teardrop

Teardrops cannot be selected or directly manipulated. When any associated primitive changes, the EDA tool should automatically remove them.

## Format

```json
["TEARDROP", "e200", "GND", 3, <single polygon>, 0]
```

## Field Descriptions

1. `TEARDROP`: teardrop identifier.
2. ID.
3. Net.
4. Layer.
5. Single polygon.
6. Group ID: `0` no group, non-`0` group marker.
