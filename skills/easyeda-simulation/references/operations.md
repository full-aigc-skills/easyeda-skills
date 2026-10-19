# 操作参考

## 第一个工具调用

调用 tools/list 实际返回的原生 `.help`，参数 `{}`，再查询 `doc.api` 帮助。
本工作流首先查询以下类，具体方法、参数、返回以当前客户端帮助为准：

```json
{"path": "doc.api", "input": {"className": "SCH_SimulationEngine"}}
```

```json
{"path": "doc.api", "input": {"className": "LIB_SimulationModel"}}
```

之后在选定会话中通过原生 `invoke` 执行已查询的 API。涉及扩展时先查询 `doc.external` 或 `functions`，确认上层接口实际存在；未暴露时报告缺口，不把源代码函数名直接当成工具。

## 完成判据

- 没有把启动引擎当成仿真完成。
- 曲线单位、时间和激励正确。
- 结果对应当前电路版本。

## 官方来源

- [easyeda-simulation-engine](https://github.com/easyeda/easyeda-simulation-engine/tree/f06a1dd20b60ea37284ab8033269ddf1212f31af)，修订 `f06a1dd20b60ea37284ab8033269ddf1212f31af`。
  - [README.md](https://github.com/easyeda/easyeda-simulation-engine/blob/f06a1dd20b60ea37284ab8033269ddf1212f31af/README.md)
- [eext-simulation-with-ngspice](https://github.com/easyeda/eext-simulation-with-ngspice/tree/6536f1dac4c44b366777cdb18e344b1603be1ffc)，修订 `6536f1dac4c44b366777cdb18e344b1603be1ffc`。
  - [README.md](https://github.com/easyeda/eext-simulation-with-ngspice/blob/6536f1dac4c44b366777cdb18e344b1603be1ffc/README.md)
- [eext-simulation-with-ltspice](https://github.com/easyeda/eext-simulation-with-ltspice/tree/0fb2afa1816481b50846f55c1c6dbacd5912569b)，修订 `0fb2afa1816481b50846f55c1c6dbacd5912569b`。
  - [README.md](https://github.com/easyeda/eext-simulation-with-ltspice/blob/0fb2afa1816481b50846f55c1c6dbacd5912569b/README.md)
- [eext-simulation-with-simulide](https://github.com/easyeda/eext-simulation-with-simulide/tree/c8eb097e2e87abe80c2235bda2c2d2691fde509e)，修订 `c8eb097e2e87abe80c2235bda2c2d2691fde509e`。
  - [src/index.ts](https://github.com/easyeda/eext-simulation-with-simulide/blob/c8eb097e2e87abe80c2235bda2c2d2691fde509e/src/index.ts)
- [eext-circuitjs1-simulator](https://github.com/easyeda/eext-circuitjs1-simulator/tree/220a62cc30a21a2c2121fb1037e9ba427e64e8d7)，修订 `220a62cc30a21a2c2121fb1037e9ba427e64e8d7`。
  - [src/index.ts](https://github.com/easyeda/eext-circuitjs1-simulator/blob/220a62cc30a21a2c2121fb1037e9ba427e64e8d7/src/index.ts)
- [circuitjs1-easyeda](https://github.com/easyeda/circuitjs1-easyeda/tree/8db75067d81cfcac180edff910716927f89760df)，修订 `8db75067d81cfcac180edff910716927f89760df`。
  - [README.md](https://github.com/easyeda/circuitjs1-easyeda/blob/8db75067d81cfcac180edff910716927f89760df/README.md)

这些链接是固定版本的知识来源，不会自动安装、运行上游扩展。文档/源码证据与真实客户端、板卡、制造验证分开记录。
