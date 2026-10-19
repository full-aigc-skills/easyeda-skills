"""离线检查技能自包含、来源映射和元数据，不宣称运行行为通过。"""
import hashlib
import importlib.util
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


def validate(root=ROOT):
    spec = importlib.util.spec_from_file_location('easyeda_official_check', root / 'scripts/validate_official.py')
    official_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(official_module)
    official = official_module.validate(root)
    catalog = json.loads((root / 'catalog.json').read_text())
    lock = json.loads((root / 'source-lock.json').read_text())
    names = [s['name'] for s in catalog['skills']]
    if len(names) != len(set(names)):
        raise ValueError('技能名重复')
    actual = {p.name for p in (root / 'skills').iterdir() if p.is_dir()}
    if set(names) != actual:
        raise ValueError('技能目录与目录清单不一致')
    records = {r['repository']: r for r in lock['records']}
    if len(records) != lock['repositoryCount']:
        raise ValueError('上游仓库清单重复或数量不一致')
    for record in records.values():
        if not re.fullmatch(r'[a-f0-9]{40}', record['revision']):
            raise ValueError('来源未固定 Git 修订')
        for file in record['files']:
            if not re.fullmatch(r'[a-f0-9]{64}', file['sha256']):
                raise ValueError('来源文件缺少内容摘要')
    for skill in catalog['skills']:
        name = skill['name']
        if not re.fullmatch(r'easyeda-[a-z0-9]+(?:-[a-z0-9]+)*', name) or len(name) > 64:
            raise ValueError('技能命名无效：' + name)
        folder = root / 'skills' / name
        if folder.is_symlink() or not folder.resolve().is_relative_to(root.resolve()):
            raise ValueError('技能目录不得通过符号链接指向外部：' + name)
        text = (folder / 'SKILL.md').read_text()
        if not text.startswith('---\nname: ' + name + '\n') or len(text.splitlines()) >= 500:
            raise ValueError('技能 frontmatter 或行数无效：' + name)
        description = re.search(r'^description: (.+)$', text, re.M)
        if not description or json.loads(description.group(1)) != skill['description']:
            raise ValueError('description 与目录不一致：' + name)
        if re.search(r'\b(?:TODO|FIXME|unimplemented)\b', text):
            raise ValueError('未完成占位内容：' + name)
        if not (folder / 'agents/openai.yaml').is_file():
            raise ValueError('缺少 Codex 技能 UI 元数据：' + name)
        for source in skill['sources']:
            if source not in records or not records[source]['files'] or name not in records[source]['skillOwners']:
                raise ValueError('技能缺少实际读取来源：' + name + '/' + source)
        for path in folder.rglob('*'):
            if path.is_symlink():
                raise ValueError('技能中不允许外部符号链接：' + str(path))
        for document in folder.rglob('*.md'):
            # 固定上游快照保持原始字节，旧安装路径/原仓库链接不能在这里重写。
            # 完整性和自包含文件树由 official-assets.json 严格校验；适配入口仍检查链接。
            if document.is_relative_to(folder / 'upstream'):
                continue
            for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', document.read_text()):
                target = target.strip().strip('<>')
                if urlsplit(target).scheme or target.startswith('#'):
                    continue
                linked = (document.parent / unquote(target.split('#')[0])).resolve()
                if not linked.is_relative_to(folder.resolve()) or not linked.is_file():
                    raise ValueError('技能引用不自包含：' + str(document) + ' → ' + target)
    return {**official, 'ok': True, 'skills': len(names), 'officialAdaptations':
            sum(s['origin'] == 'official-adapted' for s in catalog['skills']),
            'upstreamRepositories': len(records)}


if __name__ == '__main__':
    print(json.dumps(validate(), ensure_ascii=False))
