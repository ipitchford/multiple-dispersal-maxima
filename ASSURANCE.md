# Assurance boundary

## What was done

1. **Written proofs.** The theorems are proved in [multiple_dispersal_maxima.tex](multiple_dispersal_maxima.tex). Load-bearing identities are certified in exact rational arithmetic ([contrast_witness.py](contrast_witness.py) and [audit_meanfield.py](audit_meanfield.py), written independently). The traps of Proposition 4 are certified by rational square-root enclosures ([interval_traps.py](interval_traps.py)).
2. **Internal AI-assisted review.** A first-round review by an editor and by methodology, domain, perspective and devil's-advocate reviewers, plus an outside-model correctness audit. Each finding has a disposition in [REVISION_RESPONSE.md](REVISION_RESPONSE.md). The revision then had a verification re-review, a targeted proof audit with independent 120-digit interval arithmetic, and a second outside-model audit. The final editor fixes are in [FINAL_FIXES.md](FINAL_FIXES.md); they had no further review round. [REVIEW_SUMMARY.md](REVIEW_SUMMARY.md) gives a rating-free summary.
3. **Replay.** All scripts were rerun from a clean copy, and the exact receipts were byte-identical. CI replays them on Linux. [negative_controls.py](negative_controls.py) has 20 controls: perturbed witnesses, reversed trap claims and tampered receipts must all be rejected.
4. **Citations.** Every DOI was resolved, and its Crossref (or, for arXiv, DataCite) record was matched by title, first author and year ([CITATION_AUDIT.md](CITATION_AUDIT.md)). The two Arditi-Lobry-Sari papers and Bai-Li 2021 were read in full.

## What was not done

- No human specialist review or journal peer review. No independent reproduction by an unaffiliated party. No proof-assistant formalisation.
- **Priority is bounded.** The full texts of Liang-Zhang 2021 and Bai-Li-Shi 2024 were not available; only their abstracts were read. Liang-Zhang's equal-patch model contains our rational examples. See [NOVELTY_AUDIT.md](NOVELTY_AUDIT.md) and [RESEARCH_GATES.json](RESEARCH_GATES.json).
- **Effect sizes are tiny.** The low-contrast example is quantitatively fragile. Its existence is rigorous, but its left maximum is about 1e-32 high.

Agreement between AI reviewers is not independent evidence. All review here was internal AI-assisted checking.
