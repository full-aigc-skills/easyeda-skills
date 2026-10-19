# OBJ

Embeds images and files onto the page; they can be downloaded as attachments or displayed directly (determined by the EDA tool).

## Format

```json
["OBJ", "e662", "a.txt", 200, 300, 10, 20, 0, 0, "data:text/plain;base64,MTIzNA==", 1]
```

## Field Descriptions

1. `OBJ`: binary embedded object identifier.
2. ID: unique within the file.
3. Filename.
4. Top-left X.
5. Top-left Y.
6. Width.
7. Height.
8. Rotation angle, around the top-left corner.
9. Whether mirrored.
10. Binary data, in one of two modes:
    - Common format, following Data URLs: `data:[<mediatype>][;base64],<data>`
    - BLOB reference mode: `blob:hashid`
11. Locked.

## Examples

```json
["OBJ", "e662", "a.txt", 200, 300, 10, 20, 0, 0, "data:text/plain;base64,MTIzNA==", 1]
["OBJ", "e663", "b.svg", 200, 300, 100, 200, 15, 1, "data:image/svg+xml;base64,PHN2Zz48L3N2Zz4=", 1]
```
