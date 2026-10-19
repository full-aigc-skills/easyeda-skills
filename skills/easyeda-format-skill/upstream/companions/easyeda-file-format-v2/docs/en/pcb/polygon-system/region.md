# REGION Region

Keepout regions are important for both manual design and automated placement and routing, providing automated tools with area constraints in addition to design rules.

## Format

```json
["REGION", "e100", 5, 3, 1, [1, 2, 5], <complex polygon>, 0]
```

## Field Descriptions

1. `REGION`: region identifier.
2. Primitive ID.
3. Group ID: `0` no group, non-`0` group marker.
4. Layer.
5. Line width.
6. Keepout types; multiple can exist at the same time:
   - `1`: keepout traces and fills (deprecated, but keep compatible)
   - `2`: keepout components
   - `3`: keepout vias
   - `4`: keepout copper pour and internal plane (deprecated, but keep compatible)
   - `5`: keepout traces
   - `6`: keepout fills
   - `7`: keepout copper pour
   - `8`: keepout internal plane
7. See Complex Polygon chapter.
8. Locked.
