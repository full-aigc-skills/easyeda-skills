# 多边形体系

SVG 中 `path` 是一个对多边形优秀的抽象。但由于 PCB 内用不到其中相对位置等功能，并且有条件设计更方便解析的方式。所以仿造 SVG 的 `path` 创造了一种类似的表达多边形的方式。

多边形体系内 `POLY`、`REGION`、`POUR` 支持互相转换。

## 目录

- [单多边形的定义](single-polygon.md)
- [复杂多边形的定义](complex-polygon.md)
- [POLY 折线](poly.md)
- [FILL 填充](fill.md)
- [REGION 区域](region.md)
- [POUR 覆铜边框](pour.md)
- [POURED 覆铜结果文档](poured.md)
- [IMAGE 图片](image.md)
- [TEARDROP 泪滴](teardrop.md)
