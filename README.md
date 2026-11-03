# Quantum Clock Entropy Limits

How much reset bias is needed to sustain a precise quantum clock? Coherent dynamics can greatly improve tick regularity, but a finite reverse rate remains a source of fluctuations. This repository establishes a dimension-independent precision ceiling for a clock with one complete reset interface and gives a finite-bias construction with logarithmic affinity cost.

## Main result

Let a finite-dimensional clock evolve under a time-independent Hermitian Hamiltonian and the jump pair

$$
J_+=\sqrt{\Gamma}\,|a\rangle\langle b|,
\qquad
J_-=\sqrt{\Gamma r}\,|b\rangle\langle a|,
\qquad r=e^{-\Sigma}\in(0,1).
$$

Each counted jump resets the **entire clockwork**. For the signed count $N(t)=N_+(t)-N_-(t)$, define the positive stationary current $j$, variance rate $D$ and precision by

$$
j=\lim_{t\to\infty}\frac{\mathbb E N(t)}{t},
\qquad
D=\lim_{t\to\infty}\frac{\operatorname{Var}N(t)}{t},
\qquad
\mathcal P=\frac{j}{D}.
$$

On the recurrent ticking sector, the [precision theorem](science/precision_bound.md) gives

$$
\boxed{\mathcal P\le e^{2\Sigma}\tanh(\Sigma/2).}
$$

The bound is uniform over the Hilbert-space dimension, Hamiltonian spectrum, coherent couplings and complex phases. A [bounded-strength chain](science/achievability.md) achieves $\mathcal P\ge d$ at $\Sigma=3\log d+16\log 2$. Consequently, for desired precision $P\ge2$,

$$
\frac12\log P
\le \Sigma_{\min}(P)
\le 3\log\lceil P\rceil+16\log2.
$$

Thus the optimal cost has logarithmic order in this architecture. The coefficients are not sharp. At fixed forward jump rate, the construction has net tick rate $j=\Theta(d^{-2})$: its increasing precision comes with slower operation.

## Meaning and scope

$\Sigma$ is exactly the logarithm of the jump-rate ratio. Its interpretation as reservoir entropy per **net** tick, in units of $k_{\mathrm B}$, requires a locally detailed-balanced, tightly coupled implementation. The [thermodynamic interface](science/thermodynamic_interface.md) explains that identification and its physical limits.

The figure of merit concerns the signed current. It is not the optimal estimator obtainable from every detail of the timing record. Higher-rank resets, quantum memory retained after a tick and multiple counted jump pairs require different arguments. A proved [extension](science/extensions.md) allows unobserved unital noise between ticks when its operating sector is stable; this does not assign that noise zero thermodynamic cost.

The exponential quantum precision advantage was demonstrated by [Meier et al.](references/README.md#m25). The ideal exceptional-point Erlang escape law is inherited from [Holst, Blasi and Khandelwal](references/README.md#hbk26). The added result here is the affinity-only converse and a controlled finite-reverse-rate construction establishing logarithmic optimal cost. The [comparison with prior work](references/related_work.md) states the operational distinctions.

## Reading routes

| Question | Authoritative account |
|---|---|
| What is the clock, and what is charged? | [Model and observables](science/model.md) |
| Why does finite affinity impose a ceiling? | [Precision bound](science/precision_bound.md) |
| Can logarithmic affinity cost be attained? | [Finite-bias construction](science/achievability.md) |
| Which noise and boundary cases are covered? | [Extensions and boundaries](science/extensions.md) |
| When is affinity physical entropy? | [Thermodynamic interface](science/thermodynamic_interface.md) |
| What is inherited, and what is added? | [Related work](references/related_work.md) and [sources](references/README.md) |
| How can I build the prerequisites and follow the argument? | [Learning bridge](learning/anchor.md), [tutorial](learning/tutorial.md) and [30 milestones](learning/milestones.md) |
| How can the calculations be reproduced? | [Verification](verification/README.md) |

The proof combines a two-port absorption constraint with a renewal-reward calculation. It keeps the correlations between tick direction and waiting time. The construction uses a norm estimate for emitted wavepackets to control reverse ticks without relying on eigenvalue perturbation near a high-order exceptional point.

## Learning route

The educational anchor is Howard M. Wiseman and Gerard J. Milburn's *Quantum Measurement and Control* (Cambridge, 2010). The [source bridge](learning/anchor.md) connects its Lindblad and quantum-jump foundations to the clock model, translates notation, and identifies the steps supplied by this project.

The [tutorial](learning/tutorial.md) follows the clock from an observed event to its precision and entropy account. The [30-milestone map](learning/milestones.md) records the underlying understanding targets, dependencies and source pointers. Specialists can use the reading table above to go directly to the exact statements and proofs. The [LLM reading guide](llms.txt) maps common questions to their authoritative files.

## Reproduce the checks

From the repository root, with Python 3.10 or later:

```bash
python -m pip install -r verification/requirements.txt
python verification/run_checks.py --output verification/results.json
```

The suite compares tilted-generator cumulants with independent renewal-block moments, tests the absorption constraint for real and complex Hamiltonians and unital noise, and checks the exceptional-point recurrence in exact rational arithmetic. Finite checks support the implementations; the general statements are proved in the scientific pages.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
