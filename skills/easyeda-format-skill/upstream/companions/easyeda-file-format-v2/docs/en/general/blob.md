# Binary Data BLOB

BLOB is used to store binary data in the project, such as images and files.

## Format

```json
["DOCTYPE", "BLOB", "1.0"]
["BLOB", "blob-hash-id1", "aaa.png", "data:image/png;base64,xxsasdfawerwerqwer"]
```

## Field Descriptions

1. `BLOB`: Binary data identifier.
2. `blob-hash-id1`: Binary hash ID.
3. `aaa.png`: Filename, for reference only; may be empty.
4. `data:image/png;base64,...`: Binary data, using a Data URLs-like specification.

## Hash Calculation

1. The final binary data string is encoded with **UTF-8**.
2. Hash is computed with **SHA-256**.
3. The hash is encoded as a lowercase **HEX** string.

## Binary Data Formats

### Common Format

Compatible with Data URLs:

```text
data:[<mediatype>][;base64],<data>
```

Examples:

```text
data:image/png;base64,asdfasdfwer
data:text/html,<html></html>
```

### Extended Format

Extends functionality with encodings such as gzip/deflate:

```text
data:<mediatype>[pipeline],<data>
```

Examples:

```text
data:text/html;gzip;base64,asdfasdf
data:text/css;deflate;aes128;base64,aaaaaaa
```

Decoding proceeds in reverse order of the pipeline.
