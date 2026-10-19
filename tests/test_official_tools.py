"""可选的真实官方校验器正反例；CI 显式提供依赖缓存目录。"""
import json
import os
from pathlib import Path
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[1]


@unittest.skipUnless(os.environ.get('EASYEDA_FORMAT_RUNTIME'), '需要显式指定隔离的 ajv 缓存')
class OfficialFormatIntegrationTest(unittest.TestCase):
    def test_schema_accepts_valid_and_rejects_invalid_header(self):
        for skill in ['easyeda-format-skill', 'easyeda-eprj3']:
            helper = ROOT / 'skills' / skill / 'scripts/validate_format.py'
            command = ['python3', '-B', str(helper), '--runtime-dir', os.environ['EASYEDA_FORMAT_RUNTIME'], '--', 'DOCHEAD']
            good = subprocess.run([*command, json.dumps({'docType':'PCB','uuid':'1234567890abcdef','client':'1234567890abcdef'})], capture_output=True, text=True)
            self.assertEqual(good.returncode, 0, good.stderr)
            self.assertTrue(json.loads(good.stdout)['valid'])
            bad = subprocess.run([*command, json.dumps({'docType':'INVALID','uuid':'test','client':'wrong'})], capture_output=True, text=True)
            self.assertEqual(bad.returncode, 1, bad.stderr)
            self.assertFalse(json.loads(bad.stdout)['valid'])
