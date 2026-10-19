"""调用随包携带的官方格式校验器；仅显式 --install-deps 时安装锁定依赖。"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

SKILL = Path(__file__).resolve().parents[1]
FORMAT = SKILL / 'upstream'
if not (FORMAT / 'validate.js').is_file():
    FORMAT = FORMAT / 'companions/easyeda-format-skill'


def registry_lock(raw):
    """保留官方版本与 integrity，仅把镜像 tarball 地址映射到 npm 官方 registry。"""
    lock = json.loads(raw)
    for package in lock.get('packages', {}).values():
        resolved = package.get('resolved', '')
        prefix = 'https://registry.npmmirror.com/'
        if resolved.startswith(prefix):
            package['resolved'] = 'https://registry.npmjs.org/' + resolved[len(prefix):]
    return (json.dumps(lock, ensure_ascii=False, indent=2) + '\n').encode()


def runtime_path(path):
    resolved = Path(path).expanduser().resolve()
    # 技能可被整体移动；按当前安装位置保护本技能及其插件 skills/ 树。
    if resolved.is_relative_to(SKILL.parent.resolve()) or resolved == FORMAT.resolve():
        raise ValueError('依赖缓存必须位于技能安装目录之外：' + str(resolved))
    return resolved


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--runtime-dir', type=Path)
    parser.add_argument('--install-deps', action='store_true', help='显式安装 package-lock 锁定的 ajv 依赖到可写缓存')
    parser.add_argument('arguments', nargs=argparse.REMAINDER, help='-- 后原样传递给官方 validate.js')
    args = parser.parse_args(argv)
    lock = (FORMAT / 'package-lock.json').read_bytes()
    default = Path(os.environ.get('XDG_CACHE_HOME', str(Path.home()/'.cache'))) / 'easyeda-official-format' / (hashlib.sha256(lock).hexdigest()[:16] + '-npmjs')
    runtime = runtime_path(args.runtime_dir or default)
    node = shutil.which('node')
    if not node:
        parser.error('需要 Node.js 18+，本脚本不会全局安装 Node.js')
    if args.install_deps:
        npm = shutil.which('npm')
        if not npm:
            parser.error('显式安装依赖需要 npm')
        runtime.mkdir(parents=True, exist_ok=True)
        for name in ['package.json', 'package-lock.json']:
            target = runtime/name
            source = (FORMAT/name).read_bytes()
            if name == 'package-lock.json':
                source = registry_lock(source)
            if target.exists() and target.read_bytes() != source:
                parser.error('依赖目录已有不同配置，请指定新目录：' + str(runtime))
            target.write_bytes(source)
        installed = subprocess.run([npm, 'ci', '--ignore-scripts', '--no-audit', '--no-fund', '--registry=https://registry.npmjs.org', '--prefix', str(runtime)], check=False)
        if installed.returncode:
            return installed.returncode
    if not (runtime/'node_modules/ajv/package.json').is_file():
        parser.error('缺少本地 ajv 依赖；获准后用 --install-deps 初始化可写缓存：' + str(runtime))
    values = args.arguments
    if values and values[0] == '--':
        values = values[1:]
    if not values:
        return 0 if args.install_deps else parser.error('需要传递官方校验参数，例如 -- DOCHEAD JSON')
    env = dict(os.environ, NODE_PATH=str(runtime/'node_modules'))
    return subprocess.run([node, str(FORMAT/'validate.js'), *values], env=env, check=False).returncode


if __name__ == '__main__':
    try:
        sys.exit(main())
    except ValueError as error:
        print(str(error), file=sys.stderr)
        sys.exit(2)
