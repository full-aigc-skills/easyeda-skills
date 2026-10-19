"""显式刷新官方仓库清单与固定修订；仅下载文本元数据，不运行上游脚本。"""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import re
import subprocess
import time

ROOT = Path(__file__).resolve().parents[1]


def gh_json(path):
    return json.loads(subprocess.check_output(['gh', 'api', path], timeout=35))


def inspect_repo(repo):
    name = repo['name']
    sha = gh_json('repos/easyeda/' + name + '/commits/HEAD')['sha']
    cache = ROOT / '.local/upstream-records' / (name + '.json')
    if cache.is_file():
        prior = json.loads(cache.read_text())
        if prior['revision'] == sha:
            return prior
    paths = ['README.md']
    if name.endswith('-skill') or name == 'extension-dev-skill':
        paths.append('SKILL.md')
    if name.startswith('eext-'):
        paths.append('src/index.ts')
    paths += {
        'easyeda-client-cli': ['cli-for-ai.md'],
        'eext-freerouting-intergration': ['src/router/FreeRoutingRouter.ts', 'src/types/index.ts'],
        'eext-generate-schematic-from-netlist': ['src/enetImporter.ts'],
        'eext-ai-reuse-block-placement': ['src/agent/tools.ts', 'src/cbb.ts'],
        'eext-design-rule-generator': ['src/eda/runtime.ts', 'package.json'],
        'extension-dev-skill': ['scripts/eda-api.js'],
    }.get(name, [])
    files = []
    mounts = set()
    exports = set()
    license_notes = []
    for path in paths:
        url = 'https://raw.githubusercontent.com/easyeda/' + name + '/' + sha + '/' + path
        raw = None
        for attempt in range(3):
            response = subprocess.run([
                'gh', 'api', '-H', 'Accept: application/vnd.github.raw+json',
                'repos/easyeda/' + name + '/contents/' + path + '?ref=' + sha,
            ], capture_output=True, timeout=30)
            if response.returncode == 0:
                raw = response.stdout
                break
            if b'404' in response.stderr:
                break
            time.sleep(0.5 * (attempt + 1))
        if raw is None:
            if b'404' in response.stderr:
                continue
            raise RuntimeError('无法读取固定来源：' + name + '/' + path)
        body = raw.decode('utf-8-sig')
        files.append({'path': path, 'sha256': hashlib.sha256(raw).hexdigest(),
                      'bytes': len(raw), 'url': 'https://github.com/easyeda/' + name + '/blob/' + sha + '/' + path})
        mounts.update(re.findall(r'\beda\.([A-Za-z_][A-Za-z_0-9]*)', body))
        exports.update(re.findall(r'export\s+(?:async\s+)?function\s+(\w+)', body))
        if path == 'SKILL.md':
            match = re.search(r'^license:\s*(.+)$', body, re.M)
            if match:
                license_notes.append('SKILL.md frontmatter: ' + match.group(1))
    record = {'repository': name, 'revision': sha, 'url': repo['html_url'],
            'license': repo.get('license'), 'licenseEvidence': license_notes,
            'archived': repo['archived'], 'fork': repo['fork'], 'files': files,
            'observedApiMounts': sorted(mounts), 'entryExports': sorted(exports),
            'validation': 'source-inspected; runtime-not-tested'}
    cache.parent.mkdir(parents=True, exist_ok=True)
    cache.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
    return record


def main():
    repos = gh_json('orgs/easyeda/repos?per_page=100&type=all')
    if len(repos) >= 100:
        raise RuntimeError('组织仓库超过一页，需先扩展分页后再刷新完整清单')
    inventory = [{k: repo.get(k) for k in ['name', 'description', 'html_url', 'default_branch', 'archived', 'fork']}
                 | {'license': (repo.get('license') or {}).get('spdx_id')} for repo in repos]
    catalog = json.loads((ROOT / 'catalog.json').read_text())
    owners = {}
    for skill in catalog['skills']:
        for source in skill['sources']:
            owners.setdefault(source, []).append(skill['name'])
    records = []
    with ThreadPoolExecutor(max_workers=6) as executor:
        for record in executor.map(inspect_repo, sorted(inventory, key=lambda x: x['name'])):
            record['skillOwners'] = owners.get(record['repository'], [])
            record['disposition'] = ('archived-reference' if record['archived'] else
                                     'workflow-source' if record['skillOwners'] else 'supplementary-reference')
            records.append(record)
            print('READ', record['repository'], len(record['files']), flush=True)
    (ROOT / 'docs/upstream-repositories.json').write_text(json.dumps(inventory, ensure_ascii=False, indent=2) + '\n')
    (ROOT / 'source-lock.json').write_text(json.dumps({
        'schemaVersion': 1, 'retrievedAt': datetime.now(timezone.utc).isoformat(),
        'repositoryCount': len(records), 'records': records,
    }, ensure_ascii=False, indent=2) + '\n')


if __name__ == '__main__':
    main()
