# Relation to existing clock and quantum-current bounds

The central result is a dimension-independent ceiling on the precision of the signed net tick count for a single pair of complete rank-one resets. For normalized reset states $a,b$, arbitrary time-independent Hermitian $H$, and a stable active operating sector, the jumps

```math
J_+=\sqrt{\Gamma}|a\rangle\langle b|,
\qquad
J_-=\sqrt{\Gamma e^{-\Sigma}}|b\rangle\langle a|
```

obey

```math
\mathcal P\le e^{2\Sigma}\tanh(\Sigma/2).
```

Together with a controlled finite-affinity construction, this gives a logarithmic affinity cost for large target precision in the specified model. The coefficient in the optimal asymptotic cost remains open. The proof also has a [unital inter-tick extension](../science/extensions.md), subject to stability.

This page distinguishes the result from its closest scientific antecedents. It documents the premises and conclusions needed for the comparison; it does not claim an exhaustive priority search. Precise model assumptions appear in [model.md](../science/model.md), and the conditions for interpreting affinity as entropy appear in [thermodynamic_interface.md](../science/thermodynamic_interface.md).

## 1. Exponential clock advantage is an antecedent

Meier et al., [M25](README.md#m25), study the same thermally paired reset link and signed-count precision with a coherent transport chain. They establish exponential achievable precision as a function of entropy per tick. Their construction and physical interface already demonstrate why classical linear thermodynamic precision bounds need not govern this architecture.

Our result supplies the converse: at any fixed finite affinity, precision remains bounded uniformly over finite dimension and arbitrary Hermitian coherent dynamics. The construction here is useful because it provides explicit finite-affinity control and completes the order statement

```math
\Sigma_{\min}(P)=\Theta(\log P).
```

We do not attribute the exponential advantage, its coherent transport mechanism, or the biased-reset model to this work. We also do not infer that our coefficient $2$ in the precision ceiling is optimal.

## 2. The quantum-reset TUR question remains broader

Meier's thesis, [M26](README.md#m26), Section 2.2.2, discusses thermodynamically paired rank-one reset processes, including nonorthogonal states. It identifies direction–time dependence of quantum waiting kernels as an obstruction to importing a classical semi-Markov thermodynamic uncertainty relation and presents an extension to quantum reset clocks as a conjecture.

The present theorem addresses the single-pair subclass and obtains an exponential ceiling without assuming that the next direction and waiting time are independent. It does not settle a general many-pair version of that conjecture or establish its strongest proposed functional form.

The relevant semi-Markov antecedent, Ertel, van der Meer, and Seifert [EVS22](README.md#evs22), imposes thermodynamic consistency conditions on the waiting kernels. The current proof instead extracts an additional constraint from the quantum generator. The probability $A=\Pr(+\mid+)$ that the next tick is positive following a positive reset satisfies

```math
A\le\frac{1}{1+e^{-\Sigma}}.
```

Positive ticks then define regeneration blocks whose signed rewards and durations may remain correlated. The fluctuation estimate treats those correlations directly. It is not a substitution of the quantum clock into a direction–time independent semi-Markov formula.

This distinction matters operationally. A freely assigned semi-Markov waiting law can make some conditional durations arbitrarily regular without obeying the endpoint-transfer constraint of a physical two-reset quantum generator. The theorem uses both the quantum constraint and the signed block-reward structure.

## 3. Exceptional-point escape and finite-affinity recycling

Holst, Blasi, and Khandelwal [HBK26](README.md#hbk26), Section VIII.A and Appendix H, derive the maximal-exceptional-point escape law for a resonant chain with one initial excitation, an empty residual bath, and irreversible terminal loss. At an exceptional point of order $d$, it is Erlang with shape $2d-1$ and rate $\Gamma/d$. They also establish asymptotic escape optimality under a fixed sum of squared couplings. Their Discussion identifies autonomous recycling and continuously driven transport as extensions.

We inherit and credit that ideal escape mechanism. The [achievability proof](../science/achievability.md) provides an explicit positive-coupling realization and then includes a nonzero backward reset. Its added steps control the killed evolution, block moments, and signed-count fluctuations uniformly in dimension. In particular,

```math
0\lt r\le\frac{1}{65536d^3}
\quad\Longrightarrow\quad
\mathcal P_r\ge d.
```

The relevant HBK26 chain proof assumes a maximal exceptional point and does not supply an explicit positive-coupling formula valid for every $d$. That observation is a comparison with this paper, not a priority claim for the formula across the wider inverse-eigenvalue or non-Hermitian-chain literature.

The distinction between escape and a finite-affinity clock is substantive. Irreversible terminal loss describes one escape event. A running reset clock repeatedly recycles the excitation; a backward reset changes both its state and the signed reward. At $r=0$ the affinity is infinite. Thus the ideal Erlang law alone does not establish the finite-affinity logarithmic cost result.

## 4. Comparison with general quantum uncertainty bounds

The following results address closely related precision questions. Their additional data, model assumptions, or observables explain why a direct citation does not replace the present single-interface argument.

| Source | Relevant result or premise | Relation to the present theorem |
| --- | --- | --- |
| Brandner and Saito [BS25](README.md#bs25) | Thermodynamic uncertainty relations for coherent fermionic transport, formulated in the Landauer transport setting. | A stationary scattering process with occupied reservoirs is not the same stochastic process as one excitation regenerated by a full-state rank-one jump. The transport theorem requires its own assumptions; we do not import it as a reset-clock proof. |
| Tan Van Vu, Honma, and Saito [VHS26](README.md#vhs26) | General open-system precision bounds involving quantities such as forward–backward asymmetry or no-jump/activity information. | A bound with additional dynamical data is not automatically uniform in the reset affinity alone. Moreover, an exponential bound in total entropy at a finite observation time need not give a nonzero long-time Fano lower bound at fixed entropy per net tick. |
| Kwon and Lee [KL25](README.md#kl25) | A quantum TUR with a dynamics-dependent correction, including reset-process analysis. Their Eq. (51) retains the factor $(1+\delta_{\mathrm{TUR}})^2$. | The correction is not controlled solely by the paired rate ratio. Their driven two-level example can approach $\delta_{\mathrm{TUR}}=-1$ at weak coherent coupling. The correction therefore cannot simply be discarded to obtain the uniform ceiling proved here. |
| Nishiyama and Hasegawa [NH25](README.md#nh25) | Their stated framework assumes a jump eigenoperator relation $[L_m,H]=\omega_mL_m$. | This restricts the coherent dynamics. For distinct orthogonal rank-one reset ports, it makes those ports energy eigenstates and removes the coherent recycling route with only this jump pair. For overlapping ports, the distinction is the eigenoperator premise; no zero-current conclusion is asserted here. |
| Macieszczak [MAC24](README.md#mac24) | An ultimate kinetic relation and semi-Markov/reset formulations using conditional waiting-time moments, including observables that weight successive transitions. | Those results provide important timing and estimation context. The present theorem eliminates waiting-time data using the quantum endpoint constraint and fixes the observable to the signed net count. It does not bound every optimal estimator obtainable from the complete event record. |

Two qualifications keep this comparison precise. First, a general quantum bound can be valid and useful while requiring dynamical information that the affinity-only ceiling eliminates. Second, the present result has a narrower architecture than a theorem covering arbitrary open quantum systems. Generality in Hilbert-space dimension and in $H$ should not be confused with generality in reset structure.

## 5. Complete resets versus clocks with retained quantum memory

The correlated-tick clocks of [CORR26](README.md#corr26) use dynamics beyond a complete rank-one reset of the full clockwork. They are an essential scope comparison because an event can leave quantum information that affects subsequent ticks.

For our model, every positive jump prepares the same full state $|a\rangle$, and every negative jump prepares $|b\rangle$. Individual successive ticks can still have direction and time correlations. Nevertheless, intervals from one positive tick to the next regenerate the entire process, which is the property used in the proof.

If an event instead acts as

```math
J_+\otimes I_A
```

on a clock plus persistent memory $A$, it is generally higher rank on the full Hilbert space. The memory is not erased and the positive-tick block reduction need not apply. Our theorem does not rule out precision improvements from such an architecture or provide an entropy ceiling for it.

Multiple distinct reset pairs are another open direction. Each outcome can prepare a different state, and the two-port transfer matrix used here is replaced by a larger object. The one-pair proof does not establish a multipair bound merely by summing the affinities.

## 6. Source-balance and transport antecedents

The related source-balance analysis [SB](README.md#sb) supplies the bright/dark decomposition and the two contraction identities. For the no-count propagator $K(t)=\exp[(-iH-Q/2)t]$, where $Q=\Gamma(P_b+rP_a)$ and $P_i=|i\rangle\langle i|$, these are

```math
\int_0^\infty K(t)^\dagger QK(t)\,dt=I,
\qquad
\int_0^\infty K(t)QK(t)^\dagger\,dt=I
```

on a stable active sector. These are inherited ingredients, not new discoveries claimed here.

The [precision proof](../science/precision_bound.md) combines them with an accretive-resolvent compression, an endpoint-transfer bound, the reset-sign process, and a renewal-reward variance estimate. Accretivity and the underlying renewal machinery are standard mathematical tools. The proposed scientific contribution is their implication for the specified finite-affinity clock architecture.

The related transport analysis [QTP](README.md#qtp) concerns noninteracting fermionic serial-chain conduction between occupied and empty reservoirs. Its transport fluctuations and contact-throughput accounting are relevant context. Its many-particle injection and extraction process does not identify directly with the full-reset one-excitation process studied here. Similar dimension scalings in these settings are not, by themselves, a theorem transfer.

## 7. What is established and what remains open

The proved combination is a uniform finite-affinity ceiling and a constructive exponential-order lower bound within the stated reset class. In the normalization of the construction, the larger precision comes with net rate $\Theta(\Gamma d^{-2})$. The result establishes neither the best exponential coefficient nor a fixed-rate optimum.

The following questions require additional results:

- The sharp affinity-only bound for one paired reset, including its behavior away from equilibrium.
- Generalization to multiple thermodynamic reset pairs or higher-rank outcomes.
- Bounds for retained quantum memory and more general choices of time estimator.
- Uniform microscopic control of finite-rate thermal interfaces as dimension grows.
- The optimal tradeoff among entropy per tick, precision, speed, and allowed coupling scales.

These questions preserve the distinction between the exact effective-generator result and the broader thermodynamics of autonomous timekeeping.
