"""Compare two JSON receipts: equal structure, strings equal, floats within 1e-8 relative.
The top-level "versions" record (interpreter and package versions) is reported, not compared.
Usage: python3 -I compare_numeric.py NEW.json SHIPPED.json"""
import json
import sys


def cmp(a, b, path="$"):
    if isinstance(a, float) or isinstance(b, float):
        if abs(a - b) > 1e-8 * max(1.0, abs(b)):
            sys.exit(f"MISMATCH {path}: {a} vs {b}")
    elif isinstance(a, dict):
        if set(a) != set(b):
            sys.exit(f"MISMATCH keys at {path}")
        for k in a:
            cmp(a[k], b[k], f"{path}.{k}")
    elif isinstance(a, list):
        if len(a) != len(b):
            sys.exit(f"MISMATCH length at {path}")
        for i, (x, y) in enumerate(zip(a, b)):
            cmp(x, y, f"{path}[{i}]")
    elif a != b:
        sys.exit(f"MISMATCH {path}: {a!r} vs {b!r}")


new, old = json.load(open(sys.argv[1])), json.load(open(sys.argv[2]))
if isinstance(new, dict) and "versions" in new:
    print("versions (not compared):", new.pop("versions"), "vs", old.pop("versions", None))
cmp(new, old)
print("match:", sys.argv[2])
