"""交付 ZIP 必须排除依赖与临时验证文件。"""
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'scripts'))
spec = importlib.util.spec_from_file_location('package_builder', ROOT/'scripts/build_package.py')
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


class PackagingTest(unittest.TestCase):
    def test_dependencies_caches_and_test_artifacts_are_not_shipped(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for name in ['catalog.json', 'plugin.json']:
                (root/name).write_text(json.dumps({'version':'0.1.0-test.1'}))
            (root/'README.md').write_text('ship me')
            for directory in ['node_modules', '.cache', 'artifacts', '.pytest_cache', '.venv']:
                path = root/directory/'not-for-users.txt'
                path.parent.mkdir(parents=True)
                path.write_text('exclude me')
            with patch.object(builder, 'validate', return_value={'ok':True}):
                result = builder.build(root)
            with zipfile.ZipFile(result['path']) as archive:
                self.assertIn('README.md', archive.namelist())
                self.assertFalse(any('not-for-users' in path for path in archive.namelist()), archive.namelist())
