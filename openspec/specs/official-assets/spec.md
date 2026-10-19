# official-assets Specification

## Purpose
保证官方技能、脚本、Schema 与参考资料以固定修订自包含分发，继续使用内置 MCP，并能在实际 Codex 安装后验证资源与工具。

## Requirements

### Requirement: Complete traceable official assets
The package SHALL carry the tracked files of all five pinned official skills and their declared format references with original bytes and per-file provenance.

#### Scenario: Cold installation
- **WHEN** a user installs the package without the source checkout
- **THEN** official instructions, scripts, schemas, examples, and reference documents resolve inside the installed skill tree.

#### Scenario: Missing or modified resource
- **WHEN** a locked official resource is absent or has changed
- **THEN** package validation fails with the affected path.

### Requirement: Native MCP remains the editor transport
The package MUST retain the existing native MCP endpoint and MUST NOT launch or configure a second Bridge service.

#### Scenario: Official document describes legacy Bridge
- **WHEN** the upstream instructions include a WebSocket workflow
- **THEN** the Chinese entrypoint directs live editor calls to native help/discover/call and retains the upstream workflow only as reference.

### Requirement: Executable tools and clean delivery
Official offline tools SHALL run with dependencies outside immutable plugin resources, and delivery MUST exclude dependencies, caches, and temporary test projects.

#### Scenario: Format validation
- **WHEN** valid and invalid records are passed to the bundled official validator
- **THEN** valid records pass and invalid records fail without contacting an editor or starting a Bridge.

### Requirement: Plugin snapshot and installed host agree
The plugin SHALL carry the same official resource digests as the source package and expose them after actual Codex installation.

#### Scenario: Installed package verification
- **WHEN** Codex installs the updated plugin
- **THEN** installed resources match the source manifest, offline tools execute from the installation, and the native MCP can read an isolated test project.

### Requirement: Generated component defaults preserve existing semantics
The adaptation tool SHALL preview changes by default and SHALL only fill missing groupId/locked fields in an explicitly selected external eprj3 project when --apply is provided.

#### Scenario: Explicit normalization
- **WHEN** generated schematic components lack common fields
- **THEN** the tool adds absent defaults while preserving existing values, IDs, tickets, libraries, and nets, and the resulting records pass the corresponding original schemas.
