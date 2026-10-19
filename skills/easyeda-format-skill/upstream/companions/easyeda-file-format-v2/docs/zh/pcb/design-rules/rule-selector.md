# 规则选择器

## 格式

```json
["RULE_SELECTOR", ["NET", "GND"], 0, {"Safe Clearance": "通用", "Other Clearance": "通用"}]
```

## 字段说明

1. `RULE_SELECTOR`：规则选择器标识。
2. 选择器：
   - `["NET_CLASS", "High Speed"]`：网络类型
   - `["NET", "GND"]`：网络
   - `["LAYER", 3]`：层
   - `["REGION", "e10"]`：区域
   - `["FOOTPRINT", "0805"]`：封装
   - `["COMPONENT", "e100"]`：元件
   - `["POUR", "e100"]`：覆铜
   - `["DIFF_PAIR", "asdf"]`：差分对
   - `["EQ_LEN_GRP", "fdsa"]`：等长对
   - 未来如果要配置逻辑，可以写逻辑 `["AND", ["NET", "GND"], ["LAYER", 5]]`
3. 优先级：数值越小，优先级越高，建议：
   - `0`：元件规则
   - `1`：封装规则
   - `2`：区域规则
   - `3`：网络-网络规则
   - `4`：网络规则
   - `5`：层规则
4. 规则：Key 为规则类，Value 为规则名称，每个规则类下只能选择一个规则。
