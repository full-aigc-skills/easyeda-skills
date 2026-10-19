English | [中文](#中文)

# EasyEDA Pro V2 File Format Specification

> Technical documentation describing the project file format for EasyEDA Pro V2.

## Introduction

This project compiles the complete specification of the EasyEDA Pro V2 project file format, including:

- Project packaging structure
- Common file header format
- Schematic file format
- PCB file format
- Extensions such as 3D shell, design rules, and panelization

>"Note": Since version 3, the EasyEDA Pro version has stopped using the file format of version 2, but it still supports importing and exporting files in version 2 format (with some differences in details). Developers are recommended to use version 3 format for development.  
> "Note": The latest file format of EasyEDA Pro please reference at https://github.com/easyeda/easyeda-format-skill

The "epro" format is the project archive format for the versions V1 and V2 of EasyEDA Pro. Both the online editor and the offline client (which by default uses SQLite files with the eprj suffix for storage) support exporting in a zip archive format.
The project package uses the **zip compression format** for the following advantages:

## Documentation Structure

- [中文文档](docs/zh/README.md)
- [English Documentation](docs/en/README.md)
- [Original PDF Documents](docs/)
  - `嘉立创EDA专业版V2文件格式 - 通用部分.pdf`
  - `嘉立创EDA专业版V2文件格式 - 原理图部分.pdf`
  - `嘉立创EDA专业版V2文件格式 - PCB部分.pdf`

## Examples

An example project is provided. See [Example Documentation](docs/en/examples/index.md) for details.

## License

The documentation in this project is provided for reference and educational purposes only.

中文 | [English](#English)

#中文

# 嘉立创EDA专业版V2文件格式说明

> 描述嘉立创EDA专业版（EasyEDA Pro）V2 工程文件格式的技术文档。

## 简介

本项目整理了嘉立创EDA专业版V2工程文件格式的完整规范，包括：

- 工程打包结构
- 通用文件头格式
- 原理图文件格式
- PCB文件格式
- 3D外壳、设计规则、拼版等扩展格式

> "提示"：嘉立创EDA专业版从 V3 开始已经不再使用 V2 的文件格式，当仍支持 V2 格式的导入和导出（会有细节差异），建议开发者使用最新版本V3格式开发。   
> "提示"：最新版本的嘉立创EDA专业版文档格式说明请参考：https://github.com/easyeda/easyeda-format-skill

“epro”格式是嘉立创EDA专业版V1与V2版本的工程归档格式，在线版编辑器和离线客户端（离线客户端默认使用eprj后缀的SQLite文件存储）均支持导出，是一个zip压缩包。

## 文档结构

- [中文文档](docs/zh/README.md)
- [English Documentation](docs/en/README.md)
- [PDF 原始文档](docs/)
  - `嘉立创EDA专业版V2文件格式 - 通用部分.pdf`
  - `嘉立创EDA专业版V2文件格式 - 原理图部分.pdf`
  - `嘉立创EDA专业版V2文件格式 - PCB部分.pdf`

## 示例

项目提供了示例工程文件，详情请参阅 [示例说明](docs/zh/examples/index.md)。

## 许可证

本项目文档仅供参考学习使用。
