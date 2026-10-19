# Project Packaging Structure

## Overview
The "epro" format is the project archive format for the versions V1 and V2 of EasyEDA Pro. Both the online editor and the offline client (which by default uses SQLite files with the eprj suffix for storage) support exporting in a zip archive format.
The project package uses the **zip compression format** for the following advantages:

1. Wide compatibility.
2. Directory structure enables information categorization.
3. Compression enables efficient storage and exchange.

Because zip has limitations (e.g., forbidden filename characters), files are sometimes named with **meaningless IDs**, as long as they correspond to entries in `project.json`.

## .zip File Organization

The project is packaged with the following directory structure:

```text
ROOT
├── project.json              // Project information file with overall structural information
├── SYMBOL/                   // Symbol templates and Block Symbol data
│   ├── symbol-uuid-1       // Schematic library document data; filename corresponds to symbols in project.json
│   ├── symbol-uuid-2
│   └── symbol-uuid-3
├── FOOTPRINT/                // Footprint template data
│   ├── footprint-uuid-1      // PCB library document data; filename corresponds to footprints in project.json
│   ├── footprint-uuid-2
│   └── footprint-uuid-3
├── INSTANCE/                 // Instance attribute documents
│   ├── instance-part-1
│   └── instance-part-2
├── BLOB/                     // Binary data folder
│   ├── blob-hash1
│   └── blob-hash2
├── SHEET/                    // Schematic information folder
│   ├── schematic-uuid-1      // Corresponds to schematics in project.json
│   │   ├── 1                 // SCH document; filename is the Sheet number
│   │   ├── 3
│   │   └── 8
│   └── schematic-uuid-2
│       ├── 1
│       └── 2
├── PCB/                      // PCB document data
│   ├── pcb-uuid-1
│   └── pcb-uuid-2
└── POUR/                     // PCB copper pour result data
    ├── pcb-uuid-1_eid1
    └── pcb-uuid-2_eid2
```

### Notes

- `INSTANCE` contains instance attribute information written in the **INSTANCE attribute document** format. It is recommended to group by the bottom-level sheet in the hierarchy, but other grouping is allowed. Filenames are free and have no critical logical meaning.
- Filenames in the `SHEET` directory (e.g., `1`, `3`, `8`) are Sheet numbers, such as the `8` in `$8I5` in DX.
