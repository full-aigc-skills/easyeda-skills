# Changelog

## 2022111701

- Added design rule template `RULE_TEMPLATE`.
- Added pad-specific thermal relief rules including connection mode, spoke spacing, spoke width, and spoke angle.

## 2022111601

- Added `ARC` variant `CARC`: the old `ARC` always represents two-point interaction mode, and the new `CARC` always represents center interaction mode.

## 2022110101

- `REGION` keepout types 1 and 4 were split.

## 2022101701

- PCB format upgraded to 1.6.
- `FONT` cache redesigned.

## 2022083001

- Extended `PREFERENCE`, enriched routing corner modes, and added minimum trace corner ratio.

## 2022082901

- Extended `CANVAS`, added Alt snap grid size, etc.
- Extended `PREFERENCE`, added routing, snap, rotation, etc.

## 2022082601

- Version upgraded to 1.5.
- Polygon "chamfer ratio" changed to "corner radius"; parse compatibility required.
- `LAYER_PHYS` added information about retaining islands on internal planes; old formats lack this and need compatibility handling.

## 2022082201

- `LAYER_PHYS` added.

## 2022071301

- `TEARDROP` added redundant group ID information.

## 2022070701

- `PAD_NET` added optional footprint internal pad ID parameter.

## 2022062301

- Added reuse block information `REUSE_BLOCK`.

## 2022061701

- `POURED` document version upgraded to 1.1 with incompatible updates.
- `POURED` added parent `POUR` ID.

## 2022060601

- Extended `SHELL_ENTITY` "belongs to" field. Compatibility recommendations:
  - Old `SHELLCUT` defaults to shell border + boss + entity: `28 = 4 + 8 + 16`.
  - Old `SHELL_ENTITY` with value `0` can be treated as shell border + boss + entity unselected.

## 2022042901

- Deprecated `SHELLCUT` primitive.
- Added `SHELL_ENTITY` primitive, mostly inheriting from deprecated `SHELLCUT`, with a new boolean operation attribute indicating cut or fill.

## 2022042101

- `SHELLCUT` adjusted.
- `SHELL_ENTITY` and `SHELLCUT` adjusted.

## 2022040601

- `CANVAS` supports expressing snap grid size; compatibility with old formats required. If no snap grid size, assign it from the grid size with some algorithm, e.g., multiply by a ratio.

## 2022033101

- `BOSS` added screw model.

## 2022033002

- `BOSS` adjusted to match preview version.
- PCB format version bumped to 1.4, incompatible with previous versions.

## 2022033001

- `CONNECT` description for footprint content override adjusted.

## 2022032801

- Expanded `CONNECT` scope, providing footprint internal primitive override functionality.

## 2022032501

- Polygon rectangle mode added corner radius parameter.

## 2022030403

- Added `SILK_OPTS` silkscreen options.

## 2022030402

- Added `PROP` primitive property override.

## 2022030401

- Added `ITEM_ORDER` primitive order object.

## 2022030201

- Added `OBJ` object.

## 2022012001

- `SHELL` T&B type added `TopInnerHeight` and `TopInnerThickness`.

## 2021122901

- `REGION` keepout types 1 and 4 split.

## 2021122801

- `SHELL` `DRAWER` added `Direction`.
- `SHELL` line width marked as deprecated.

## 2021111801

- Unshown `ATTR` marked by `null` in either X or Y.

## 2021090301

- `PANELIZE_OPT` split into `PANELIZE_STAMP` and `PANELIZE_SIDE`.

## 2021090202

- Panelization removed canvas origin following.

## 2021090201

- Added panelization primitives `PANELIZE` and `PANELIZE_OPT`.

## 2021080901

- Format version upgraded to 1.3.
- `RULE_SELECTOR` added `POUR` copper pour ID selector, `DIFF_PAIR` differential pair selector, `EQ_LEN_GRP` equal-length group selector.

## 2021071301

- `NET` added equal-length group information.

## 2021062301

- Format version upgraded to 1.2.
- `FONT` added width and height information.

## 2021050801

- Fine-tuned design rule priority values.
- Polygon system `C` fixed as cubic Bezier.

## 2021032402

- `SHELL` custom properties examples added.

## 2021032401

- `SHELL` added PCB height.

## 2021032301

- Added 3D shell system.

## 2021031301

- Removed the rule that 3D model parameters are stored in `ATTR`; now stored in custom properties.
- Adjusted the meaning of the 3D Model Transform property from transformation matrix to transformation parameters.

## 2021030401

- `NET` added differential pair configuration items.

## 2021022201

- Polygon system independent elements `RECT` and `CIRCLE` added `isCCW` parameter to define edge rotation direction.

## 2021020102

- `LAYER` type added `SUBSTRATE` definition.
- `LAYER` removed limits on number of `SIGNAL`, `PLANE`, `SUBSTRATE` layers.
- `CONNECT` primitive changed to one-to-many mode.

## 2021020101

- PCB version bumped to 1.1.
- `LAYER` removed the semantics that `SIGNAL`, `PLANE`, `SUBSTRATE` order is determined by layer number; now determined by order of appearance in the format.
- Added `LAYER_PHYS` layer physical properties.
- `TEARDROP` removed associated primitive ID.
- Added `CONNECT` primitive association to replace the previous internal `TEARDROP` association expression and provide a mechanism for future associations.

## 2020120801

- Vias removed solder mask expansion.
- Text removed strikethrough and underline.
- Text inverse expansion changed to "inverse enabled + inverse expansion size" to support zero-expansion inverse.

## 2020120101

- `IMAGE` changed to top-left point + width/height model.
- Polygon rectangle mode `R` changed to top-left point + width/height model.

## 2020112501

- Added 3D model related property definitions.

## 2020111801

- Removed `FONT`; previous font design was too simple.
- Added `FONT` caching the whole text polygon.

## 2020110901

- Re-annotated pad structure description according to actual implementation.

## 2020110501

- Removed copper pour "clearance to other nets" and "thermal relief" options; now handled by design rules.

## 2020110301

- `FILL` removed "internal plane no fill".

## 2020110201

- Added design rules.
- Via layers now use design rules.

## 2020102201

- Adjusted multiple primitives.

## 2020101402

- Adjusted `POURED` primitive to support splitting copper pour results into multiple primitives.

## 2020101401

- Adjusted copper pour related structures.
- Removed `DEVICE` and `FOOTPRINT` from PCB.

## 2020070901

- Removed `END_COMPONENT`; `ATTR` related to `COMPONENT` must explicitly specify the parent ID.
- Added `PAD_NET` section to indicate pad instance nets.

## 2020042701

- Removed design rules.
- Added `FOOTPRINT` file type.
- Adjusted classification of some primitives.
