from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]

def load_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)

def main():
    targets = list((ROOT / "configs").glob("*.json"))
    targets += list((ROOT / "schemas").glob("*.json"))
    targets += list((ROOT / "tests").rglob("*.json"))
    targets += list((ROOT / "workflows").glob("*.json"))

    failed = False
    for path in targets:
        try:
            load_json(path)
            print(f"OK {path.relative_to(ROOT)}")
        except Exception as exc:
            failed = True
            print(f"FAIL {path.relative_to(ROOT)}: {exc}", file=sys.stderr)

    if failed:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
