# Panelization

## PANELIZE

```json
["PANELIZE", 1, 2, 3, 5.5, 6.1, 1]
```

### Field Descriptions

1. `PANELIZE`: panelization identifier.
2. Whether enabled.
3. Number of rows.
4. Number of columns.
5. Row spacing.
6. Column spacing.
7. Whether to panelize only the outline.

## PANELIZE_STAMP

```json
["PANELIZE_STAMP", 1, 1, 3, 8, 0.1]
```

### Field Descriptions

1. `PANELIZE_STAMP`: stamp hole parameter identifier.
2. Direction: `0` horizontal, `1` vertical.
3. Whether enabled (if not, V-CUT is used).
4. Number of stamp hole groups.
5. Stamp hole diameter.
6. Number of stamp holes per group.
7. Stamp hole spacing.

## PANELIZE_SIDE

```json
["PANELIZE_SIDE", 0, 1, 5, 3, 2, 1]
```

### Field Descriptions

1. `PANELIZE_SIDE`: process edge parameter identifier.
2. Direction: `0` horizontal, `1` vertical.
3. Whether enabled (if not, no process edge is used).
4. Process edge height.
5. Positioning hole diameter (`0` means none).
6. Mark point diameter (`0` means disabled).
7. Mark point solder mask expansion.
