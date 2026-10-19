# 本地 .eext 的实际调用

内部扩展名 easyeda-mcp；命名空间 external.easyedaMcp。通过客户端原生 MCP 调用，不依赖外部 Python 服务。

```json
{"path":"invoke","input":{"session":"实际会话ID","extUuid":"b0f54bac131848dab885c8215a0ac81c","code":"return await external.easyedaMcp.inspectProject({});","timeout":15000}}
```

原生 doc.external 在本机主页 render 返回 BRIDGE_NOT_READY，但以下只读查询可以发现全部接口：

```json
{"path":"invoke","input":{"session":"实际会话ID","extUuid":"b0f54bac131848dab885c8215a0ac81c","code":"return await eda.sys_Help.help('external','easyedaMcp');","timeout":15000}}
```

14 个接口为 getCapabilities、inspectProject、searchDevices、listComponents、getPins、getNetlist、checkDrc、placeSchematicComponents、connectPins、placePcbComponents、autoLayout、autoRoute、saveDocument、exportManufacturing。实时帮助可查看参数。

工程读取区分 no_project、project_only、read；工程已打开而未激活图页时不要误报工程不存在。实际修改需要用户在扩展菜单中开启本次会话的修改模式。保留先前只读授权范围，不因读取技能就开启修改或外部交互权限。

修改与读取图页的请求使用 projectUuid、documentUuid。连接引脚使用真实 primitiveId、pinNumber 与 netName；默认路径是简单正交线，需核对交叉和网表。自动布局/布线保留返回值，检查失败网络后再做 DRC。

exportManufacturing 格式为 gerber、bom、pickAndPlace；delivery 支持 base64（宿主保存）、dialog（仅报告下载请求）、filesystem（明确绝对输出目录）。文件系统写入 force=false，成功后逐字节回读，但制造正确性仍需预览。单文件上限 10MiB。

接口可能返回三层状态：MCP isError、原生命令 ok/data、领域接口 ok/data/error。批次失败的 error.partial 需要先核对，不能重复整批写入。

工程信息 API 若挂起，扩展 1500ms 后仅对只读方法使用活动图页 parentProjectUuid，返回 projectInfoSource=active_document 和 warnings。此时工程名称可能缺失，不能猜测；写入和保存仍要求完整工程信息。

实测：面板/RPC 与外部接口必须使用同一真实 extUuid；省略时独立脚本上下文会看不到已确认的写入模式。先从 functions 核对 UUID，不能使用内置 eda 身份冒充。完整 LED 独立测试已验证放置、连线、同步 PCB、布局布线与导出，但不代表任意电路均可自动完成。

本机 BOM 与贴片坐标原始 .csv 为 UTF-16LE BOM、TAB 分隔。按 BOM 检测编码和分隔符；转换时保留原字节文件，不把文件扩展名当作格式证明。
