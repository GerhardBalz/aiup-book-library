import hashlib, json
from pathlib import Path

root = Path(__file__).resolve().parent.parent
baseline = json.loads((root / 'replay/BASELINE.json').read_text(encoding='utf-8'))
errors = []
for name, expected in baseline['files'].items():
    path = (root / name).resolve()
    if not path.is_relative_to(root.resolve()) or not path.is_file():
        errors.append('Missing/out-of-scope: ' + name)
    elif hashlib.sha256(path.read_bytes()).hexdigest() != expected:
        errors.append('Changed: ' + name)
docs = sorted(path.relative_to(root).as_posix() for path in (root / 'docs').rglob('*') if path.is_file())
if docs != baseline['initial_docs']:
    errors.append('Specification authoring has already started: docs/ differs from the starter')
runtime = json.loads((root / 'replay/runtime.json').read_text(encoding='utf-8'))
runtime_files = 0
for package in runtime['packages'].values():
    for name, expected in package['files'].items():
        path = root / '.agents' / name
        runtime_files += 1
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != expected:
            errors.append('Published runtime mismatch: ' + name)
print(json.dumps({'variant': baseline['variant'], 'checked_files': len(baseline['files']),
    'runtime_files': runtime_files, 'initial_docs': docs, 'failures': errors}, indent=2))
raise SystemExit(bool(errors))
