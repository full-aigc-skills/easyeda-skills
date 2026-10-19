# Document Conventions

This chapter introduces the general conventions used in the EasyEDA Pro V2 file format.

## Primitive Structure Array

- The file is line-oriented; each line is a valid JSON array, called a **primitive structure array**.
- Unless otherwise specified, every element in the primitive structure array has a fixed position. The same element will not be placed in different positions depending on the situation (except for cross-version compatibility).

## Direction and Units

- Rotation angles are positive in the counter-clockwise direction, using degrees.
- Unless otherwise specified, all coordinates, lengths, and sizes use **0.01 inch** as the unit.

## Unique IDs

- Almost every primitive must have a unique ID within the file.
- Almost every primitive has a lock parameter. A locked primitive behaves as follows in the editor:
  1. Cannot be dragged.
  2. Cannot be deleted.
  3. Cannot be resized with the mouse or keyboard.
  4. Cannot have its shape changed with the mouse or keyboard.

## Colors

- All colors are expressed as `"#RRGGBB"`. To indicate no color (fully transparent), use `""`.

## Block-level Primitives

- All primitives with scope, such as `PART`, and the file itself, are called **block-level primitives**.

## Boolean Encoding

- All attributes described as "whether XXXX" use `1` for yes and `0` for no.

## Sequences and Key-Value Pairs

- `[xxx, xxx, xxx, xxx]` denotes a sequence.
- `{"KEY": "VALUE", "_kEy": "@vAlUe"}` denotes a key-value pair. Except for keys explicitly marked as reserved, others can be freely set for special tool scenarios.

## JSON Standard

- Parts not explicitly described in this convention (such as escaping) follow RFC 7195 "The JavaScript Object Notation (JSON) Data Interchange Format".
