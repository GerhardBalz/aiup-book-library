"""Verify the frozen pre-requirements tutorial starting point without writing."""
import hashlib
import json
from pathlib import Path
import sys

root = Path(__file__).resolve().parent.parent
manifest = json.loads((root / 'baseline/BASELINE.json').read_text(encoding='utf-8'))
runtime = json.loads((root / 'baseline/runtime.json').read_text(encoding='utf-8'))
errors = []
for name, expected in manifest['files'].items():
    path = root / name
    if not path.resolve().is_relative_to(root) or not path.is_file():
        errors.append('Missing or out-of-scope file: ' + name)
    elif hashlib.sha256(path.read_bytes()).hexdigest() != expected:
        errors.append('Changed file: ' + name)
docs = sorted(p.relative_to(root).as_posix() for p in (root / 'docs').rglob('*') if p.is_file())
if docs != manifest['initial_docs']:
    errors.append('docs/ no longer matches the pre-requirements starting point')
for name, item in runtime['skills'].items():
    folder = root / '.agents/skills' / name
    if folder.is_symlink() or (hasattr(folder, 'is_junction') and folder.is_junction()):
        errors.append('Discovery folder must be an ordinary directory: ' + name)
    for relative, expected in item['files'].items():
        file = folder / relative
        if not file.is_file() or hashlib.sha256(file.read_bytes()).hexdigest() != expected:
            errors.append('Runtime file differs: ' + name + '/' + relative)
print(json.dumps({'variant': 'Book Library starter before requirements authoring',
                  'checked_files': len(manifest['files']),
                  'skills': len(runtime['skills']),
                  'runtime_files': sum(len(x['files']) for x in runtime['skills'].values()),
                  'initial_docs': docs, 'failures': errors}, indent=2))
sys.exit(1 if errors else 0)
