# Review summary (rating-free public record)

All review was internal and AI-assisted. The original reports are kept privately. This summary keeps the substance of the objections and how each was resolved, without any scores or ratings.

## Round 1 (first draft)

Five reviewer roles (editor, methodology, domain, perspective, devil's advocate) and an outside-model correctness audit raised these issues, among others:
- the arrangement of resource values in the smooth approximation;
- the order in which tolerances are chosen in the proof of Theorem 1;
- a uniform lower bound on the implicit denominator D;
- uniformity of the first-variation error;
- the endpoint argument;
- receipt and reproducibility hygiene;
- effect sizes;
- the ecological reading;
- related work (Liang-Zhang, Bai-Li-Shi, Arditi-Lobry-Sari, Gao-Lou).

Every item and its disposition is in [REVISION_RESPONSE.md](REVISION_RESPONSE.md).

## Verification of the revision

- **Re-review.** Every round-1 item was found addressed. Five small new defects were raised:
  - NEW-1: the Bai-Li 2021 arXiv citation had no DOI;
  - NEW-2: two scripts lacked declared dependencies;
  - NEW-3: the search receipt used 1500 starts against a default of 2000;
  - NEW-4: an unshipped private audit file contained a private editorial note;
  - NEW-5: the search wording and the "order 10^-14" effect size.

  All five are fixed ([FINAL_FIXES.md](FINAL_FIXES.md), items 4, 11-16).
- **Targeted proof audit.** Every audited item was found correct: Proposition 4 (independently certified in exact and 120-digit interval arithmetic), Theorem 2, the proof of Theorem 1, and Lemmas 7 and 10 and Remark 8. There was one minor gap, the undefined r_0 in Lemma 12, now fixed. Optional wording fixes covered "disjoint" traps, the two eta symbols and the patching sentence; all were applied. The audit also found the low-contrast witness quantitatively fragile, which is now stated in the paper.
- **Second outside-model audit.** It raised six points:
  1. the last sentence of Theorem 2 overstated what survives smooth approximation;
  2. the exact certificate of Proposition 4 was not displayed;
  3. the atomic law was not kept probabilistic;
  4. "not uniformly" was not proved;
  5. the base case of Lemma 12 was undefined;
  6. the finite-cover patching needed an argument.

  All six are fixed (FINAL_FIXES items 1, 2, 5-8). Its novelty points were already disclosed and remain open: read the Liang-Zhang and Bai-Li-Shi full texts, and note the finite complete-graph analogue.

## Remaining limitations

Priority is bounded by two abstract-only sources. The effects are tiny, and the result is qualitative. There was no human peer review.
