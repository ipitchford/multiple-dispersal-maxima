"""Independent exact check of the three-resource-level population minimum."""

from fractions import Fraction as F
import argparse
import json
from pathlib import Path

p = [F(2405, 3504), F(1095, 3504), F(4, 3504)]
t = [F(4, 5), F(4, 3), F(30)]
m = [F(1, 20), F(25, 12), F(329, 10)]
d, M = F(3), F(1)

assert sum(p) == 1 and all(w > 0 for w in p)
assert all(x > 0 for x in m)
assert sum(w * x for w, x in zip(p, t)) == M
residuals = [d * (M - x) + x * (resource - x) for x, resource in zip(t, m)]
assert residuals == [0, 0, 0]
A = [d + 2 * x - resource for x, resource in zip(t, m)]
assert A == [F(91, 20), F(43, 12), F(301, 10)]
assert A == [x + d * M / x for x in t]
D = 1 - d * sum(w / a for w, a in zip(p, A))
assert D == F(2, 7)
assert D == sum(w * x**2 / a for w, x, a in zip(p, t, A)) / M
N = sum(w * (M - x) / a for w, x, a in zip(p, t, A))
assert N == 0
Mprime = N / D
tprime = [(M - x + d * Mprime) / a for x, a in zip(t, A)]
C = sum(w * (u**2 + u) / a for w, u, a in zip(p, tprime, A))
Msecond = (2 * Mprime * sum(w / a for w, a in zip(p, A)) - 2 * C) / D
assert C == F(-6042635, 13826346807)
assert Msecond == F(6042635, 1975192401) > 0
mean_resource = sum(w * resource for w, resource in zip(p, m))
assert mean_resource == F(347, 480) < M

result = {
    "status": "All exact checks passed",
    "probabilities": list(map(str, p)),
    "resources": list(map(str, m)),
    "equilibrium_at_d_3": list(map(str, t)),
    "M": str(M),
    "A": list(map(str, A)),
    "implicit_denominator": str(D),
    "M_prime": str(Mprime),
    "component_derivatives": list(map(str, tprime)),
    "curvature_numerator": str(C),
    "M_second": str(Msecond),
    "mean_resource_and_endpoint_limit": str(mean_resource),
}
text = json.dumps(result, indent=2)
print(text)
ap = argparse.ArgumentParser()
ap.add_argument("--out", default="output", help="output directory (never the shipped receipt)")
out = Path(ap.parse_args().out)
out.mkdir(parents=True, exist_ok=True)
(out / "meanfield_audit_result.json").write_text(text + "\n")
