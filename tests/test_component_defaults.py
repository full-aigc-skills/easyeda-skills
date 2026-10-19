"""字段适配仅补缺失的原理图公共字段，不改变已有值和网络关联。"""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]

class ComponentDefaultsTest(unittest.TestCase):
    def test_only_missing_fields_are_added_and_preview_does_not_write(self):
        spec=importlib.util.spec_from_file_location('defaults',ROOT/'skills/easyeda-eprj3/scripts/normalize_component_defaults.py')
        m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);(root/'test.eprj3').write_text('{}');file=root/'P1.esch2'
            header='{"type":"DOCHEAD"}||{"docType":"SCH_PAGE","uuid":"abc","client":"abc"}|\n'
            body={'id':'one','attrs':{'NET':'VCC','Name':'a||b'}}
            original=header+'{"type":"COMPONENT","id":"one","ticket":2}||'+json.dumps(body)+'|\n'
            file.write_text(original)
            self.assertEqual(m.normalize(root)['records'],1);self.assertEqual(file.read_text(),original)
            m.normalize(root,apply=True);line=file.read_text().splitlines()[1];payload=json.loads(line.split('||',1)[1].removesuffix('|'))
            self.assertEqual(payload,{**body,'groupId':'','locked':False});self.assertIn('"ticket":2',line)
            self.assertEqual(m.normalize(root,apply=True)['records'],0)
