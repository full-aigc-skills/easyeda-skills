# Design Rule Template

There are two conceptual ways to understand the design rule template; the PCB editor chooses as needed:

1. As the base version of other design rules, where other rules override the template.
2. Mutually exclusive with other design rules; when a template exists, other rules are only temporary and have no effect.
3. As an indicator of which template the rules originate from, without affecting the actual effect of subsequent rules (currently adopted).

## Format

```json
["RULE_TEMPLATE", "JLCPCB Capability(High Frequency Board)"]
```

## Field Descriptions

1. `RULE_TEMPLATE`: design rule template identifier.
2. Template name.
