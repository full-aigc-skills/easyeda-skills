# COMPONENT Component Instance

## Format

```json
["COMPONENT", "e8", 5, 1, 150, 200, 45, {"3D Model": "uuid", "3D Model Transform": "20,10,0,0,15,45,0,0,20"}, 0]
```

## Field Descriptions

1. `COMPONENT`: instance identifier.
2. Primitive ID.
3. Group ID: `0` no group, non-`0` group marker.
4. Layer (only top or bottom).
5. Position X.
6. Position Y.
7. Rotation angle.
8. Custom properties.
9. Locked.

## Custom Properties

- Fixed `3D Model` is the UUID of the 3D model; this UUID refers to a record with doctype = 16 in the components table.
- Fixed `3D Model Transform` is the 3D model transformation parameters.

## Attribute Examples

```json
["ATTR", "e102", 0, "e8", 1, "Designator", "U1", 0, 1, "SimSun", 50, 10, 0, 0, 0, 1, 2, 15, 1, 1]
["ATTR", "e103", 0, "e8", 1, "Footprint", "footprint-uuid", 0, 1, "SimSun", 50, 10, 0, 0, 0, 1, 2, 15, 1, 1]
["ATTR", "e104", 0, "e8", 1, "Device", "device-uuid", 0, 1, "SimSun", 50, 10, 0, 0, 0, 1, 2, 15, 1, 1]
```

## PAD_NET

```json
["PAD_NET", "e8", "a1", "GND", "e125"]
```

1. `PAD_NET`: pad instance net mapping identifier.
2. Parent component instance ID.
3. Pad number.
4. Net name.
5. Footprint internal pad ID (optional).

## REUSE_BLOCK

```json
["REUSE_BLOCK", "e8", "$1e16", "$2e5_$4e3"]
```

1. `REUSE_BLOCK`: reuse block information identifier.
2. Parent component instance ID.
3. Group ID.
4. Channel ID.
