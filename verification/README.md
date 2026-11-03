# Reproducing the finite checks

[Overview](../README.md) · [Converse proof](../science/precision_bound.md) · [Construction proof](../science/achievability.md)

The analytical statements hold for all finite dimensions under their stated assumptions. The checks here test independent implementations and boundary cases; they do not infer a general theorem from a finite sweep.

## Run

Use Python 3.10 or later from the repository root:

```bash
python -m pip install -r verification/requirements.txt
python verification/run_checks.py --output verification/results.json
```

The script uses dense linear algebra, NumPy and SciPy. It does not download data, sample trajectories or require a GPU. The random seed is fixed at `70905`; the output records the numerical-library versions. [results.json](results.json) contains the recorded run, including every tested parameter case and summary residuals.

## What is checked

| Calculation | Cases and purpose |
|---|---|
| Stationary tilted-generator cumulants | Real and complex random Hamiltonians in dimensions 2, 3, 4, 6 and 8, plus perfect-transfer chains; compare the variance rate with the affinity envelope. |
| No-count absorption resolvent | Independently evaluate the two-port transfer matrix; check integrated reciprocity, positive semidefiniteness and the consecutive-forward ceiling. |
| Nonorthogonal endpoints | Sixteen random examples in dimensions 2 and 4; test the algebraic endpoint extension. |
| Unobserved unital noise | Eight dephasing examples in dimensions 3 and 5; test the extended no-count generator. |
| Coincident labeled endpoints | Two exactly Poisson cases; verify the signed-count Fano factor against its closed form. |
| Exceptional-point determinant | Exact rational tridiagonal recurrences for dimensions 2 through 30, compared with the binomial coefficients of the repeated-root polynomial. |
| Finite-bias construction | Dimensions 2, 3, 4, 5, 8 and 12, at zero reverse rate and at the stated positive reverse rate; check Erlang moments, the perturbation envelope and tick-rate bounds. |
| Independent variance representations | For every construction case, compare stationary tilted-generator derivatives with the positive-tick renewal-block moment formula. |

The converse suite has 195 cases, and the construction suite has 12 cases. The rational recurrence checks use exact arithmetic; the remaining checks use double precision. Tolerances are stated in the script and are loose relative to the recorded residuals. Very large dimensions or reverse rates extremely close to one can require higher precision or sparse algorithms and are not certified by this run.

## Numerical conventions

The superoperators use column vectorization. For a matrix $X$, `vec(X)` stacks columns; hence $AXB$ is represented by $B^{\mathsf T}\otimes A$. The forward rate is set to one. A counted jump is represented by $J^*\otimes J$.

For stationary cumulants, the script solves the normalized steady-state equation and its first tilted derivative. If $\mathcal L_s$ weights positive jumps by $e^s$ and negative jumps by $e^{-s}$, then

$$
j=\operatorname{tr}(\mathcal L'_0\rho_{\rm ss}),
\qquad
D=\operatorname{tr}(\mathcal L''_0\rho_{\rm ss}+2\mathcal L'_0\rho'_0).
$$

Here $\rho'_0$ solves

$$
\mathcal L\rho'_0=-(\mathcal L'_0-jI)\rho_{\rm ss},
\qquad \operatorname{tr}\rho'_0=0.
$$

There is no numerical differentiation of eigenvalues. The independent block calculation kills only positive ticks and retains negative jumps inside each interval, as derived in the [construction](../science/achievability.md).

These checks do not establish a microscopic thermal realization, the optimal coefficient of the logarithmic law, a universal bound for other clock architectures, or actual hosted mathematical rendering. Those are separate statements with separate evidence.

## Hosted mathematical display

The [hosted-rendering check](hosted/README.md) compares the exact committed Markdown expressions with their actual GitHub rendering at desktop and narrow viewport widths. Its workflow retains the source inventory, comparison report and screenshots for a separate visual review. This checks presentation of the scientific account and learning route; it does not replace the analytical or numerical checks above.
