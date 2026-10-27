# Arbitrarily many population maxima under uniform global dispersal

**Unrefereed research candidate, version 1.0.0-candidate (27 October 2026).**
DOI: [10.5281/zenodo.23687852](https://doi.org/10.5281/zenodo.23687852) (concept DOI 10.5281/zenodo.23687851).
Release page: https://evidencepress.org/releases/multiple-dispersal-maxima/
Creator: Anonymous. Text and data CC0-1.0; code MIT.

## The question

Individuals leave their location at rate d and resettle anywhere in the habitat with equal probability. Bai and Li (arXiv:2108.01826, Section 5) proved that the total equilibrium population M(d) has a single peak in d when habitat quality varies by less than a factor of about 1.618, and asked whether several peaks are possible.

## The answer

Yes.

- **Theorem 1.** For every budget a > 0 and every N, there are smooth, strictly increasing resources with mean a whose population curve d -> M(d) has at least N distinct strict local maxima. These resources converge to a in every finite L^p. The rich patches shrink in area, not in height, and the contrast exceeds 2^(N-1).
- **Theorem 2.** An exact three-level example: resource 1/20, 25/12 and 329/10 on fractions 2405/3504, 5/16 and 1/876. It has an exactly certified nondegenerate population minimum at d = 3 (M = 1, M' = 0, M'' = 6042635/1975192401), and hence two strict maxima.
- **Theorem 3.** Two resource levels always give exactly one peak, so three levels are the minimum.
- **Proposition 4.** A three-level example with contrast about 14.17. It is certified exactly, and also by two rigorous interval traps.

**Effect sizes.** The peaks are real but tiny. In Theorem 2 the first peak rises about 7.6e-4 above the minimum. In Proposition 4 the left peak lies within 1e-4 of d0 = 3.04 and is about 1e-32 high, and it vanishes under tiny parameter changes. The result is qualitative: it shows that multiple maxima exist, not that they would be visible in a census.

## Files

- [multiple_dispersal_maxima.pdf](multiple_dispersal_maxima.pdf) (16 pages) and its LaTeX source [multiple_dispersal_maxima.tex](multiple_dispersal_maxima.tex).
- Exact certificates (standard library only): [audit_meanfield.py](audit_meanfield.py), [contrast_witness.py](contrast_witness.py), [interval_traps.py](interval_traps.py), [resource_fingerprints.py](resource_fingerprints.py). Their receipts are the matching `.json` files.
- Numerical illustrations and evidence (pinned numpy/scipy/matplotlib): [plot_population.py](plot_population.py) and [contrast_search.py](contrast_search.py).
- [negative_controls.py](negative_controls.py): 20 semantic controls.
- Records: [STATUS.md](STATUS.md), [ASSURANCE.md](ASSURANCE.md), [CLAIMS.json](CLAIMS.json), [REVIEW_SUMMARY.md](REVIEW_SUMMARY.md), [REVISION_RESPONSE.md](REVISION_RESPONSE.md), [FINAL_FIXES.md](FINAL_FIXES.md), [NOVELTY_AUDIT.md](NOVELTY_AUDIT.md), [RESEARCH_GATES.json](RESEARCH_GATES.json), [SOURCES.md](SOURCES.md), [CITATION_AUDIT.md](CITATION_AUDIT.md), [PROVENANCE.md](PROVENANCE.md), [AI_INDEX.md](AI_INDEX.md).

## Replay

```sh
for s in audit_meanfield contrast_witness resource_fingerprints interval_traps; do uv run python3 -I $s.py --out output; done
uv run --no-project --with numpy==2.4.6 --with scipy==1.17.1 --with matplotlib==3.11.2 python3 -I plot_population.py --out output
uv run --no-project --with numpy==2.4.6 --with scipy==1.17.1 --with matplotlib==3.11.2 python3 -I contrast_search.py --out output
uv run python3 -I negative_controls.py
```

Do not use `python -O`: the certificates rely on `assert`. Scripts never overwrite the shipped receipts. See [REPLAY_RECEIPT.md](REPLAY_RECEIPT.md).

## Priority caveat

Two close sources were read only as abstracts: Liang and Zhang (DCDS-B 2021, doi:10.3934/dcdsb.2020280), whose equal-patch model contains our rational examples, and Bai, Li and Shi (J. Math. Study 2024, doi:10.4208/jms.v57n3.24.04). Neither abstract reports multiple maxima. Their full texts were not available, so priority is stated only within the recorded bounded search.
