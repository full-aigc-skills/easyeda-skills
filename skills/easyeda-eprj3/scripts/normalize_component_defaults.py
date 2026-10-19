"""预览或补齐独立 .eprj3 工程中原理图 COMPONENT 缺失的公共字段。"""
import argparse
import json
from pathlib import Path

SKILL = Path(__file__).resolve().parents[1]


def normalize(project, apply=False):
    root = Path(project).resolve()
    if root.is_relative_to(SKILL.parent.resolve()) or not any(root.glob('*.eprj3')):
        raise ValueError('只能适配技能目录之外的明确 .eprj3 工程')
    decoder = json.JSONDecoder()
    updates = []
    count = 0
    for path in sorted(root.rglob('*.esch2')):
        if path.is_symlink() or not path.resolve().is_relative_to(root):
            raise ValueError('工程中不允许外部文档链接：' + str(path))
        lines = path.read_text().splitlines(keepends=True)
        kind = None
        changed = 0
        for i, line in enumerate(lines):
            if not line.strip():
                continue
            head, end = decoder.raw_decode(line)
            if line[end:end+2] != '||':
                raise ValueError('文档分隔符无效：' + str(path))
            start = end + 2
            if not line[start:].lstrip('|\r\n'):
                continue
            body, consumed = decoder.raw_decode(line[start:])
            if head.get('type') == 'DOCHEAD':
                kind = body.get('docType')
            if kind not in {'SCH_PAGE', 'SYMBOL', 'SIMULATION'} or head.get('type') != 'COMPONENT':
                continue
            if 'groupId' in body and 'locked' in body:
                continue
            body.setdefault('groupId', '')
            body.setdefault('locked', False)
            lines[i] = line[:start] + json.dumps(body, ensure_ascii=False, separators=(',', ':')) + line[start+consumed:]
            changed += 1
        if changed:
            updates.append((path, ''.join(lines), changed))
            count += changed
    # 全部解析成功后再写，避免遇到无效文件时只改了一半。
    if apply:
        for path, text, _ in updates:
            path.write_text(text)
    return {'applied': apply, 'records': count,
            'files': [{'path':str(path.relative_to(root)), 'records':n} for path, _, n in updates]}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--project', type=Path, required=True)
    parser.add_argument('--apply', action='store_true', help='默认只预览；显式应用到已授权工程')
    args = parser.parse_args()
    print(json.dumps(normalize(args.project, args.apply), ensure_ascii=False))
