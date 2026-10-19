# OBJ

Embeds images and files into the page for download or direct display.

## Format

```json
["OBJ", "e662", 0, 15, "a.png", 200, 300, 10, 20, 0, 1, "blob:1234ade2f", 1]
```

## Field Descriptions

1. `OBJ`: binary embedded object identifier.
2. Primitive ID.
3. Group ID: `0` no group, non-`0` group marker.
4. Layer.
5. Filename.
6. Top-left X.
7. Top-left Y.
8. Width.
9. Height.
10. Rotation angle, around the top-left corner.
11. Whether the original image is mirrored horizontally around its BBox center.
12. Binary data:
    - Common format, compatible with Data URLs: `data:[<mediatype>][;base64],<data>`
    - BLOB reference format: `blob:hashid`
13. Locked.
14. BBox (optional).
