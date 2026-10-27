# Revision response: "Arbitrarily many population maxima under uniform global dispersal"

Round 1, 27 October 2026. Reviewers: EIC; METH (methodology); DOM (domain); PERSP (perspective); DA (devil's advocate); SOL (Sol correctness audit).
Format: **R** = request, **A** = action, **C** = where the change is.

## Correctness

1. **R (SOL §3; DA m6):** Theorem 2 allowed any arrangement of the three levels, yet it claimed approximation by increasing functions. That claim is false for arbitrary arrangements.
   **A:** Theorem 2 now fixes the increasing step function (3). Invariance under rearrangement is stated separately. The proof notes that L^1 approximation by increasing functions needs this arrangement.
   **C:** Thm 2 statement; proof, "Smooth increasing versions".
2. **R (SOL §2; EIC m4; METH m5):** The smoothing tolerance must be chosen after epsilon, and the proof should give the diagonal choice explicitly.
   **A:** The proof of Theorem 1 is rewritten in four steps:
   - explicit epsilon_* = min{epsilon_I, Delta/(4C_I)};
   - eta_epsilon from Lemma 7, with ||v - s|| < min{epsilon^2, eta_epsilon};
   - an explicit |b_epsilon - a| bound;
   - the pointer to disjoint traps for "at least N".
   **C:** Proof of Thm 1, Steps 1–4.
3. **R (SOL §5; DA m5; EIC m2):** Display a uniform lower bound on D.
   **A:** Added eq. (14), D >= l^2/(b(b + d_1 b/l)), together with explicit M' and M'' formulas. The text now states that full C^2 convergence is used only in Thm 2 (METH m7).
   **C:** Lemma 7 and its proof.
4. **R (brief; METH m4; DA m2):** Make the first-variation error uniform over the dispersal range.
   **A:** Lemma 10 now states |M - a_eps - eps*sum w g| <= C_I eps^2 uniformly for d in I. The proof covers joint analyticity in (eps, d, M), the bound F_M <= -a/(a+d_1), a finite cover, and the coincidence of the root with M_mu by uniqueness.
   **C:** Lemma 10 and its proof.
5. **R (SOL §3):** Add the endpoint argument, both for two maxima and for the smooth approximants.
   **A:** Added: values exceed M(3) on both sides of 3, and both endpoint limits equal the mean. For approximants, nonconstancy gives M > the integral of m.
   **C:** Proof of Thm 2, "Two maxima" and "Smooth increasing versions".
6. **R (DA m3):** Remark 8 should say that M is nonconstant.  **A:** Clause added.  **C:** Remark 8.
7. **R (EIC m1):** Give the rate for fixed d.  **A:** Eq. (20) now reads O(R^{-1}).  **C:** Lemma 11.
8. **R (SOL §4; DA m1):** Three levels are minimal among finitely-valued laws.  **A:** Stated, with a one-line proof.  **C:** Thm 3 and its proof.
9. **R (SOL §2):** Make the trap margins explicit.  **A:** The inequalities 1/(8a), 3/(16a), 1/(16a) are shown. The bound r_{k+1} > 2r_k is recorded.  **C:** Lemma 12.

## Code and reproducibility

10. **R (METH m1):** Scripts overwrite the shipped JSON.
    **A:** Every script takes `--out` (default `output/`) and never writes a shipped receipt. The shipped receipts were replaced by clean-run outputs, deliberately.
    **C:** all scripts.
11. **R (METH m2):** The matrix fields in the fingerprints are hand-typed.
    **A:** Rank, trace, determinant, characteristic polynomial (Faddeev–LeVerrier) and eigenvalues (exact root division) are now computed in rational arithmetic.
    **C:** `resource_fingerprints.py`.
12. **R (METH m3):** Peak markers are hard-coded.
    **A:** Peaks are found by brentq on M' and written to `three_level_peaks.json`. The values agree with the previous ones to about 1e-9.
    **C:** `plot_population.py`; Fig. 1 caption.
13. **R (EIC verification):** Cancellation at large R.
    **A:** The kernel now uses t - 1 = (r - 1)/(1 + (h - z)/2).
    **C:** `plot_population.py`.
14. **R (METH m6; EIC m5; PERSP W6):** Record versions.
    **A:** `environment.json`: Python 3.11.14, NumPy 2.4.6, SciPy 1.17.1, Matplotlib 3.11.2. All scripts were rerun from a clean copy with `uv run python3 -I`. The meanfield audit output is identical to the original receipt.
    **C:** Declarations.

## Framing and effect sizes

15. **R (DA M1, M4; DOM m2; PERSP W1; EIC m3):** Report effect sizes.
    **A:** The text and Table 1 now give:
    - first maximum at d ≈ 1.989, M ≈ 1.000756;
    - minimum at d = 3, M = 1;
    - second maximum at d ≈ 15.08, M ≈ 1.0530;
    - relative depth ≈ 7.6e-4 (0.08%);
    - contrast 658, richest area 1/876.

    The text also says plainly that the result is qualitative.
    **C:** §4 "Effect sizes", Table 1, abstract, §6.
16. **R (DA M1; DOM m1):** The "near a constant" and L^p wording is misleading.
    **A:** Theorem 1 is retitled "...from rare rich patches". Its item 2 now states convergence in L^p but not uniform convergence, with contrast above 2^{N-1}. A new paragraph explains that the contrast grows without bound in N in the construction. It also cites Bai–Li's "exactly one maximum for perturbations" remark.
    **C:** Thm 1 and the paragraph after it.
17. **R (DOM m3, m5):** Admissible class and preprint status.  **A:** Both are stated in the text.  **C:** §2.
18. **R (EIC M2; DOM m4):** Monotonicity is cosmetic.  **A:** Stated after Theorem 1.  **C:** §2.

## Ecology, readability and literature

19. **R (PERSP W2, W3):** Give an ecological reading and practical points.
    **A:** New §6 covers:
    - the well-mixed pool (marine larvae, seeds, spores);
    - m as carrying capacity;
    - non-monotone responses, identifiability, rare rich patches, and the two-level rule;
    - the limits of the model.
    **C:** §2 (after eq. 1), §6.
20. **R (PERSP W4.1–8; brief):** Readability.
    **A:**
    - plain-language abstract;
    - motivating introduction with a roadmap;
    - glosses for d, m, A, D, the closure, t_r and g_r;
    - scaling law moved to §3;
    - "How the examples are found" paragraph;
    - intuitive sketch at the start of §5;
    - Fig. 1 discussed in the text;
    - Fig. 2 caption notes the epsilon scale.

    The "Status of this draft" paragraph is replaced by Declarations: author "Anonymous", AI provenance, literature caveats, and code availability, with no rating text.
    **C:** throughout.
21. **R (DOM M1; brief):** Liang–Zhang 2021.
    **A:** Cited, with the equivalence stated: equal-patch identical migration is the discrete analogue, and Theorem 2 is a 3504-patch example. Only the abstract was read. It concerns joint optimisation and does not report multiple maxima. This is described honestly as the closest priority risk, in the body and in Declarations.
    **C:** §7, Declarations.
22. **R (DOM M2; EIC m7; PERSP W2):** Programme references.
    **A:** Added Lou 2006, DeAngelis–Ni–Zhang 2016, Freedman–Waltman 1977, Arditi–Lobry–Sari 2015 and 2018, Elbetch et al. 2022 (Revista Integración), Nagylaki 2011 and Bravo de la Parra 2026. Every DOI, author list and title was taken from its Crossref record. Liang–Zhang, both Arditi papers and Bai–Li–Shi follow the coordinator's verified list.
    **C:** §2, §7, bibliography.
23. **R (DOM M3; SOL §6; brief):** Bai–Li–Shi 2024.
    **A:** Cited. The body and the Declarations both carry the sentence: "we found no subsequent resolution in the sources we could inspect; the full text of [BaiLiShi2024] was not available to us". They also note that only the abstract was read and that it does not report multiple maxima. "Answers" is kept for Bai–Li 2021, qualified by these caveats.
    **C:** §7 "Follow-up by the source authors", Declarations.

### Prior-art check: Arditi–Lobry–Sari (full texts supplied by the owner)

- **2015 (TPB 106, 45–59).**
  - The standard model is analysed for two patches only. The total population N_T*(beta) is either above the sum of carrying capacities, below it, or above at low migration and below at high migration (Fig. 1–2, Prop. 4). None of the curves shown has more than one interior maximum.
  - The mechanistic consumer–resource variant N_T**(beta) in Fig. 4 decreases, then increases, then decreases. That is still a single interior maximum, and it is a different model.
  - The Discussion leaves n > 2 patches as "a challenge for further work".
- **2018 (TPB 120, 11–15).** Two patches with asymmetric migration. In Prop. 2, N_T*(beta) either rises to one maximum and then falls, or stays on one side of K1 + K2.
- **Conclusion.** Neither paper shows or implies more than one local maximum in a setting that translates to ours. Neither treats complete-graph or identical migration with n >= 3 patches. No stop was needed. Both papers are described accordingly in §7.

## Extension: the contrast threshold

24. **R (DA M2; EIC M2; DOM ext 1; PERSP W5; brief):** Attack the gap between 1.618 and 658.
    **A:**
    - **New certified result.** Proposition 4 (label `prop:lowcontrast`) is a three-level law with d0 = 76/25 and theta = (1 - 1e-6, 1 + 1e-7, 57/5). It has an exact certificate M(d0) = 1, M'(d0) = 0 and M''(d0) ≈ 1.08e-21 > 0, with contrast **14173319160000/999994960001 ≈ 14.1734**. Every quantity is asserted in rational arithmetic by `contrast_witness.py`, whose output is `contrast_witness.json`.
    - **Numerical evidence, not certified.** A multistart SLSQP over all three-level laws found nothing below 14.17. Its iterates drift into a rare-patch limit. In that limit the condition reduces to two humps of c d/(1+d)^2 + g_R(d), which first occur at R* ≈ 14.1729 (`contrast_search.py`).
    - **No lower bound proved.** The interval 1.618 <= kappa_3 <= 14.1734 and the conjecture kappa_3 = R* are stated in Open problems.
    - **Construction bound.** Theorem 1's construction needs contrast above 2^{N-1}, which is proved. Whether contrast must grow with N is left open.

    **C:** Prop. 4 and its proof; §8; Table 1.

## Rejected or deferred

- **Transfer to convolution kernels, random diffusion, dispersal mortality, and prevalence surveys** (EIC, DOM, PERSP extensions). Deferred to Open problems. They are out of scope for a single revision round.
- **Four-level certificate and necessity of N+1 levels** (METH extensions). Listed as open.
- **Author enquiry or library access for Liang–Zhang and Bai–Li–Shi** (DOM M1, M3). Not possible in this round: the owner could not obtain the full texts. The disclosure is made instead.
- **Laboratory systems, e.g. Zhang et al.** (PERSP W2). Not cited, because they were not verified on Crossref in this round.
- **Gao–Lou parameter dictionary** (SOL §6). Gao–Lou's full text was not re-inspected. The text keeps its explicit statement that it claims no priority for the two-level formula.
