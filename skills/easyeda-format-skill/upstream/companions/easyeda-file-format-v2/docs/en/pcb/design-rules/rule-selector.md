# Rule Selector

## Format

```json
["RULE_SELECTOR", ["NET", "GND"], 0, {"Safe Clearance": "General", "Other Clearance": "General"}]
```

## Field Descriptions

1. `RULE_SELECTOR`: rule selector identifier.
2. Selector:
   - `["NET_CLASS", "High Speed"]`: net class
   - `["NET", "GND"]`: net
   - `["LAYER", 3]`: layer
   - `["REGION", "e10"]`: region
   - `["FOOTPRINT", "0805"]`: footprint
   - `["COMPONENT", "e100"]`: component
   - `["POUR", "e100"]`: copper pour
   - `["DIFF_PAIR", "asdf"]`: differential pair
   - `["EQ_LEN_GRP", "fdsa"]`: equal-length group
   - Future logic can be expressed as `["AND", ["NET", "GND"], ["LAYER", 5]]`
3. Priority: smaller numbers are higher priority. Recommended:
   - `0`: component rule
   - `1`: footprint rule
   - `2`: region rule
   - `3`: net-to-net rule
   - `4`: net rule
   - `5`: layer rule
4. Rules: Key is the rule class, Value is the rule name; only one rule can be selected per rule class.
