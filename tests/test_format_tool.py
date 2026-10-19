"""格式工具保持原版校验语义，依赖必须位于插件资源之外。"""
import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
ENTRY = ROOT/'skills/easyeda-format-skill/scripts/validate_format.py'


class FormatToolTest(unittest.TestCase):
    def test_registry_mapping_preserves_versions_and_integrity(self):
        import json
        spec = importlib.util.spec_from_file_location('format_tool', ENTRY)
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        raw = {'packages': {'node_modules/pkg': {'version': '1.2.3', 'integrity': 'sha512-test',
                'resolved': 'https://registry.npmmirror.com/pkg/-/pkg-1.2.3.tgz'}}}
        mapped = json.loads(m.registry_lock(json.dumps(raw).encode()))
        self.assertEqual(mapped['packages']['node_modules/pkg']['version'], '1.2.3')
        self.assertEqual(mapped['packages']['node_modules/pkg']['integrity'], 'sha512-test')
        self.assertEqual(mapped['packages']['node_modules/pkg']['resolved'], 'https://registry.npmjs.org/pkg/-/pkg-1.2.3.tgz')

    def test_runtime_cannot_pollute_skill_or_source(self):
        spec = importlib.util.spec_from_file_location('format_tool', ENTRY)
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        with self.assertRaises(ValueError):
            m.runtime_path(ENTRY.parent/'node_modules')
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(m.runtime_path(Path(tmp)), Path(tmp).resolve())
