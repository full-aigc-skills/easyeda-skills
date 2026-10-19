"""在临时格式目录中运行原版审计器，适配其硬编码 node_modules 路径。"""
import argparse
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from validate_format import FORMAT, SKILL, runtime_path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--runtime-dir', type=Path, required=True)
    args = parser.parse_args()
    runtime = runtime_path(args.runtime_dir)
    if not (runtime/'node_modules/ajv/package.json').is_file():
        parser.error('请先使用本技能 validate_format.py --install-deps 初始化隔离依赖')
    node = shutil.which('node')
    if not node:
        parser.error('需要 Node.js 18+')
    with tempfile.TemporaryDirectory(prefix='easyeda-format-audit-') as tmp:
        staged = Path(tmp)/'format'
        shutil.copytree(FORMAT, staged)
        (staged/'node_modules').symlink_to(runtime/'node_modules', target_is_directory=True)
        return subprocess.run([node, str(SKILL/'upstream/scripts/tools/audit-format.js'),
                               '--format-skill', str(staged)], cwd=tmp, check=False).returncode


if __name__ == '__main__':
    sys.exit(main())
