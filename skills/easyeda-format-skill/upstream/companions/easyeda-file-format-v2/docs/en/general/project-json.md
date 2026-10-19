# project.json Information File

`project.json` is the core project information file, describing the overall structure, including devices, symbols, footprints, schematics, PCBs, and board configurations.

## Example Structure

```json
{
  "devices": {
    "device-uuid-1": {
      "title": "DV2005",
      "description": "...",
      "tags": [],
      "images": [],
      "attributes": {
        "symbol_uuid": "symbol-uuid-1",
        "footprint_uuid": "footprint-uuid-2",
        "manufacture": "LCSC",
        "value": "10uF"
      }
    }
  },
  "symbols": {
    "symbol-uuid-1": {
      "title": "symbol1",
      "source": "",
      "version": "",
      "type": 17,
      "desc": "TI Memory",
      "tags": ["Memory"]
    }
  },
  "footprints": {
    "footprint-uuid-1": {
      "title": "0805",
      "source": "",
      "version": "",
      "type": 17,
      "desc": "TI Memory",
      "tags": ["Memory"]
    }
  },
  "schematics": {
    "schematic-uuid-1": {
      "name": "Schematic1",
      "sheets": [
        {"id": 1, "name": "1"},
        {"id": 3, "name": "A"},
        {"id": 8, "name": "3"}
      ]
    }
  },
  "pcbs": {
    "pcb-uuid-1": "PCB Title 1",
    "pcb-uuid-2": "AAbbCCd"
  },
  "boards": {
    "Board1": {
      "schematic": "schematic-uuid-1",
      "pcb": "pcb-uuid-1"
    },
    "Board2": {
      "schematic": "schematic-uuid-2"
    }
  },
  "config": {
    "title": "Project3",
    "defaultSheet": "device-uuid-3",
    "cbbProject": false
  }
}
```

## Field Descriptions

### devices

- Key is the device UUID.
- `title`: Device title.
- `description`: Device description.
- `tags`: Tags.
- `images`: Image list.
- `attributes`: Device attributes, may include `symbol_uuid`, `footprint_uuid`, `manufacture`, `value`, etc.

### symbols

- Key is the symbol UUID, corresponding to files in the `SYMBOL` directory.
- `title`: Symbol name.
- `source`: Symbol source. Empty if from the project library.
- `version`: Symbol source version. Empty if from the project library.
- `type`: Symbol type ID.
- `desc`: Symbol description. Empty if not from the project library.
- `tags`: Symbol tags. Empty if not from the project library.

### footprints

- Key is the footprint UUID, corresponding to files in the `FOOTPRINT` directory.
- Fields are similar to `symbols`, corresponding to footprint name, source, version, type ID, description, and tags.

### schematics

- Key is the schematic UUID, matching the folder names under `SHEET`.
- `name`: Schematic name.
- `sheets`: All Sheet information under the schematic, in the same order as displayed in the tree.
  - `id`: Sheet number, matching the filename under the corresponding schematic folder.
  - `name`: Display name of the Sheet.

### pcbs

- Key is the PCB UUID; value is the PCB title.

### boards

- Describes board-level mapping.
- `schematic`: Corresponding schematic UUID.
- `pcb`: Corresponding PCB UUID (optional).

### config

- `title`: Project name.
- `defaultSheet`: Default sheet frame configuration (device UUID).
- `cbbProject`: Whether it is a CBB project. If true, basic CBB requirements are checked on import.
