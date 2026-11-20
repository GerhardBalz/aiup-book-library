import hashlib, json, sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent
record = json.loads((root / "replay/BASELINE.json").read_text(encoding="utf-8"))
errors = []
for rel, expected in record["files"].items():
    path = (root / rel).resolve()
    if not path.is_relative_to(root.resolve()) or not path.is_file():
        errors.append("Missing/out-of-scope: " + rel)
    elif hashlib.sha256(path.read_bytes()).hexdigest() != expected:
        errors.append("Changed: " + rel)
runtime = json.loads((root / record["runtime_manifest"]).read_text(encoding="utf-8"))
for package in runtime["packages"].values():
    for rel, expected in package["files"].items():
        parts = Path(rel).parts
        path = root / ".agents/skills" / Path(*parts[1:])
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != expected:
            errors.append("Runtime mismatch: " + rel)
if list((root / "docs/use_cases").glob("UC-001-*.md")):
    errors.append("UC-001 already exists; this is no longer the pre-authoring checkpoint")
print(json.dumps({"variant":record["variant"], "checked_files":len(record["files"]),
    "runtime_skills":runtime["discovered_skill_count"],"failures":errors},indent=2))
raise SystemExit(bool(errors))

