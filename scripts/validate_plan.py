"""Validate structured agent plans in docs/plans/*.plan.md."""
import pathlib
import sys

import yaml

REQUIRED = {"task", "issue", "risk", "autonomy", "files", "acceptance"}
RISKS = {"low", "medium", "high"}
AUTONOMY = {"L1", "L2", "L3"}
CHECKS = {"pytest", "mypy", "review"}
ALLOWED_PREFIXES = ("src/", "tests/", "docs/")


def validate(path: pathlib.Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return [f"{path}: must start with '---' (YAML frontmatter)"]
    try:
        meta = yaml.safe_load(text.split("---", 2)[1])
    except yaml.YAMLError as exc:
        return [f"{path}: invalid YAML: {exc}"]
    if not isinstance(meta, dict):
        return [f"{path}: frontmatter is not a mapping"]

    errors: list[str] = []
    keys = set(meta)
    errors += [f"{path}: missing key '{k}'" for k in sorted(REQUIRED - keys)]
    errors += [f"{path}: unknown key '{k}' (typo?)" for k in sorted(keys - REQUIRED)]

    if meta.get("risk") not in RISKS:
        errors.append(f"{path}: risk must be one of {sorted(RISKS)}")
    if meta.get("autonomy") not in AUTONOMY:
        errors.append(f"{path}: autonomy must be one of {sorted(AUTONOMY)}")
    if meta.get("autonomy") == "L3" and meta.get("risk") != "low":
        errors.append(f"{path}: L3 autonomy is only allowed for low-risk plans")

    for f in meta.get("files") or []:
        if not str(f).startswith(ALLOWED_PREFIXES):
            errors.append(f"{path}: file out of scope: {f}")

    for ac in meta.get("acceptance") or []:
        if not isinstance(ac, dict) or not {"id", "text", "verified_by"} <= set(ac):
            errors.append(f"{path}: acceptance item needs id, text, verified_by: {ac}")
        elif ac["verified_by"] not in CHECKS:
            errors.append(f"{path}: {ac['id']} verified_by must be one of {sorted(CHECKS)}")
    return errors

def main() -> int:
    plans = sorted(pathlib.Path("docs/plans").glob("*.plan.md"))
    errors = [e for p in plans for e in validate(p)]
    for e in errors:
        print(f"::error::{e}")
    print(f"Checked {len(plans)} plan(s): {len(errors)} error(s)")
    return 1 if errors else 0

if __name__ == "__main__":
    sys.exit(main())