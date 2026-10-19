"""校验随技能分发的固定官方快照，不联网、不启动 EDA 或 Bridge。"""
import hashlib
import json
from pathlib import Path, PurePosixPath
import re

PRIMARY = {'easyeda-api', 'easyeda-schematic-net-fanout', 'easyeda-eprj3',
           'easyeda-format-skill', 'easyeda-extension-development'}
FORBIDDEN = {'.git', 'node_modules', '__pycache__', '.cache', '.venv', 'dist'}


def inside(root, relative):
    path = PurePosixPath(relative)
    if path.is_absolute() or '..' in path.parts or not path.parts or '\\' in relative:
        raise ValueError('官方资源路径越界：' + relative)
    target = root.joinpath(*path.parts)
    if not target.resolve().is_relative_to(root.resolve()):
        raise ValueError('官方资源路径越界：' + relative)
    if any(root.joinpath(*path.parts[:i]).is_symlink() for i in range(1, len(path.parts) + 1)):
        raise ValueError('官方资源含符号链接：' + relative)
    return target


def validate(root, require_complete=True):
    root = Path(root).resolve()
    lock = json.loads((root / 'official-assets.json').read_text())
    if lock['schemaVersion'] != 1:
        raise ValueError('未知官方资源清单版本')
    expected, primaries, roots = {}, set(), set()
    for bundle in lock['bundles']:
        if not re.fullmatch(r'[0-9a-f]{40}', bundle['revision']):
            raise ValueError('官方资源未固定修订')
        prefix = 'skills/' + bundle['skill'] + '/upstream'
        if bundle['root'] != prefix and not bundle['root'].startswith(prefix + '/companions/'):
            raise ValueError('官方资源不在所属技能内：' + bundle['root'])
        folder = inside(root, bundle['root'])
        roots.add(prefix)
        if bundle['role'] == 'primary':
            primaries.add(bundle['skill'])
        for file in bundle['files']:
            path = inside(folder, file['path'])
            rel = path.relative_to(root).as_posix()
            if rel in expected:
                raise ValueError('重复官方资源：' + rel)
            expected[rel] = file
            if not path.is_file() or path.stat().st_size != file['bytes'] or hashlib.sha256(path.read_bytes()).hexdigest() != file['sha256']:
                raise ValueError('官方资源缺失或内容不一致：' + rel)
    if require_complete and primaries != PRIMARY:
        raise ValueError('未包含全部五个官方技能')
    actual = set()
    for prefix in roots:
        folder = inside(root, prefix)
        for path in folder.rglob('*'):
            rel = path.relative_to(root).as_posix()
            if path.is_symlink() or any(part in FORBIDDEN for part in path.relative_to(folder).parts):
                raise ValueError('官方资源中不允许依赖、缓存或符号链接：' + rel)
            if path.is_file():
                actual.add(rel)
    if actual != set(expected):
        raise ValueError('官方资源含未锁定文件或缺失文件：' + ', '.join(sorted(actual ^ set(expected))[:8]))
    if require_complete:
        needed = ['skills/easyeda-api/upstream/references/_index.md',
                  'skills/easyeda-format-skill/upstream/validate.js',
                  'skills/easyeda-eprj3/upstream/companions/easyeda-format-skill/validate.js',
                  'skills/easyeda-eprj3/upstream/scripts/init.js',
                  'skills/easyeda-extension-development/upstream/scripts/eda-api.js']
        for path in needed:
            if path not in expected:
                raise ValueError('缺少官方工具依赖：' + path)
    schemas = sum('/schemas/' in path and path.endswith('.json') for path in expected)
    return {'officialSkills': len(primaries), 'officialBundles': len(lock['bundles']),
            'officialFiles': len(expected), 'schemas': schemas}


if __name__ == '__main__':
    print(json.dumps(validate(Path(__file__).resolve().parents[1]), ensure_ascii=False))
