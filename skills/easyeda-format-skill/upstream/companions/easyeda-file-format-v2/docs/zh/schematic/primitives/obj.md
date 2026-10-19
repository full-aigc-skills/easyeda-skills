# OBJ 二进制内嵌对象

内嵌于图页上的图片和文件等数据，可作为附件下载，以及直接显示（EDA 自行决定，不在格式内要求）。

## 格式

```json
["OBJ", "e662", "a.txt", 200, 300, 10, 20, 0, 0, "data:text/plain;base64,MTIzNA==", 1]
```

## 字段说明

1. `OBJ`：二进制内嵌对象标识。
2. 编号：文件内唯一。
3. 文件名。
4. 左上角 X。
5. 左上角 Y。
6. 宽。
7. 高。
8. 旋转角度：绕左上角旋转。
9. 是否镜像。
10. 二进制数据，有两种模式：
    - 一般格式，遵循 Data URLs 规范：`data:[<mediatype>][;base64],<data>`
    - BLOB 引用模式：`blob:hashid`
11. 是否锁定。

## 示例

```json
["OBJ", "e662", "a.txt", 200, 300, 10, 20, 0, 0, "data:text/plain;base64,MTIzNA==", 1]
["OBJ", "e663", "b.svg", 200, 300, 100, 200, 15, 1, "data:image/svg+xml;base64,PHN2Zz48L3N2Zz4=", 1]
```
