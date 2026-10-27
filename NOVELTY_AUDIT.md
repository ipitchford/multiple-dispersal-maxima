# Novelty-gate report: population maxima under uniform global dispersal

**Search date:** 20 October 2026.  
**Researcher/agent:** Mathematical construction and literature agent, with independent checks by the numerical/review agent and parent researcher.  
**Corpus boundary:** Public primary papers, available author texts, journal abstracts and previews, two web search engines, arXiv, OEIS, and the public EvidencePress index. This was not a subscription-database census or an author enquiry.  
**Intended contribution unit:** A theorem and complete proof, with an exact arithmetic verification artifact.

**Decision: BOUNDED UNCERTAINTY concerning historical priority.** The exact originating question and model were verified in full primary text, and no earlier statement or proof of the frozen theorem was found in the recorded search. Several especially relevant adjacent papers were available only as abstracts or previews. The theorem is proved in the accompanying manuscript; historical novelty remains qualified by these access limits.

## 1. Frozen claim

For every positive budget \(a\) and integer \(N\geq1\), there is a sequence of positive \(C^\infty\) resource functions on \([0,1]\), each with strictly positive derivative and mean \(a\), that converges to \(a\) in every finite \(L^p\) while the corresponding equilibrium population has at least \(N\) distinct strict local maxima as a function of the single dispersal rate \(d\).

The model is exactly

\[
 d(M-\theta)+\theta(m-\theta)=0,\qquad
 M=\int_0^1\theta(x)\,dx,\qquad d>0.
\]

Before smoothing, \(N+1\) resource levels suffice. A three-level rational witness has a nondegenerate population minimum at \(d=3\), hence at least two strict local maxima. Every positive two-level law has one maximum, so three resource levels are minimal for the two-maxima phenomenon.

The claim concerns local maxima, without requiring equal heights. It does not concern independently variable local competition coefficients, a changing mixing operator, arbitrary kernels, infinitely many maxima for one bounded resource, a contrast bound independent of \(N\), or \(L^\infty\) closeness to a constant. The two-level classification, quadratic root formula, resource concentration as a general method, and multimodality of unrestricted positive mixtures are not advertised as new.

The statement, exclusions, formulas and aliases are frozen in target.yaml. The final structural rerun used the first-variation kernel and its eliminated quadratic equation, in addition to the original population model.

## 2. Normalisation and verified translations

| Original or adjacent formulation | Canonical formulation | Verified relationship |
|---|---|---|
| Bai–Li (2021), Eq. (1.11), spatial average | Unit interval, \(M=\int\theta\) | Habitat measure is fixed to one; the equation agrees exactly. |
| Uniform global dispersal | \(d(P-I)\), \(P_{ij}=p_j\) on resource classes | \(P\theta=\mathbf1\sum_jp_j\theta_j\). |
| Density in a class of area \(p_i\) | Abundance \(x_i=p_i\theta_i\) | \(\dot x_i=x_i(m_i-x_i/p_i)+d(p_i\sum_jx_j-x_i)\). Both migration and competition coefficients transform. |
| Complete graph with equal patches | Repeated resource classes | Rational \(p_i\) can be realised by repeating equal-area patches. The rational witness has 3504 equal subpatches in three classes; it is not a claim of three equal patches. |
| Change of resource budget | \(m\mapsto cm\) | \(M_{cm}(d)=cM_m(d/c)\), preserving all local maxima. |
| Rearrangement of a resource field | Same probability law \(\mu\) | The scalar closure depends only on \(\mu\), permitting increasing smooth realisations on a connected interval. |
| Small-amplitude resource perturbation | \(m=a+\varepsilon f\) | Different from rare-mass perturbation. Finite-\(L^p\) closeness does not imply small pointwise contrast. |

These translations rule out a false shortcut: a three-patch example with arbitrary intrinsic growth, carrying capacity and migration coefficients is not automatically an example in the present restricted class.

## 3. Exact fingerprints

### Three finite instances

All three instances below have \(d=3\), \(M=1\), and \(M'=0\), with equilibrium values \((4/5,4/3,v)\). Their probabilities solve

\[
 \sum_i p_i=1,\qquad \sum_i p_i\theta_i=1,\qquad
 \sum_i p_i\,\frac{\theta_i(1-\theta_i)}{\theta_i^2+3}=0.
\]

The resource values are \(m_i=\theta_i+3-3/\theta_i\).

| \(v\) | Resource values | Probabilities | Exact \(M''(3)>0\) |
|---:|---|---|---|
| 30 | \(1/20,\ 25/12,\ 329/10\) | \(2405/3504,\ 5/16,\ 1/876\) | \(6042635/1975192401\) |
| 50 | \(1/20,\ 25/12,\ 2647/50\) | \(4258345/6232656,\ 1169385/3699056,\ 72587/113745972\) | \(3428551838255/882921021075379\) |
| 100 | \(1/20,\ 25/12,\ 10297/100\) | \(2516085/3694208,\ 702405/2204608,\ 41441/136685696\) | \(18416996060265/4136157806939522\) |

The program resource_fingerprints.py reproduces these with Python standard-library fractions and no numerical root finder. Its JSON output records common integer scalings, full rank-one mixing matrices, canonical and transpose hashes, signs, row sums and spectra. For each three-class matrix \(P\), the rank is one, trace one, determinant zero, and characteristic polynomial \(\lambda^2(\lambda-1)\). At \(d=3\), the generator has characteristic polynomial \(\lambda(\lambda+3)^2\). These familiar invariants are identity checks, not novelty claims.

The discovery calculation initially used a finite linear program for the probability weights at a prescribed stationary mean. That exploratory calculation was replaced by the exact three-equation system above. The program audit_meanfield.py is an independently written rational verifier of the main certificate.

### Algebraic response kernel and sequence

Perturb a constant law by rare high-resource atoms:

\[
 \mu_\varepsilon=(1-\varepsilon W)\delta_a+
       \varepsilon\sum_iw_i\delta_{r_i},\quad W=\sum_iw_i,\quad r_i>a.
\]

The first variation, after subtracting the resource mean, is

\[
 M_{\mu_\varepsilon}(d)-\mathbb E_{\mu_\varepsilon}m
 =\varepsilon\sum_iw_i g_{r_i}(d)+O(\varepsilon^2),\quad
 g_r(d)=\frac{d(t_r-a)^2}{a t_r},\quad
 t_r=\frac{r-d+\sqrt{(r-d)^2+4ad}}2.
\]

Eliminating \(t_r\) gives

\[
 a g^2+[d^2+(3a-r)d+ar]g-d(r-a)^2=0,\qquad g(0)=0.
\]

For \(a=1,r=2\), the coefficients of \(g\), starting at degree zero, are

\[
 0,\frac12,-\frac38,\frac18,-\frac1{128},-\frac1{128},
 \frac1{1024},\frac1{1024},-\frac5{32768},-\frac5{32768},
 \frac7{262144},\frac7{262144},-\frac{21}{4194304}.
\]

The underlying even coefficients of \(t=1-d/2+\sqrt{1+d^2/4}\) reduce to alternating Catalan numbers:
\([d^{2k}]t=(-1)^{k-1}C_{k-1}/2^{4k-1}\).
This standard identity matches [OEIS A000108](https://oeis.org/A000108). No new sequence, special function or generating-function identity is claimed.

The load-bearing limits are
\(R^{-2}g_R(d)\to0\) for fixed \(d\),
\(R^{-2}g_R(sR)\to s(1-s)/a\) for \(0<s<1\), and
\(R^{-2}g_R(R)\to0\).
They permit positive kernel sums to retain old strict population-value inequalities while adding new ones. The nonlinear theorem also requires first-variation passage, smooth approximation and budget normalisation; it does not follow merely from a generic fact about mixtures.

## 4. Alias map

| Analysis | Probability | Combinatorics | Mathematical physics | Optimisation and statistics |
|---|---|---|---|---|
| Uniform nonlocal logistic equation; global mixing | Resource probability law; rare atoms | Complete graph; repeated resource classes | Globally coupled logistic units | Biomass versus migration intensity |
| Scalar equilibrium closure | Rank-one reset generator; island migration | Rank-one averaging matrix | Mean-field reaction equation | Positive mixtures and multiple local optima |
| Algebraic first-variation kernels | Identical migration; global panmixia | Catalan square-root coefficients | Separation of relaxation scales | Fixed-resource dispersal optimisation |

Queries involving logistic maps, synchronisation and temporal oscillations returned unrelated results. Maxima over time, attractor bifurcations and likelihood maxima are different observables from the stationary population curve.

## 5. Primary sources and closest adjacent work

### A. Originating question: full primary text inspected

Xueli Bai and Fang Li, *Effects of nonlocal dispersal strategies and heterogeneous environment on total population*, arXiv:2108.01826v1, 4 August 2021.

- [Primary abstract](https://arxiv.org/abs/2108.01826)
- [Complete primary PDF](https://arxiv.org/pdf/2108.01826)

Equation (1.11), printed p.7, is the uniform averaging model. Assumption (M) permits nonnegative, nonconstant \(L^\infty\) resources. Theorem 1.5 proves unimodality below a golden-ratio pointwise contrast bound. Section 5, printed p.20, explicitly asks whether the model permits multiple population maxima. The exact quotation is in the manuscript and is not duplicated here. The source is a preprint; this audit does not silently promote it to a verified journal publication. Its full text was checked independently by two agents.

### B. Concentrated-resource optimisation: full primary preprint inspected

Xueli Bai, Fang Li and Maolin Zhou, *Optimization of total population in logistic model with nonlocal dispersals and heterogeneous environments*, Calculus of Variations and PDE 62, 169 (2023), DOI [10.1007/s00526-023-02509-3](https://doi.org/10.1007/s00526-023-02509-3). The preprint title uses “Optimisation”.

- [Primary preprint, arXiv:2208.14335](https://arxiv.org/abs/2208.14335)
- [Full primary PDF](https://arxiv.org/pdf/2208.14335)

Theorems 1.2–1.3 concern the best total population as resources and dispersal rate vary jointly at fixed resource budget. They establish order-\(\sqrt d\) growth and a concentration criterion; Section 4.2 gives high-resource small-patch examples. Resource concentration is therefore established methodology and is credited. The introduction's nonunique-maximum remark refers to the local-diffusion paper below. No fixed-resource arbitrary-number-of-maxima or finite-\(L^p\) approximation theorem was found in the inspected text.

### C. Local diffusion: known counterexamples, different operator

Song Liang and Yuan Lou, *On the dependence of population size upon random dispersal rate*, DCDS-B 17 (2012), 2771–2788, DOI [10.3934/dcdsb.2012.17.2771](https://www.aimsciences.org/article/doi/10.3934/dcdsb.2012.17.2771).

The primary abstract explicitly gives at least two local population maxima for near-constant resources in the Neumann Laplacian model. This is genuine prior work and caused the local-diffusion candidate to be discarded. The present manuscript retains only the different uniform averaging problem. These dispersal operators cannot be interchanged.

### D. Identical migration optimisation: important access limitation

Xing Liang and Lei Zhang, *The optimal distribution of resources and rate of migration maximizing the population size in logistic model with identical migration*, DCDS-B 26 (2021), 2055–2065, DOI [10.3934/dcdsb.2020280](https://www.aimsciences.org/article/doi/10.3934/dcdsb.2020280).

The primary abstract/intro concern joint optimisation under identical migration. This is a close object-level neighbour, not dismissed merely because its title says optimisation. The author's [publication page](https://mathzhanglei.github.io/research.html) links the DOI. The journal's full-HTML link led to an actual login/payment restriction; no attempt was made to bypass it. The two-level maximum formula might overlap this work. No original priority is claimed for that supporting formula. A full-text comparison remains desirable before external publication.

### E. Two-patch classification: abstract inspected

Daozhou Gao and Yuan Lou, *Total biomass of a single population in two-patch environments*, Theoretical Population Biology 146 (2022), 1–14, DOI [10.1016/j.tpb.2022.05.003](https://doi.org/10.1016/j.tpb.2022.05.003).

The [primary abstract](https://pubmed.ncbi.nlm.nih.gov/35654290/) states a complete classification of biomass responses in the general two-patch setting and further optimisation results. The full article was not obtained. The manuscript cites this classification and gives its elementary specialization to prove the minimum number of resource levels. It does not claim a new general two-patch classification.

### F. Recent survey: abstract and two-page preview only

Xueli Bai, Fang Li and Jiale Shi, *Some Progress on Single Species Models with Nonlocal Dispersal Strategies in Heterogeneous Environments*, Journal of Mathematical Study 57 (2024), 294–308, DOI [10.4208/jms.v57n3.24.04](https://journal.hep.com.cn/joms/EN/10.4208/jms.v57n3.24.04).

- [Primary journal page](https://www.global-sci.com/jms/article/view/13474)
- [Indexed PDF endpoint](https://global-sci.com/index.php/jms/article/download/13474/26856)

The abstract describes a new monotonicity result under conditions on resources. The complete PDF endpoint was unavailable; another endpoint and independent retrieval exposed only two pages. Neither full theorem statements nor discussion were inspected. This limitation is explicit because this is close author-level prior art. A 2026 mirror migration date is not treated as publication date.

### G. General multipatch logistic models: full relevant primary texts inspected

B. Elbetch, T. Benzekri, D. Massart and T. Sari, *The multi-patch logistic equation with asymmetric migration*, arXiv:2103.13144v3; published 2022, DOI [10.18273/revint.v40n1-2022002](https://doi.org/10.18273/revint.v40n1-2022002).

[Primary full text](https://arxiv.org/html/2103.13144v3) contains complex three-patch responses, including multiple crossings of the aggregate carrying-capacity baseline. Its migration matrix and growth/competition ratios are general. Our model always lies strictly above its resource-mean baseline, so those crossing examples cannot be imported unchanged. This is a verified parameter/observable distinction, not a claim that the wider literature has no related extrema.

Juan Segura, Marcos Marvá and Daniel Franco, *Dispersal in multi-patch metapopulations: The impact of patch number and network topology*, Journal of Theoretical Biology 619 (2026), 112331, DOI [10.1016/j.jtbi.2025.112331](https://doi.org/10.1016/j.jtbi.2025.112331).

The complete [author-posted text](https://www.researchgate.net/publication/398256016_Dispersal_in_multi-patch_metapopulations_the_impact_of_patch_number_and_network_topology) was inspected. Its general patch model permits independent growth and carrying-capacity parameters, and its three-patch response classifications are numerical. Appendix B lists the example parameters. Our common-quadratic, resource-weighted mixing constraints are not automatically satisfied. No arbitrary-\(N\), fixed-resource, near-constant finite-\(L^p\) theorem was found. It is cited to avoid claiming novelty for complex biomass responses in unrestricted patch systems.

### H. Current discrete-time paper: independently checked

Rafael Bravo de la Parra, *Dispersal and Total Population Size in Discrete-Time Metapopulation Models*, Mathematics 14 (2026), 3624, published 6 October 2026, DOI [10.3390/math14193624](https://www.mdpi.com/2227-7390/14/19/3624).

The review agent obtained the complete primary HTML through the search connector after direct fetch returned HTTP 429. The paper treats stability, fast-dispersal comparisons and a two-patch Beverton–Holt case. Its introduction distinguishes its approach from classification of response curves as dispersal varies. No present arbitrary-local-maxima claim was found. Discrete-time models are not assumed equivalent without checking their equilibrium equations.

### I. Thesis lead: secondary abstract only

A secondary index lists *The Dependence Of Population Size Upon Nonlocal Dispersal Rate Of A Nonlocal Biological Model*:
[GlobeThesis record](https://www.globethesis.com/?t=2180330461475709).
Its abstract describes numerical searches for multiple maxima and confidence bounds that appear consistent with unsuccessful sampling. The author, institution, original-language full thesis and exact equations have not been independently established. Consequently it neither clears priority nor establishes a collision. It remains a specialist literature lead.

## 6. Search log

All entries were searched on 20 October 2026. Exact quoted queries sometimes returned loosely matching unrelated pages; these were not treated as exact matches. Both engines were used when the lower-cost engine missed identifiable primary sources.

| Family | Exact queries or source operations | Consequence |
|---|---|---|
| Origin | "2108.01826" maxima; "Effects of nonlocal dispersal strategies" "Bai" 2026; nonlocal logistic population dispersal rate multiple local maxima Bai Li | Full model and question verified; later adjacent sources examined. |
| Uniform model | "nonlocal" "multiple maxima" "population"; "uniform dispersal" "population" "maxima"; "uniform mixing" "logistic" population maxima; "uniform nonlocal" "multiple maxima" | No exact-result collision found; different operators separated. |
| Global/mean-field aliases | "global mixing" logistic "maxima"; "global panmixia" "population" maximum; nonlocal logistic multiple maxima dispersal rate global panmixia meanfield; "mean field" "logistic" "multiple maxima" | Genetics and temporal maps appeared; no verified identity with frozen result. |
| Patch aliases | logistic patch model total population multiple maxima complete mixing; total biomass diffusion rate three patches unimodal; logistic all-to-all migration total biomass several local maxima; "complete graph" "logistic" "multiple maxima" | Gao–Lou, Elbetch et al., Segura et al. compared above. |
| Identical migration | Exact Liang–Zhang title; "identical migration" "multiple"; "identical migration" "unimodal"; "identical migration" "unique"; "dcdsb.2020280" pdf; "Liang" "Zhang" "identical migration" "Theorem" | Abstract, author page and actual full-text paywall recorded. |
| Survey | "Some Progress on Single Species Models" nonlocal pdf; "Some Progress on Single Species Models" "maximum"; Bai Li Shi nonlocal total population monotonicity 2024 2025 2026 | Abstract/two-page preview only; missingness retained. |
| Strong theorem rerun | "nonlocal dispersal" "arbitrarily many"; "arbitrarily many" "dispersal" "maxima"; "population" "maxima" "global panmixia"; "nonlocal" "population" "Lp" dispersal | No matching theorem in returned corpus. |
| First variation rerun | "total biomass" "linear response"; "identical migration" "linear response" logistic; "logistic" "response kernel" dispersal; "total population" "rare" "resource" "dispersal" | Concentration work recognised and credited; no arbitrary-N theorem located. |
| Algebraic rerun | "population" "d^2+(3a"; "logistic" "d²" "3a" "population"; "total biomass" "positive mixtures" | Formula indexing recall poor; no exact match found. |
| Exact instances | "6042635" "1975192401"; "2405/3504" "population"; "population" "3428551838255"; "3428551838255" "18416996060265" | Unrelated number/index pages or no relevant result; not proof of theorem priority. |
| Sequence | "1/2, -3/8, 1/8, -1/128"; "1/128" "1/1024" "logistic"; site:oeis.org "1, 1, 2, 5, 14, 42, 132" Catalan | Catalan square-root identity identified; no new-sequence claim. |
| Physics aliases | "globally coupled logistic" "maxima"; "rank-one" "logistic" "population"; logistic "global dispersal" "critical points" | Map dynamics and statistical models; no verified fixed-equilibrium identity. |
| Current paper | "Dispersal and Total Population Size in Discrete-Time"; full primary HTML independently retrieved | Recent discrete-time paper has complementary scope. |
| Duplicate release | site:evidencepress.org dispersal population; "population" "maxima" "evidencepress"; public-index find operations for dispersal and maxima | No matching index entry; attachments and unindexed releases not exhaustively searched. |

The [EvidencePress public index](https://evidencepress.org/) was retrieved on the search date. Findings about unrelated releases are not clearance of this theorem.

## 7. Collisions, non-collisions and missingness

**Verified prior content:** the model, positive-equilibrium problem, limited-contrast unimodality, concentrated-resource optimisation, general two-patch classification and local-diffusion multiple maxima already exist. The manuscript acknowledges these.

**No verified collision with the frozen theorem:** no arbitrary-\(N\) statement in the exact uniform-mixing/common-quadratic class, or its fixed-budget, strictly increasing smooth, finite-\(L^p\) strengthening, was found in the inspected sources.

**Limits:** full Liang–Zhang2021, Gao–Lou2022 and Bai–Li–Shi2024 texts were unavailable; the thesis lead lacks a primary identity; CNKI and subscription thesis databases were not searched comprehensively; non-English coverage was incomplete; equation and fraction indexing has low recall; no authors were contacted. No inaccessible source is declared non-colliding solely from an abstract.

The 2021 question establishes an explicit historical question. It does not by itself establish that nobody answered it between 2021 and this search date.

## 8. Outcome by contribution unit

| Unit | Outcome | Assessment | Allowed wording | Forbidden wording |
|---|---|---|---|---|
| Arbitrary-\(N\)/finite-\(L^p\) statement | BOUNDED UNCERTAINTY | No collision found; close missing full texts remain | We prove the specified theorem; answers the question posed in Bai–Li2021; no prior result found in the reported bounded search | First ever; proved historically novel; nobody has solved this |
| Complete proof | CLEAR TO PROVE within boundary | Supplied and independently audited | A complete proof is provided; describe its mechanism | The first proof |
| Two-level classification | Prior content likely overlaps; not claimed original | General two-patch classification established | For completeness, the required specialization is proved | New general two-patch classification |
| Scalar root, rank-one matrix, Catalan identity | COLLISION with standard objects | Known supporting tools/fingerprints | Exact formulas as calculations | New special function or averaging process |
| Rational witnesses and verifier | CLEAR within boundary | Three instances checked exactly; no literal match found | Explicit rational certificate; independently recomputed | Historically unique parameters |
| Exposition and smooth realisation | Part of theorem proof | Continuity and scaling proved | Quantified persistence in stated topology | Assertion for arbitrary mixing kernels |

## 9. Decision and continuation

The target was well defined, the source inspectable, and no decisive collision appeared. The mathematical result is complete and independently checked. **Historical priority remains under bounded uncertainty**, especially pending legitimate full-text comparisons of the three close sources and identification of the thesis. These limits affect originality assessment, not validity of the proof.

No external messages, submissions or author enquiries were sent. Remaining bibliographic comparisons do not require rerunning the mathematical search or proofs.

## 10. Rerun triggers

The gate was rerun after scalar closure, the exact witness, arbitrary-scale rare atoms, and the final first-variation algebraic kernel. A further rerun is required if a source identifies this response family under another name; a full identical-migration paper discusses its number of maxima; the primary thesis appears; or the theorem is broadened to fixed contrast, another kernel, equal-height global maxima, or further minimal-level claims.

## 11. Final bounded primary-copy follow-up

A final limited search on the same date tried author/institutional routes,
without repeating the unavailable publisher PDF downloads:

- "Some Progress on Single Species" "Shi" pdf;
- "Bai" "Li" "Shi" "2024" "nonlocal" site:wm.edu;
- "Liang" "Zhang" "identical migration" filetype:pdf;
- "Some Progress" "Jiale Shi" pdf;
- "Xing Liang" "Lei Zhang" "resources" university pdf.

The primary survey metadata establishes that its third author is **Jiale
Shi**, at Sun Yat-sen University; the earlier expanded name in this audit
was corrected. No author or institutional full copy of the two target
papers was found.

The search also exposed a new accepted-manuscript route for Gao–Lou2022,
https://www.sciencedirect.com/science/article/am/pii/S0040580922000326 .
Direct access returned HTTP403; the independent public-text extractor
returned only a ScienceDirect landing title. A 2026 AIMS conference
abstract with the survey title was indexed, but its page returned HTTP401.
Neither was treated as an inspected full text. This follow-up therefore
does not change the missingness assessment or the bounded-uncertainty
decision. No manuscript claim was altered.
