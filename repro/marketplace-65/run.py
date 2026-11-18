"""Reproduce Marketplace #65 against frozen Book Library specification inputs.

Standard-library tooling test. It runs navigator/lint commands, never the application,
and never changes the source fixture, lifecycle statuses or tracker state.
"""
import argparse
import hashlib
import json
import platform
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

SEARCH = """# Use Case: Search catalog

## Overview

**Use Case ID:** UC-002\x20\x20
**Use Case Name:** Search catalog\x20\x20
**Primary Actor:** Member, Librarian\x20\x20
**Goal:** The actor finds Books and sees book copy availability.\x20\x20
**Trigger:** The actor requests a Catalog search.\x20\x20
**Status:** Draft\x20\x20

**Requirements:** [FR-002, FR-003](../requirements.md)\x20\x20
**Layers:** UI\x20\x20

## Preconditions

- The Catalog is configured.

## Main Success Scenario

1. The actor requests a Catalog search.
2. Book Library asks for search criteria.
3. The actor supplies search criteria.
4. Book Library presents matching Books and book copy availability.

## Alternative Flows

### A1: No matching Books

**Trigger:** No Books match the criteria (step 4).\x20\x20
**Flow:**

1. Book Library informs the actor that there are no matching Books.
2. Use case ends.

## Postconditions

### Success Postconditions

- The actor sees matching Books and book copy availability.

### Failure Postconditions

_None — the use case changes no data._

## Business Rules

### BR-001: Availability

Search results include book copy availability.
"""

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def invoke(script, fixture, output, name, extra):
    command = [sys.executable, "-X", "utf8", "-B", str(script),
               "--docs", str(fixture / "docs"), *extra, "--format", "json"]
    result = subprocess.run(command, cwd=fixture, capture_output=True, text=True, encoding="utf-8")
    (output / (name + ".stdout.json")).write_text(result.stdout, encoding="utf-8")
    (output / (name + ".stderr.txt")).write_text(result.stderr, encoding="utf-8")
    if result.returncode not in (0, 1):
        raise RuntimeError(name + ": unexpected tool exit " + str(result.returncode))
    try:
        value = json.loads(result.stdout)
    except ValueError as error:
        raise RuntimeError(name + ": non-JSON tool output") from error
    return value, result.returncode

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline-script", type=Path)
    parser.add_argument("--main-script", type=Path)
    parser.add_argument("--candidate-script", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    manifest = json.loads((Path(__file__).parent / "fixture-manifest.json").read_text(encoding="utf-8"))
    for item in manifest["files"]:
        relative = Path(item["path"])
        if relative.is_absolute() or ".." in relative.parts:
            raise RuntimeError("Fixture paths must be relative and stay inside the checkout")
        path = (root / item["path"]).resolve()
        if not path.is_relative_to(root):
            raise RuntimeError("Fixture path leaves the checkout")
        actual = (hashlib.sha256(path.read_bytes().replace(b"\r\n", b"\n")).hexdigest()
                  if "sha256_lf" in item else digest(path))
        if actual != item.get("sha256_lf", item["sha256"]):
            raise RuntimeError("Frozen fixture differs: " + item["path"])
    if (root / "docs/.spec-lint-baseline.json").exists():
        raise RuntimeError("An unrecorded lint baseline would change this reproduction")
    baseline = args.baseline_script or root / ".tessl/plugins/ai-unified-process/aiup-core/skills/spec-review/scripts/spec_lint.py"
    variants = [("registry-3.20.1", baseline.resolve())]
    if args.main_script:
        variants.append(("upstream-main", args.main_script.resolve()))
    if args.candidate_script:
        variants.append(("candidate", args.candidate_script.resolve()))
    for label, script in variants:
        if not script.is_file():
            raise RuntimeError("Tool is absent for " + label)
        expected = manifest.get("tool_sha256_lf", {}).get(label)
        actual = hashlib.sha256(script.read_bytes().replace(b"\r\n", b"\n")).hexdigest()
        if expected and actual != expected:
            raise RuntimeError("Pinned baseline identity differs for " + label)
    output = args.output.resolve()
    if output.exists():
        raise RuntimeError("Use a new output directory; retain earlier evidence")
    output.mkdir(parents=True)
    source_before = {item["path"]: digest(root / item["path"]) for item in manifest["files"]}
    report = {
        "scope": "deterministic navigator/lint reproduction; no fresh-agent or application qualification",
        "python": platform.python_version(),
        "fixture": manifest,
        "variants": [],
        "source_inputs_preserved": False,
    }
    cases = ["mapped-missing-spec", "unmapped-control", "existing-spec-missing-link", "repaired-link"]
    with tempfile.TemporaryDirectory(prefix="marketplace65-cases-") as temporary:
        for label, script in variants:
            if not script.is_file():
                raise RuntimeError("Tool is absent for " + label)
            variant = {"label": label, "script_sha256": digest(script), "cases": []}
            consumer_output = output / label / "consumer"
            consumer_output.mkdir(parents=True)
            consumer, consumer_exit = invoke(script, root, consumer_output, "next", ["--next"])
            variant["consumer_pending_commands"] = [p["command"] for p in consumer["pending"]]
            variant["consumer_next_exit"] = consumer_exit
            for case in cases:
                fixture = Path(temporary) / label / case
                fixture.mkdir(parents=True)
                git_context = subprocess.run(["git", "-C", str(fixture), "rev-parse", "--show-toplevel"],
                                             capture_output=True)
                if git_context.returncode == 0:
                    raise RuntimeError("Controlled fixture inherits an unrelated Git repository")
                for item in manifest["files"]:
                    target = fixture / item["path"]
                    target.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copyfile(root / item["path"], target)
                if case == "unmapped-control":
                    path = fixture / "docs/use_cases.puml"
                    text = path.read_text(encoding="utf-8")
                    text, count = re.subn(
                        r"(?m)^    ' Requirements: FR-002, FR-003\n    usecase [^\n]+ as UC002\n",
                        "", text)
                    if count != 1:
                        raise RuntimeError("Unmapped control could not remove the intended mapping")
                    text = re.sub(r"(?m)^.* --> UC002\n", "", text)
                    if "UC002" in text:
                        raise RuntimeError("Unmapped control retains a UC002 mapping")
                    path.write_text(text, encoding="utf-8")
                elif case in ("existing-spec-missing-link", "repaired-link"):
                    text = SEARCH
                    if case == "existing-spec-missing-link":
                        text = text.replace("**Requirements:** [FR-002, FR-003](../requirements.md)  \n", "")
                    target = fixture / "docs/use_cases/UC-002-search-catalog.md"
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_text(text, encoding="utf-8")
                snapshot = {p.relative_to(fixture).as_posix(): digest(p) for p in fixture.rglob("*") if p.is_file()}
                evidence = output / label / case
                evidence.mkdir(parents=True)
                nav, nav_exit = invoke(script, fixture, evidence, "next", ["--next"])
                lint, lint_exit = invoke(script, fixture, evidence, "lint", [])
                findings = lint if isinstance(lint, list) else lint["findings"]
                uncovered = sorted({f["element"] for f in findings if f["code"] == "FR_UNCOVERED"})
                pending = nav["pending"]
                commands = [p["command"] for p in pending]
                diagram = "/use-case-diagram" in commands
                target_spec = "/use-case-spec UC-002" in commands
                if case == "unmapped-control":
                    contract = diagram and all(r in uncovered for r in ("FR-002", "FR-003"))
                elif case == "repaired-link":
                    contract = not diagram and not target_spec and not any(
                        r in uncovered for r in ("FR-002", "FR-003"))
                else:
                    contract = not diagram and target_spec and all(
                        r in uncovered for r in ("FR-002", "FR-003"))
                after = {p.relative_to(fixture).as_posix(): digest(p) for p in fixture.rglob("*") if p.is_file()}
                if snapshot != after:
                    raise RuntimeError(label + "/" + case + ": navigator or lint wrote fixture data")
                variant["cases"].append({
                    "case": case, "contract_met": contract,
                    "next_exit": nav_exit, "lint_exit": lint_exit,
                    "pending_commands": commands, "uncovered_FRs": uncovered,
                    "lint_counts": nav["state"]["lint"],
                    "inputs_preserved": True,
                    "git_context": "isolated file fixture without repository history",
                })
            report["variants"].append(variant)
    report["source_inputs_preserved"] = source_before == {
        item["path"]: digest(root / item["path"]) for item in manifest["files"]}
    if not report["source_inputs_preserved"]:
        raise RuntimeError("Source fixture changed")
    original = report["variants"][0]["cases"]
    report["bug_reproduced"] = (
        not original[0]["contract_met"] and original[1]["contract_met"]
        and not original[2]["contract_met"])
    report["candidate_contract_met"] = (
        all(c["contract_met"] for c in report["variants"][-1]["cases"])
        if args.candidate_script else None)
    (output / "summary.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"bug_reproduced": report["bug_reproduced"],
                      "candidate_contract_met": report["candidate_contract_met"],
                      "source_inputs_preserved": report["source_inputs_preserved"],
                      "variants": [{"label": v["label"], "cases": [
                          {"case": c["case"], "contract_met": c["contract_met"],
                           "pending_commands": c["pending_commands"]} for c in v["cases"]]}
                          for v in report["variants"]]}, indent=2))
    return 0 if report["bug_reproduced"] and report["candidate_contract_met"] is not False else 1

if __name__ == "__main__":
    raise SystemExit(main())
