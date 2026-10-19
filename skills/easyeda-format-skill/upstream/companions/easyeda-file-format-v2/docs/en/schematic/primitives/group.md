# GROUP

## Format

```json
["GROUP", 1, 0, "Logo", ["e1", "e2"]]
```

## Field Descriptions

1. `GROUP`: grouping identifier.
2. Group ID: cannot be `0`.
3. Parent group ID: `0` means no parent.
4. Group name: empty string `""` when unnamed.
5. Primitive IDs: all primitive IDs belonging to this group.
