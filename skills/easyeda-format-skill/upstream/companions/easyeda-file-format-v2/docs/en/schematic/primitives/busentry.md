# BUSENTRY

`BUSENTRY` represents a branch access point of a bus.

## Description

- Light yellow represents the `BUS`.
- The green rounded diamond and the pin-like shape extending to its right are `BUSENTRY`.
- Blue represents the `Wire`.
- The endpoint is the coordinate where the `WIRE` and the rightmost endpoint-like point of `BUSENTRY` meet.
- Because `WIRE` and `BUS` can connect at any angle, the rotation direction must be specified to match the `WIRE` approach direction (e.g., 180 degrees in diagrams).
- `BUSENTRY` has a fixed one-grid length.
- The exact shape of `BUSENTRY` is interpreted by XTools and is not constrained by the format.

## Format

```json
["BUSENTRY", "e380", "e271", 4, 500, 600, 90]
```

## Field Descriptions

1. `BUSENTRY`: primitive name.
2. ID: unique within the file.
3. Parent ID: the `BUS` it belongs to.
4. Sequence number: within the parent `BUS`, can repeat.
   - For example, if the bus net is `A[2:3]B[7:6]`, a series of `BUSENTRY` sequence numbers `0 1 2 3 0 1 2 3 …` can exist, where:
     - `0` represents branch `A2B7`
     - `1` represents branch `A2B6`
     - `2` represents branch `A3B7`
     - `3` represents branch `A3B6`
5. Endpoint X.
6. Endpoint Y.
7. Rotation angle: around the endpoint.
