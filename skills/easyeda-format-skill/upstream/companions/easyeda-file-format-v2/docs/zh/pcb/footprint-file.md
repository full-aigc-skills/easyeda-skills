# FOOTPRINT 文件格式

`FOOTPRINT` 和 `PCB` 基本一致，就是能采用的图元有限。具体能采用什么图元看需求，格式内不做太多限制。

除了绝对不应存在 `DEVICE`、`FOOTPRINT`、`COMPONENT` 图元，封装不应调用封装产生递归定义。

## 文件头

```json
["DOCTYPE", "FOOTPRINT", "1.0"]
["HEAD", {"editorVersion": "4.7.8", "importFlag": 0}]
["CANVAS", 0, 0, "mm", 10, 10]
["LAYER", 0, "TOP", "Top Layer", 1, "#FF0000", 0.5, "#880000", 0.3]
```

## 主体示例

```json
["PAD", "e100", 1, "GND", 0, "1", 100, 200, 15, [], [], [[0, 1, []]], 10, -5, 30, 1, 0, null, 0.5, 0.4, null, 0]
```
