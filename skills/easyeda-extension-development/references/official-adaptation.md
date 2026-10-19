# .eext 开发的类型驱动流程

该技能整理官方 extension-dev-skill；Agent 插件的 manifest 与 EDA 内部 extension.json 属于不同宿主。创建 Agent 插件不代表已经安装 .eext。

## 证据顺序

1. 目标扩展工程安装的 @jlceda/pro-api-types/index.d.ts 决定 API 结构、mount、重载、参数、返回及枚举。
2. 目标工程 npm run build 验证与已安装 SDK 的编译和打包兼容。
3. 当前声明中的 JSDoc 补充 public/beta/alpha、语义和限制。
4. 官方 recipes 提供流程，guide 提供菜单、i18n 与发布方法。它们不能覆盖当前类型。

## 查询方法

原技能包含 eda-api.js 查询器。本包已携带该脚本及全部配方/资料，但不捆绑 node_modules；直接使用 [包内查询器](bundled-official.md)。它的 --project 必须指向目标扩展工程，依赖解析也来自该工程。

```text
node <已安装官方技能的绝对路径>/scripts/eda-api.js doctor --project <目标工程>
node <已安装官方技能的绝对路径>/scripts/eda-api.js search --project <目标工程> --member <方法>
node <已安装官方技能的绝对路径>/scripts/eda-api.js inspect --project <目标工程> --mount <挂载> --member <方法> --closure
```

查询器缺少 TypeScript 或类型包时应报告环境错误；安装依赖需已有授权。普通 MCP 操作则先用客户端 doc.api，不能假定桌面版本与某个开发工程 SDK 相同。

## 生成与调试

- 对计划调用的 mount/member 查询完整类型闭包；逐项处理重载、联合类型和枚举。
- 排除 private/protected/internal；beta/alpha 标出版本限制。
- 使用 TypeScript、async/await、明确日志标签和有边界的异常处理。
- 运行环境是浏览器沙箱，不能直接使用 Node.js 文件系统与进程接口；自定义 UI 的 IFrame 与宿主消息按 SDK 约定处理。
- 菜单和 i18n 键与 extension.json 对齐；不要修改生成产物来绕过源码错误。
- 构建后在已有授权的测试客户端导入 .eext 并调试；没有实际导入不能声称安装成功。

若要让原生 MCP 调用扩展功能，需设计并暴露可发现的上层接口，再通过 doc.external/functions 验证。只有菜单命令的扩展不自动成为 MCP 工具。
