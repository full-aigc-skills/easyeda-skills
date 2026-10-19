# PCB 文件格式

## 文件头

```json
["DOCTYPE", "PCB", "1.0"]
["HEAD", {"editorVersion": "4.7.8", "importFlag": 0}]
["CANVAS", 0, 0, "mm", 10, 10]
["LAYER", 0, "TOP", "Top Layer", 1, "#FF0000", 0.5, "#880000", 0.3]
```

## 主体示例

```json
["LINE", "e100", 1, "GND", 1, 100, 200, 400, 300, 0.7, 0]
["ARC", "e100", 3, "GND", 1, 100, 200, 300, 400, -170, 10, 0]
["VIA", "e100", 0, "GND", "asdf", 100, 200, 5, 9, 0, null, null, null, null, 0]
```

PCB 主体由一系列基础图元组成，包括 `NET`、`PRIMITIVE`、`GROUP`、`SILK_OPTS`、`PREFERENCE`、`CONNECT`、`VIA`、`PAD`、`LINE`、`ARC`、`OBJ`、`ITEM_ORDER`、`PROP`、`EQLEN_GRP`、`EQLEN` 等。
