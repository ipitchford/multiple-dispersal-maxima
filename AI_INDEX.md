# Agent navigation

## Identity

- Release slug: `multiple-dispersal-maxima`. Version `1.0.0-candidate`, tag `v1.0.0-candidate`. DOI 10.5281/zenodo.23687852; concept DOI 10.5281/zenodo.23687851.
- Repository: https://github.com/ipitchford/multiple-dispersal-maxima. Release page: https://evidencepress.org/releases/multiple-dispersal-maxima/
- Scholarly creator: Anonymous. Status: unrefereed candidate ([STATUS.md](STATUS.md)).
- Manuscript: [PDF](multiple_dispersal_maxima.pdf) (16 pages) and its self-contained [LaTeX source](multiple_dispersal_maxima.tex).
- Machine-readable claims: [CLAIMS.json](CLAIMS.json). Human overview: [README.md](README.md).
- Assurance limits: [ASSURANCE.md](ASSURANCE.md). Review record: [REVIEW_SUMMARY.md](REVIEW_SUMMARY.md), [REVISION_RESPONSE.md](REVISION_RESPONSE.md), [FINAL_FIXES.md](FINAL_FIXES.md).
- Prior art and sources: [NOVELTY_AUDIT.md](NOVELTY_AUDIT.md), [target.yaml](target.yaml), [RESEARCH_GATES.json](RESEARCH_GATES.json), [SOURCES.md](SOURCES.md), [CITATION_AUDIT.md](CITATION_AUDIT.md). Provenance: [PROVENANCE.md](PROVENANCE.md).
- Citation: [CITATION.cff](CITATION.cff), [.zenodo.json](.zenodo.json). Licences: [LICENSES.md](LICENSES.md).

## Scientific map

Object: the positive equilibrium θ of d(M − θ) + θ(m − θ) = 0 on (0,1), with M = ∫θ. This is uniform global dispersal at rate d, with resource m. The curve d ↦ M_m(d) is the total population. Bai and Li (arXiv:2108.01826, Section 5) asked whether it can have several maxima.

- Scalar reduction (Section 3): M depends only on the law of m. The derivative formulas (15) and (17) and the pairwise identity (16) follow. The endpoint limits are M(0+) = M(∞) = mean of m (Lemma 6). Lemma 7 gives continuity under L¹ approximation. Remark 8 shows that analytic traps give strict maxima.
- Theorem 3: two levels give one peak, at d = (a+b)/2.
- Theorem 2: an exact three-level witness with a certified minimum at d = 3, giving two maxima. Smooth L¹-close increasing versions keep two maxima but not the exact identities.
- Proposition 4: the contrast-14.17 witness. It is certified exactly and by the traps (d0−1e−4, d0−1e−5, d0) and (d0, d0+1e−2, 3.1). It is extremely fragile.
- Theorem 1: rare rich patches add separated response kernels g_r (Lemmas 10–12). These are transferred to the nonlinear curve, then smoothed and normalised. The result is at least N maxima with m_j → a in every finite L^p.

## Evidence and replay

- Exact certificates: [audit_meanfield.py](audit_meanfield.py) → [meanfield_audit_result.json](meanfield_audit_result.json); [contrast_witness.py](contrast_witness.py) → [contrast_witness.json](contrast_witness.json); [interval_traps.py](interval_traps.py) → [interval_traps.json](interval_traps.json); [resource_fingerprints.py](resource_fingerprints.py) → [resource_fingerprints.json](resource_fingerprints.json). These use the standard library and `assert`, so do not use -O.
- Numerical: [plot_population.py](plot_population.py) → figures and [three_level_peaks.json](three_level_peaks.json); [contrast_search.py](contrast_search.py) → [contrast_search.json](contrast_search.json). Pinned dependencies are in [requirements.txt](requirements.txt) and in PEP 723 headers.
- [negative_controls.py](negative_controls.py) runs 20 controls. [compare_numeric.py](compare_numeric.py) compares numerical receipts; [check_search.py](check_search.py) checks the platform-sensitive search. CI: [.github/workflows/replay.yml](.github/workflows/replay.yml). Records: [REPLAY_RECEIPT.md](REPLAY_RECEIPT.md), [ENVIRONMENT.txt](ENVIRONMENT.txt), [environment.json](environment.json). Integrity: [SHA256SUMS](SHA256SUMS).

## Trust boundary

Review was internal and AI-assisted. There was no peer review, no independent reproduction and no formal verification. Priority holds only within a bounded search: Liang–Zhang 2021 and Bai–Li–Shi 2024 were read only as abstracts. The effects are tiny, and the result is qualitative.
