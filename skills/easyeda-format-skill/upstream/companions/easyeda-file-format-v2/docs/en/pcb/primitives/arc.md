# ARC/CARC

Arcs follow Eagle's mathematical model, described by start and end points.

- `ARC`: two-point interaction mode.
- `CARC`: center arc interaction mode.

## Format

```json
["ARC", "e100", 3, "GND", 1, 100, 200, 300, 400, -170, 10, 0]
```

## Field Descriptions

1. Arc identifier: `ARC` or `CARC`.
2. Primitive ID.
3. Group ID: `0` no group, non-`0` group marker.
4. Net.
5. Layer.
6. Start X.
7. Start Y.
8. End X.
9. End Y.
10. Arc angle: positive counter-clockwise, negative clockwise.
11. Width.
12. Locked.
