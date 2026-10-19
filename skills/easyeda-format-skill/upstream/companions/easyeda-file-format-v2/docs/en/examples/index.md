# Example Project

This repository provides an example project file `examples/easyeda-pro-v2.2-format-example.epro`. After extracting, you can see its internal structure.

## Example Project Structure

```text
easyeda-pro-v2.2-format-example/
└── project.json
```

All core information of the example project is stored in `project.json`. Below is an explanation of the main fields.

## project.json Description

### schematics

```json
{
  "schematics": {
    "324ebe00d3ad4f43b364b3e0db4c5cb8": {
      "name": "Schematic1",
      "sheets": [
        {"name": "P1", "id": 1, "uuid": "aa1ebc2929054073a8a7cdad9451d85b"},
        {"name": "P2", "id": 2, "uuid": "7b9a481ef7e74ab98ad1d58f32a39af2"}
      ]
    },
    "e204390255ac4eba973d82b97125a470": {
      "name": "Schematic2",
      "sheets": [
        {"name": "P1", "id": 1, "uuid": "7eb4d82ca41542fdb29dd5a5ae2f4479"}
      ]
    }
  }
}
```

- Key is the schematic UUID.
- `name`: schematic name, e.g., `Schematic1`, `Schematic2`.
- `sheets`: list of sheets under the schematic.
  - `name`: sheet display name.
  - `id`: sheet number.
  - `uuid`: sheet unique identifier.

### pcbs

```json
{
  "pcbs": {
    "21bf3cb7badf4afaad0dd41b43ce6d3b": "PCB1",
    "de0a8ca498fb4cf7ba7cff4f6a30e115": "PCB2"
  }
}
```

- Key is the PCB UUID.
- Value is the PCB title.

### panels

```json
{
  "panels": {
    "5e182b6d5b48426fad374255e5efd1dc": "Panel_1"
  }
}
```

- Key is the panel UUID.
- Value is the panel name.

### symbols

```json
{
  "symbols": {
    "6644fff3ec4746afad9f4bc9616a8eee": {
      "source": "dae013dc9fb24993ad62a51f9f80d9cd|0819f05c4eef4c71ace90d822a990e87",
      "desc": "",
      "tags": {"parent_tag": [], "child_tag": []},
      "custom_tags": "["特殊器件"]",
      "title": "Drawing-Symbol_A4",
      "version": "1763433565736",
      "type": 20
    }
  }
}
```

- Key is the symbol UUID.
- `source`: symbol source, composed of two parts separated by `|`.
- `desc`: symbol description.
- `tags`: classification tags, including `parent_tag` and `child_tag`.
- `custom_tags`: custom tags, stored as a JSON string.
- `title`: symbol title.
- `version`: version number.
- `type`: symbol type number.

### footprints

```json
{
  "footprints": {
    "7e30682893f74f5f9297a8d0e547deba": {
      "title": "R0603",
      "source": "50b4943912284dab97752312e589e9e2|0819f05c4eef4c71ace90d822a990e87",
      "version": "1766479705",
      "type": 4,
      "desc": "0603;...",
      "tags": {"parent_tag": [], "child_tag": []},
      "custom_tags": "["RES-SMD"]"
    }
  }
}
```

- Key is the footprint UUID.
- `title`: footprint title, e.g., `R0603`.
- `source`: footprint source.
- `version`: version number.
- `type`: footprint type number.
- `desc`: footprint description, usually containing multiple searchable keywords.
- `tags` and `custom_tags`: classification tags.

### devices

```json
{
  "devices": {
    "9bb222e758404bf989041750f60ffeef": {
      "title": "Drawing-Symbol_A4",
      "attributes": {
        "Symbol": "6644fff3ec4746afad9f4bc9616a8eee",
        "Page Size": "A4",
        "Size": "A4",
        "Width": "1170",
        "Height": "825"
      },
      "description": "",
      "tags": {"parent_tag": [], "child_tag": []},
      "images": [""],
      "source": "bc676184ec9748d7b372ad543982403a|0819f05c4eef4c71ace90d822a990e87",
      "version": "1763386843",
      "custom_tags": [""]
    }
  }
}
```

- Key is the device UUID.
- `title`: device title.
- `attributes`: device attributes, which may include:
  - `Symbol`: bound symbol UUID.
  - `Footprint`: bound footprint UUID.
  - `3D Model`: 3D model UUID.
  - `Designator`: designator.
  - `Value`: value.
  - `Name`: name.
- `description`: device description.
- `tags`: classification tags.
- `images`: image list.
- `source`: source.
- `version`: version number.
- `custom_tags`: custom tags.

### boards

```json
{
  "boards": {
    "Board1": {
      "schematic": "324ebe00d3ad4f43b364b3e0db4c5cb8",
      "pcb": "21bf3cb7badf4afaad0dd41b43ce6d3b"
    },
    "Board2": {
      "schematic": "e204390255ac4eba973d82b97125a470",
      "pcb": "de0a8ca498fb4cf7ba7cff4f6a30e115"
    }
  }
}
```

- Key is the board name, e.g., `Board1`, `Board2`.
- `schematic`: associated schematic UUID.
- `pcb`: associated PCB UUID.

### config

```json
{
  "config": {
    "title": "easyeda-pro-v2.2-format-example",
    "cbbProject": false,
    "defaultSheet": "9bb222e758404bf989041750f60ffeef",
    "editorVersion": "2.2.48.10"
  }
}
```

- `title`: project title.
- `cbbProject`: whether this is a CBB project.
- `defaultSheet`: UUID of the default sheet device.
- `editorVersion`: editor version.

## Summary

The example project shows how `project.json` organizes a project with multiple schematics and PCBs. In actual projects, `project.json` only stores structural information, while the specific primitive data is stored in files under directories such as `SYMBOL`, `FOOTPRINT`, `SHEET`, and `PCB`.
