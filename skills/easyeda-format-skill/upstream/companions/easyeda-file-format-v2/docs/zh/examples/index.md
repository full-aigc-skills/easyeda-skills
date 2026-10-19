# 示例工程

本仓库提供了一个示例工程文件 `examples/easyeda-pro-v2.2-format-example.epro`，解压后可以看到其内部结构。

## 示例工程结构

```text
easyeda-pro-v2.2-format-example/
└── project.json
```

示例工程的核心信息全部保存在 `project.json` 中，下面是对 `project.json` 主要字段的说明。

## project.json 说明

### schematics（原理图）

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

- 键为原理图 UUID。
- `name`：原理图名称，例如 `Schematic1`、`Schematic2`。
- `sheets`：该原理图下的 Sheet 列表。
  - `name`：Sheet 显示名称。
  - `id`：Sheet 编号。
  - `uuid`：Sheet 的唯一标识。

### pcbs（PCB）

```json
{
  "pcbs": {
    "21bf3cb7badf4afaad0dd41b43ce6d3b": "PCB1",
    "de0a8ca498fb4cf7ba7cff4f6a30e115": "PCB2"
  }
}
```

- 键为 PCB UUID。
- 值为 PCB 标题。

### panels（面板）

```json
{
  "panels": {
    "5e182b6d5b48426fad374255e5efd1dc": "Panel_1"
  }
}
```

- 键为面板 UUID。
- 值为面板名称。

### symbols（符号）

```json
{
  "symbols": {
    "6644fff3ec4746afad9f4bc9616a8eee": {
      "source": "dae013dc9fb24993ad62a51f9f80d9cd|0819f05c4eef4c71ace90d822a990e87",
      "desc": "",
      "tags": {"parent_tag": [], "child_tag": []},
      "custom_tags": "[\"特殊器件\"]",
      "title": "Drawing-Symbol_A4",
      "version": "1763433565736",
      "type": 20
    }
  }
}
```

- 键为符号 UUID。
- `source`：符号来源，由两部分组成，用 `|` 分隔。
- `desc`：符号描述。
- `tags`：分类标签，包含 `parent_tag` 和 `child_tag`。
- `custom_tags`：自定义标签，以 JSON 字符串形式保存。
- `title`：符号标题。
- `version`：版本号。
- `type`：符号类型编号。

### footprints（封装）

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
      "custom_tags": "[\"RES-SMD\"]"
    }
  }
}
```

- 键为封装 UUID。
- `title`：封装标题，例如 `R0603`。
- `source`：封装来源。
- `version`：版本号。
- `type`：封装类型编号。
- `desc`：封装描述，通常包含多个可搜索的关键字。
- `tags` 和 `custom_tags`：分类标签。

### devices（器件）

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

- 键为器件 UUID。
- `title`：器件标题。
- `attributes`：器件属性，可能包括：
  - `Symbol`：绑定的符号 UUID。
  - `Footprint`：绑定的封装 UUID。
  - `3D Model`：3D 模型 UUID。
  - `Designator`：位号。
  - `Value`：值。
  - `Name`：名称。
- `description`：器件描述。
- `tags`：分类标签。
- `images`：图片列表。
- `source`：来源。
- `version`：版本号。
- `custom_tags`：自定义标签。

### boards（板子）

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

- 键为板子名称，例如 `Board1`、`Board2`。
- `schematic`：关联的原理图 UUID。
- `pcb`：关联的 PCB UUID。

### config（配置）

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

- `title`：工程标题。
- `cbbProject`：是否为 CBB 工程。
- `defaultSheet`：默认图框对应的器件 UUID。
- `editorVersion`：编辑器版本。

## 总结

示例工程展示了 `project.json` 如何组织一个多原理图、多 PCB 的工程。实际工程中，`project.json` 仅保存结构性信息，而具体的图元数据则分别存储在 `SYMBOL`、`FOOTPRINT`、`SHEET`、`PCB` 等目录下的文件中。
