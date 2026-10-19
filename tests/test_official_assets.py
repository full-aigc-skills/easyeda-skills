"""验证官方资源在冷安装中可用，篡改、缺失和依赖污染不能通过。"""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


def module():
    spec = importlib.util.spec_from_file_location('official_assets', ROOT / 'scripts/validate_official.py')
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


class OfficialAssetsTest(unittest.TestCase):
    def test_all_five_complete_skills_are_present(self):
        result = module().validate(ROOT)
        self.assertEqual(result['officialSkills'], 5)
        self.assertGreaterEqual(result['schemas'], 297)
        for name in ['easyeda-api', 'easyeda-schematic-net-fanout', 'easyeda-eprj3',
                     'easyeda-format-skill', 'easyeda-extension-development']:
            self.assertTrue((ROOT / 'skills' / name / 'upstream/SKILL.md').is_file())
        self.assertTrue((ROOT / 'skills/easyeda-eprj3/upstream/companions/easyeda-format-skill/validate.js').is_file())

    def test_missing_tampered_and_untracked_files_fail(self):
        m = module()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            folder = root / 'skills/easyeda-api/upstream'
            folder.mkdir(parents=True)
            file = folder / 'SKILL.md'
            file.write_text('original')
            import hashlib
            manifest = {'schemaVersion': 1, 'bundles': [{'skill': 'easyeda-api', 'repository': 'easyeda-api-skill',
                'revision': 'a' * 40, 'root': 'skills/easyeda-api/upstream', 'role': 'primary',
                'files': [{'path': 'SKILL.md', 'bytes': 8, 'sha256': hashlib.sha256(b'original').hexdigest()}]}]}
            (root / 'official-assets.json').write_text(json.dumps(manifest))
            m.validate(root, require_complete=False)
            file.write_text('tampered')
            with self.assertRaisesRegex(ValueError, 'SKILL.md'):
                m.validate(root, require_complete=False)
            file.unlink()
            with self.assertRaisesRegex(ValueError, 'SKILL.md'):
                m.validate(root, require_complete=False)
            file.write_text('original')
            extra = folder / 'node_modules/dependency/index.js'
            extra.parent.mkdir(parents=True)
            extra.write_text('bad')
            with self.assertRaisesRegex(ValueError, 'node_modules'):
                m.validate(root, require_complete=False)

    def test_manifest_path_escape_and_symlink_fail(self):
        m = module()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            folder = root / 'skills/easyeda-api/upstream'
            folder.mkdir(parents=True)
            (folder/'outside').symlink_to(root.parent)
            (root/'official-assets.json').write_text(json.dumps({'schemaVersion':1,'bundles':[
                {'skill':'easyeda-api','repository':'easyeda-api-skill','revision':'a'*40,
                 'root':'skills/easyeda-api/upstream','role':'primary','files':[]}]}))
            with self.assertRaises(ValueError):m.validate(root, require_complete=False)
