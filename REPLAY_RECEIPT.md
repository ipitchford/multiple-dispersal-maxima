# Replay receipt (27 October 2026)

Environment: see [ENVIRONMENT.txt](ENVIRONMENT.txt). Every run started from a fresh copy and wrote to a temporary output directory; no shipped file was modified.

| Step | Command | Result |
|---|---|---|
| Exact certificates, normal mode | `uv run python3 -B -I {audit_meanfield,contrast_witness,resource_fingerprints,interval_traps}.py --out OUT` | All assertions hold; the four receipts are byte-identical to the shipped JSON |
| Same, optimised mode | `... python3 -B -I -O ...` | Outputs byte-identical. Assertions are stripped in this mode, so it checks output determinism only; normal mode is the certificate |
| Numerical scripts | `uv run --no-project --with numpy==2.4.6 --with scipy==1.17.1 --with matplotlib==3.11.2 python3 -B -I {plot_population,contrast_search}.py --out OUT` | `three_level_peaks.json` and `contrast_search.json` byte-identical (also checked with `compare_numeric.py`, relative tolerance 1e-8). `contrast_search` uses the default 2000 starts: best contrast 14.407868554182523, R* = 14.172900795246138 |
| PEP 723 route | `uv run --no-project --script contrast_search.py --out OUT` | Identical output |
| Negative controls | `uv run python3 -B -I negative_controls.py` | 20/20 controls behave as required. Under `-O` the script refuses to run, as intended |
| PDF | pdflatex, three passes | 16 pages; no undefined references or overfull boxes; every page inspected; TeX-leak preflight passed |

Key certified values: M''(3) = 6042635/1975192401 (Theorem 2); M''(d0) ≈ 1.0797588e-21 > 0 exactly (Proposition 4); contrast 14173319160000/999994960001 ≈ 14.1733906; trap signs M(d0−1e−4) < 1, M(d0−1e−5) > 1, M(d0+1e−2) > 1, M(3.1) < 1.

Figures (PDF/PNG) are not byte-reproducible across platforms. Their plotted maxima are recorded in `three_level_peaks.json`. The multistart part of `contrast_search.py` is platform-sensitive: on Linux x86-64 (GitHub Actions, same pins) two runs gave no successful start and 14.1745, so CI checks only R* and flags any contrast below 14.17 (`check_search.py`).
