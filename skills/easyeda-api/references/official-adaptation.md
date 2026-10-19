# 官方 API 技能的原生 MCP 适配

原技能通过独立 HTTP/WebSocket Bridge 执行 JavaScript；本包使用客户端原生 `invoke`，保留对象操作与校验方法。Bridge 的端口发现、握手和窗口 ID 不能直接搬到原生协议。

## 执行环境

- `eda` 来自编辑器扩展上下文，不从 `window.parent` 获取。浏览器沙箱不支持 Node.js 的 require、fs、process。
- 返回 Promise 的调用需要 await；返回原语对象时先提取需要的状态，避免跨进程丢失原型方法。
- 图元修改通常采用读取 → toAsync → setState_* → await done 的模式；具体重载和返回类型由当前 `doc.api` 决定，不假定所有 get 都返回单个对象。
- Layer、线型、方向等参数需先查询枚举，不能凭数字记忆猜值。
- 原理图 API 坐标通常每单位 10mil，PCB 通常每单位 1mil；直接文件格式与脚本可能另有约定。

## 最小只读探查

1. `doctor` 与 `session.list` 识别客户端和唯一目标窗口。
2. 读取 `dmt_Project.getCurrentProjectInfo` 和 `dmt_SelectControl.getCurrentDocumentInfo`。
3. 按文档类型查询 sch_* 或 pcb_*；当前图页不匹配时停止写入。
4. 按 ID 读取对象并提取位号、引脚、坐标，之后再生成修改参数。

## 工程切换与回读

`openProject` 可能影响当前未保存工作；只读请求不得顺便打开工程。用户已授权修改时也应先识别当前保存状态。`invoke` 的传输成功、API 返回值、对象实际变化分别判断。网络或执行超时后先按 ID 回读，避免重复创建。

## IFrame 与扩展

IFrame 与宿主的数据交换使用目标版本提供的消息接口；不要把复杂原型对象直接跨边界传递。外部扩展必须先发现其真实上层接口。完整声明、源码格式和例程按本目录 operations.md 中固定修订链接渐进读取。
