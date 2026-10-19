# CONNECT

`CONNECT` expresses internal grouping logic of primitives, such as:

- Teardrop connections to LINE, ARC, PAD, and VIA.
- Pad connections to pin 3D outlines and FILL.
- 3D shell connections between CREASE, BOSS, and SHELL_ENTITY.
- Footprint internal primitive overrides in PCB.

Only one-to-many relationships are expressed. Many-to-many relationships can use multiple `CONNECT` primitives.

## Format

```json
["CONNECT", "e3", ["e15", "e18", "e100"]]
```

## Field Descriptions

1. `CONNECT`: connection identifier.
2. Master primitive.
3. Associated primitive IDs.

## Examples

```json
["CONNECT", "e4", ["e5", "e6"]]
["CONNECT", "e5", ["e4", "e6"]]
["CONNECT", "e6", ["e4", "e5"]]
```

## Footprint Internal Override

PCB references primitives inside footprints using the form `/^[a-z]+\d+[a-z]+\d+$/i`, combining the footprint and inner primitive IDs.

Example:

```json
["DOCTYPE", "PCB", "1.0"]
["COMPONENT", "e13", 5, 1, ...]
["VIA", "e13e20", 0, "GND", "asdf", ....]
["PAD", "e13e25", 1, "GND", 0, "1", ....]
["CONNECT", "e13", ["e13e20", "e13e25"]]
```
