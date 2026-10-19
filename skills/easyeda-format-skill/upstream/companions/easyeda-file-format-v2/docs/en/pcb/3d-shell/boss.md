# BOSS Boss

A `BOSS` associated with `CREASE` via `CONNECT` adds a side boss.

## Format

```json
["BOSS", "e36", 0, 50, 100, 200, 100, "M2", 10, 20, [100, 20], [20, 40, 20, 10], 0]
```

## Field Descriptions

1. `BOSS`: boss identifier.
2. Primitive ID.
3. Group ID: `0` no group, non-`0` group marker.
4. Layer number.
5. Center X.
6. Center Y.
7. Screw model: `"M2"`, `"M3"`, etc., or `null` for custom.
8. Boss height.
9. Boss wall thickness.
10. Boss through-hole diameter.
11. Countersink parameters; `null` means no countersunk head.
    - screw head height
    - screw head diameter
12. Rib parameters; `null` means no ribs.
    - rib top width
    - rib bottom width    - rib distance from top of boss
    - rib thickness
13. Locked.

## Example

```json
["BOSS", "e36", 0, 50, 100, 200, 100, null, 10, 20, [100, 20], [20, 40, 20, 10], 0]
```
