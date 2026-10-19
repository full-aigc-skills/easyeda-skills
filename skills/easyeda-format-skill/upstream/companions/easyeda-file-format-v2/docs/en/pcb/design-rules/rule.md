# Design Rule

## Format

```json
["RULE", "Safe Clearance", "General", 1, {unit: "mm", xxxxx}]
```

## Field Descriptions

1. `RULE`: design rule identifier.
2. Rule type: determined by the EDA tool.
3. Rule name.
4. Rule state: `0` normal, `1` default, `2` disabled.
5. Rule content: determined by the EDA tool.

Rules of the same type should appear in the same order as the left tree in the rule manager.
