"""Semantic negative controls (standard library only).

Each control feeds a plausible corruption to the shipped certificate code
and requires that it is rejected; the unmodified baselines must pass first.
The certificates use assert statements, so this file refuses to run under
python -O.  Usage:  uv run python3 -I negative_controls.py
"""
import json
import sys
from fractions import Fraction as F
from pathlib import Path

if not __debug__:
    sys.exit("negative_controls.py must run without -O (the certificates use assert)")

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import contrast_witness as cw  # noqa: E402
import interval_traps as it  # noqa: E402

results = []


def expect(name, fn, should_pass):
    try:
        fn()
        ok = True
    except AssertionError:
        ok = False
    status = "PASS" if ok == should_pass else "FAIL"
    results.append((status, name, "accepted" if ok else "rejected"))


# Baselines
expect("baseline: Theorem 2 witness certifies", lambda: cw.certify(F(3), [F(4, 5), F(4, 3), F(30)]), True)
expect("baseline: Proposition 4 witness certifies", lambda: cw.certify(cw.D0, cw.THETA), True)
TRAPS = [(it.d0 - F(1, 10**4), -1), (it.d0 - F(1, 10**5), 1), (it.d0 + F(1, 100), 1), (F(31, 10), -1)]


def assert_sign(d, s):
    assert it.sign_M_minus_1(d) == s


for d, s in TRAPS:
    expect(f"baseline: sign(M(d)-1)={s} at d={float(d):.6f}", lambda d=d, s=s: assert_sign(d, s), True)

# Corruptions of the low-contrast witness (proof-audit fragility checks)
th = cw.THETA
expect("corrupt: d0 = 3.03 (M'' < 0)", lambda: cw.certify(F(303, 100), th), False)
expect("corrupt: theta3 = 11.3 (M'' < 0)", lambda: cw.certify(cw.D0, [th[0], th[1], F(113, 10)]), False)
expect("corrupt: theta2 = 1+1e-6 (M'' < 0)", lambda: cw.certify(cw.D0, [th[0], 1 + F(1, 10**6), th[2]]), False)
expect("corrupt: theta1 = 1-1e-7 (M'' < 0)", lambda: cw.certify(cw.D0, [1 - F(1, 10**7), th[1], th[2]]), False)
expect("corrupt: theta2 = 1-1e-8 (p not positive)", lambda: cw.certify(cw.D0, [th[0], 1 - F(1, 10**8), th[2]]), False)
# Corruption of the Theorem 2 witness: shrink the rich density
expect("corrupt: Theorem 2 with theta3 = 5", lambda: cw.certify(F(3), [F(4, 5), F(4, 3), F(5)]), False)
# Reversed trap claims must be rejected
for d, s in TRAPS:
    expect(f"corrupt: claim sign {-s} at d={float(d):.6f}", lambda d=d, s=s: assert_sign(d, -s), False)


# Receipt tampering: recompute and compare with shipped JSON, then with tampered copies
shipped = json.loads((HERE / "contrast_witness.json").read_text())
fresh = {"low_contrast_witness": cw.certify(cw.D0, cw.THETA),
         "original_witness": cw.certify(F(3), [F(4, 5), F(4, 3), F(30)])}


def same(a, b):
    assert a == b


expect("baseline: shipped contrast_witness.json equals recomputation", lambda: same(shipped, fresh), True)
for key, field, bad in [("original_witness", "M_second_at_d0", "6042636/1975192401"),
                        ("low_contrast_witness", "contrast_max_over_min", "14173319160001/999994960001"),
                        ("original_witness", "habitat_fractions", ["2405/3504", "5/16", "1/877"])]:
    t = json.loads(json.dumps(shipped))
    t[key][field] = bad
    expect(f"corrupt: tampered receipt {key}.{field}", lambda t=t: same(t, fresh), False)

fail = [r for r in results if r[0] != "PASS"]
for r in results:
    print(*r, sep=" | ")
print(f"{len(results) - len(fail)}/{len(results)} controls behaved as required")
sys.exit(1 if fail else 0)
