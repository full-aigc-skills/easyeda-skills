"""从固定官方 checkout 导入完整跟踪文件；来源在 .local，不复制 Git、依赖或缓存。"""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
from validate_official import FORBIDDEN, inside, validate

ROOT = Path(__file__).resolve().parents[1]
BUNDLES = [
    ('easyeda-api', 'easyeda-api-skill', 'upstream', 'primary'),
    ('easyeda-schematic-net-fanout', 'easyeda-enhanced-schematic-skill', 'upstream', 'primary'),
    ('easyeda-eprj3', 'easyeda-eprj3-skill', 'upstream', 'primary'),
    ('easyeda-eprj3', 'easyeda-format-skill', 'upstream/companions/easyeda-format-skill', 'companion'),
    ('easyeda-eprj3', 'easyeda-eprj3-format', 'upstream/companions/easyeda-eprj3-format', 'companion'),
    ('easyeda-format-skill', 'easyeda-format-skill', 'upstream', 'primary'),
    ('easyeda-format-skill', 'easyeda-file-format', 'upstream/companions/easyeda-file-format', 'companion'),
    ('easyeda-format-skill', 'easyeda-file-format-v2', 'upstream/companions/easyeda-file-format-v2', 'companion'),
    ('easyeda-extension-development', 'extension-dev-skill', 'upstream', 'primary'),
]


def vendor(source_root, check=False):
    sources = {r['repository']: r for r in json.loads((ROOT / 'source-lock.json').read_text())['records']}
    bundles = []
    for skill, repository, directory, role in BUNDLES:
        source = Path(source_root).resolve() / repository
        revision = subprocess.check_output(['git', '-C', str(source), 'rev-parse', 'HEAD'], text=True).strip()
        if revision != sources[repository]['revision']:
            raise ValueError('官方 checkout 与来源锁不一致：' + repository)
        tracked = subprocess.check_output(['git', '-C', str(source), 'ls-files', '-z']).decode().split('\0')
        destination = ROOT / 'skills' / skill / directory
        records = []
        for name in sorted(n for n in tracked if n):
            relative = Path(name)
            original = source / relative
            if original.is_symlink() or any(x in FORBIDDEN for x in relative.parts):
                raise ValueError('官方 checkout 跟踪了不允许的依赖或链接：' + name)
            raw = original.read_bytes()
            target = inside(ROOT, (destination / relative).relative_to(ROOT).as_posix())
            if check:
                if not target.is_file() or target.read_bytes() != raw:
                    raise ValueError('官方导入不一致：' + str(target))
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(raw)
            records.append({'path': name, 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()})
        bundles.append({'skill': skill, 'repository': repository, 'revision': revision,
                        'url': sources[repository]['url'], 'license': sources[repository]['license'],
                        'licenseEvidence': sources[repository]['licenseEvidence'],
                        'root': destination.relative_to(ROOT).as_posix(), 'role': role, 'files': records})
    manifest = {'schemaVersion': 1, 'transport': 'native-mcp-only', 'bundles': bundles}
    path = ROOT / 'official-assets.json'
    if check:
        if json.loads(path.read_text()) != manifest:
            raise ValueError('官方资源清单与固定 checkout 不一致')
    else:
        path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(validate(ROOT), ensure_ascii=False))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-root', type=Path, required=True)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    vendor(args.source_root, args.check)
