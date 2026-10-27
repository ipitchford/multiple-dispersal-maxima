# Final editor fixes (27 October 2026)

These fixes were made after the verification re-review, the targeted proof audit and the final outside-model correctness audit of the revised draft. No mathematical claim was strengthened. Each change is listed with its trigger.

## Manuscript

1. **Theorem 2, final sentences** (outside-model audit, item 1). The old sentence "The same holds ..." imported the exact identities M(3)=1, M'(3)=0 and the value of M''(3) into smooth L^1-close approximations, where they are false (adding a small constant to an approximation raises M(3)). The statement now separates two cases. Every rearrangement of m has the same population curve, so it keeps the exact identities and the two maxima. Every positive smooth strictly increasing resource that is L^1-close to the increasing step function, with values in a fixed compact subinterval of (0, infinity), keeps a nondegenerate local minimum near d=3 and at least two distinct strict local maxima. The exact identities are explicitly not claimed for these approximations. The proof now says that the perturbed minimum d_m~ moves and that M at that minimum is close to, but in general not equal to, 1.
2. **Proposition 4 certificate** (outside-model audit, item 2; proof audit, section 1). The proof now displays the exact p_3 and D, gives the size and sign of the exact rational M''(d0) ~ 1.0797588e-21, and adds a check that does not use M''. Two traps are certified: (d0-1e-4, d0-1e-5, d0) and (d0, d0+1e-2, 31/10), with M(d0)=1 exactly. The new standard-library script `interval_traps.py` certifies the four signs with rigorous rational square-root enclosures. Its output agrees with the proof audit's independent 120-digit interval computation.
3. **Fragility of the 14.17 witness** (proof audit, section 1). The effect-size paragraph now says plainly that the left maximum lies within 1e-4 of d0 and is about 1e-32 above M(d0)=1, that the right maximum lies in (d0+1e-2, 3.1), and that small parameter changes (d0=3.03, theta3=11.3, theta2=1+1e-6, theta1=1-1e-7) make M''(d0) negative so the two maxima of the construction disappear.
4. **Effect size** (re-review, NEW-5). "Area of order 10^-14" is now "about 7 x 10^-15", matching Table 1 and p3 ~ 7.43e-15.
5. **Lemma 12 (lem:many-kernels)** (proof audit, section 6; outside-model audit, item 5). Added the convention r_0 := a, so the base case of the induction is defined.
6. **Lemma 10, patching sentence** (proof audit, section 5; outside-model audit, item 6). The finite-cover sentence is replaced by a uniform argument: F_M stays below -a/(2(a+d_1)) on a fixed neighbourhood, so F is strictly decreasing in M there, the local implicit-function branches agree on overlaps and define one analytic function on [-eps_I, eps_I] x I.
7. **Atomic law stays probabilistic** (outside-model audit, item 3). Lemma 10's proof now chooses eps_I < 1/(2W), so 1 - eps W > 0 and eps_* <= eps_I inherits this.
8. **"But not uniformly"** (outside-model audit, item 4). Step 4 of the proof of Theorem 1 now proves it: max m_eps >= c_eps r_N with c_eps -> 1, so the sup-norm distance to a stays at least r_N - a.
9. **"Disjoint" traps** (proof audit, sections 2 and 7). Remark 8 now speaks of traps whose open intervals are disjoint, which covers traps sharing an endpoint. The proof of Theorem 2 names its two traps and says why the maxima are distinct.
10. **Two eta symbols** (proof audit, section 3). The slope of the added linear term is renamed kappa; eta_eps remains the L^1 tolerance.
11. **Section 8 search wording** (re-review, NEW-5). The text now says the multistart search's best contrast was 14.41 and never reached the certified 14.17, so the negative finding is weak evidence.
12. **Bai-Li 2021 citation** (re-review, NEW-1). Added the DataCite DOI 10.48550/arXiv.2108.01826. It resolves at doi.org, and the DataCite record title, authors (Bai, Xueli; Li, Fang) and year (2021) match the citation.
13. **Code availability**. Rewritten to state the exact `uv run` commands with pinned versions, and to name `interval_traps.py`. The DOI and repository were added to the title block and to this paragraph at publication.

The novelty/priority points of the outside-model audit (Liang-Zhang full text, Bai-Li-Shi full text, finite complete-graph analogue) were already disclosed as caveats. They remain open and are recorded in RESEARCH_GATES.json.

## Code and receipts

14. **Dependencies** (re-review, NEW-2). `plot_population.py` and `contrast_search.py` now carry PEP 723 inline metadata pinning numpy 2.4.6, scipy 1.17.1 and matplotlib 3.11.2. The same pins are in `requirements.txt`.
15. **Contrast-search receipt** (re-review, NEW-3). `contrast_search.json` was regenerated with the default 2000 starts. The best contrast found (14.407868554182523) and R* (14.172900795246138) are unchanged; only `part1_starts` changed from 1500 to 2000.
16. **Private editorial note** (re-review, NEW-4). A private development audit file that contained a private editorial assessment is not shipped. Every shipped file was scanned with the Evidence Press leak scanner.

## Rebuild and rerun

The PDF was rebuilt with pdflatex (three passes). There were no undefined references and no overfull boxes after one display was split. All 16 pages were rendered and inspected, and the TeX-leak preflight passed. All six scripts were rerun from a clean copy:
- `audit_meanfield.py`, `contrast_witness.py`, `resource_fingerprints.py` and `interval_traps.py` with `uv run python3 -I`;
- `plot_population.py` and `contrast_search.py` with `uv run --no-project --with numpy==2.4.6 --with scipy==1.17.1 --with matplotlib==3.11.2 python3 -I`;
- `contrast_search.py` also through `uv run --script`.

`contrast_witness.json`, `meanfield_audit_result.json`, `resource_fingerprints.json` and `three_level_peaks.json` were byte-identical to the receipts. The script-mode and `--with` search outputs were identical.

## Found during publication CI

17. **Platform sensitivity of the search** (GitHub Actions, Linux x86-64). With the same pinned versions, the multistart part of `contrast_search.py` found no successful SLSQP start on Linux (best contrast `inf`). It found 14.41 on macOS arm64. R* agreed. The code-availability paragraph now says so. CI checks the search with `check_search.py`, which requires R* to match and flags any contrast below 14.17. The search is evidence only and no proof depends on it.
