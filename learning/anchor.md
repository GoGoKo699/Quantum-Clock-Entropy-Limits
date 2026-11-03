# Educational anchor: quantum measurements and trajectories

[Learning map](milestones.md) · [Tutorial](tutorial.md) · [Scientific model](../science/model.md)

The single educational anchor for this learning route is **Howard M. Wiseman and Gerard J. Milburn, _Quantum Measurement and Control_ (Cambridge University Press, 2010)**, hardback ISBN **978-0-521-80442-4**. Cambridge's [official frontmatter](https://assets.cambridge.org/97805218/04424/frontmatter/9780521804424_frontmatter.pdf) confirms the authors, title, ISBN, and first-publication year.

The book provides the measurement and open-system language in which the clock is formulated. The precision ceiling, its proof, and the finite-affinity construction are developed in this repository. The section pointers below are verified against Cambridge's [official table of contents](https://assets.cambridge.org/97805218/04424/toc/9780521804424_toc.pdf). The equations on this page use local project notation; no unverified textbook equation numbers are assigned.

## 1. The relevant route through the anchor

| Verified section | Starting page | Role in this project |
| --- | ---: | --- |
| §3.6, “The Lindblad form and positivity” | 119 | The unconditional density-operator generator and its positivity requirements. |
| §3.11, “Heisenberg-picture dynamics” | 141 | The adjoint action on observables and the relation between trace loss and absorption. |
| §4.2, “Quantum jumps” | 149 | Resolved count events, conditioned evolution between events, and the distinction between a trajectory and its ensemble average. |
| §4.7, “Monitoring in the Heisenberg picture” | 181 | The observable-side description used when integrated no-count maps and their adjoints appear in the proof. |

Finite-dimensional quantum mechanics, matrix adjoints, traces, eigenvalues, and elementary probability are the mathematical starting point. The book's earlier treatment of measurements supplies broader context. Feedback control is not an assumption of this clock: the Hamiltonian and jump operators are time independent, and passive monitoring records the output without changing the subsequent generator.

The conceptual sequence is therefore:

**Lindblad dynamics → resolved quantum jumps → complete reset → regenerative counting blocks → a precision constraint.**

The first two transitions establish the language. The last three require the additional model assumptions and arguments identified below.

## 2. From a jump record to a complete reset

For the baseline clock, the unconditional state obeys

```math
\dot\rho=-i[H,\rho]+\mathcal D[J_+](\rho)+\mathcal D[J_-](\rho),
```

with the local dissipator convention

```math
\mathcal D[J](X)=JXJ^\dagger-\frac12\{J^\dagger J,X\}.
```

If the current normalized conditional state is $\rho_c$, the probability of one resolved event of sign $\sigma$ in a short interval is

```math
\Pr(dN_\sigma=1\mid\rho_c)
=\mathrm{Tr}(J_\sigma^\dagger J_\sigma\rho_c)\,dt+o(dt).
```

Conditional on that event, the normalized state becomes

```math
\rho_c\longmapsto
\frac{J_\sigma\rho_cJ_\sigma^\dagger}
{\mathrm{Tr}(J_\sigma^\dagger J_\sigma\rho_c)}.
```

The [project's special choice](../science/model.md) is

```math
J_+=\sqrt\Gamma\,|a\rangle\langle b|,
\qquad
J_-=\sqrt{\Gamma r}\,|b\rangle\langle a|.
```

It gives

```math
J_+\rho_cJ_+^\dagger
=\Gamma\langle b|\rho_c|b\rangle P_a,
\qquad
J_-\rho_cJ_-^\dagger
=\Gamma r\langle a|\rho_c|a\rangle P_b.
```

Thus every positive event prepares $P_a$, and every negative event prepares $P_b$, whenever that outcome has nonzero probability. This is a statement about the entire clockwork. An event can be rank one on a small subsystem while preserving memory elsewhere; such an event does not meet this complete-reset premise.

The coefficient $\Gamma$ is not generally the observed positive-event rate. The conditional positive intensity is $\Gamma\langle b|\rho_c|b\rangle$. Likewise, the reverse coefficient is $\Gamma r$, while its intensity depends on occupation of $a$.

## 3. No-count evolution carries probability in its trace

In the Hamiltonian baseline, define

```math
Q=J_+^\dagger J_++J_-^\dagger J_-
=\Gamma(P_b+rP_a),
\qquad
G=-iH-\frac Q2,
\qquad
K_t=e^{tG}.
```

Starting from a normalized state $\rho_0$, the unnormalized state conditioned on no counted event is

```math
\widetilde\rho(t)=K_t\rho_0K_t^\dagger.
```

Its trace is the survival probability. Normalizing $\widetilde\rho(t)$ would give the conditional state, but would remove the survival weight needed to calculate waiting-time probabilities. The next-event densities are

```math
w_\sigma(t\mid\rho_0)
=\mathrm{Tr}\!\left[
J_\sigma^\dagger J_\sigma K_t\rho_0K_t^\dagger
\right].
```

These formulas explain why the proof integrates a trace-decreasing evolution. The [active-sector argument](../science/precision_bound.md#1-active-subspace-and-eventual-absorption) supplies the additional fact that survival decays to zero. Without that step, an integral could retain a dark component and the inverse used later might not exist.

There are two different stopping rules in the scientific pages:

- In the **converse**, no-count evolution ends at either a positive or a negative tick.
- In the **finite-affinity construction**, a regeneration block ends only at the next positive tick. Negative ticks remain inside that block and are included in its killed generator.

At zero reverse rate these stopping rules coincide. At finite reverse rate they must not be interchanged.

## 4. Local notation dictionary

This is a dictionary for the repository, not a claim that the book uses these exact symbols.

### Dynamics and absorption

| Symbol | Local meaning |
| --- | --- |
| $\rho$, $\rho_c$, $\widetilde\rho$ | Unconditional normalized state, conditional normalized state, and unnormalized surviving state. |
| $H$ | Time-independent Hermitian Hamiltonian; with $\hbar=1$, its units are inverse time. |
| $P_a,P_b$ | Rank-one projectors onto normalized reset states. Orthogonality is optional in the converse. |
| $J_+,J_-$ | Resolved jump operators, with units of inverse square-root time. |
| $\Gamma,r,\Sigma$ | Forward rate coefficient, reverse/forward coefficient ratio, and affinity $\Sigma=-\log r$. |
| $Q$ | Sum of the two counted loss operators $J_\sigma^\dagger J_\sigma$. |
| $G,K_t$ | No-count amplitude generator and propagator. The calligraphic $\mathcal G$ in the extension is instead a superoperator. |
| $\mathcal L_0$ | The killed superoperator explicitly defined on its page: both signs are killed in the converse; the construction first uses the ideal $r=0$ generator. |
| $\mathcal L_r$ in the construction | Evolution killed at positive ticks while retaining the negative jump dissipator. |
| $\mathcal R$ or $R$ | The time integral of a stable killed semigroup, equivalently its negative-generator inverse. It has units of time. |
| $C_{ij}$ | In the Hamiltonian baseline, the integrated transfer intensity $\int_0^\infty\lvert\langle i\vert K_t\vert j\rangle\rvert^2dt$, with units of time. The unital extension uses the integrated superoperator instead. |
| $A$ | Dimensionless probability $\Gamma C_{ba}=\Pr(+\mid+)$. |

### Record, blocks, and precision

| Symbol | Local meaning |
| --- | --- |
| $N_+,N_-,N$ | Positive count, negative count, and signed net count $N=N_+-N_-$. |
| $T,M,Y$ | Duration of a positive-tick block, number of its negative ticks, and net block reward $Y=1-M$. |
| $\mu,q$ | $\mu=\mathbb ET$ and $q=\mathbb EY$ in the converse. |
| $j$ | Long-time mean signed count per unit time; the theorem assumes $j>0$. |
| $D$ or $v_N$ | Long-time variance growth rate $\lim_{t\to\infty}\mathrm{Var}N(t)/t$. No factor of two is included. |
| $F,\mathcal P$ | Signed-count Fano factor $F=D/j$ and inverse-Fano precision $\mathcal P=j/D$. |
| $v$ in the construction | The raw block second moment $\mathbb ET^2$; it is not $\mathrm{Var}T$ or the count variance rate. |
| $d$ | Finite clock dimension; the long-time limit is taken at each fixed $d$ before discussing dimension scaling. |

The symbols $D$ and $G$ also occur as temporary operators inside individual proofs. Their definitions at those locations control their meaning; the variance rate and amplitude generator in this dictionary must not be substituted mechanically into such local algebra.

## 5. Additional assumptions supplied by the project

The trajectory formalism permits many models. The theorem uses a specific one:

1. Finite-dimensional, time-independent Markovian dynamics, with two resolved counted channels of the displayed rank-one form.
2. Complete reset of every persistent degree of freedom after a counted event.
3. The active Hamiltonian-cyclic sector generated by $a,b$, with positive stationary signed current.
4. Ideal passive detection of both output labels and the fixed signed unit-count convention.
5. Long-time mean and variance rates at fixed finite dimension.

The main proof establishes the necessary no-count stability and block moments for this sector. It does not impose independence between waiting time and tick direction. Its [unital extension](../science/extensions.md) allows additional uncounted unital dynamics under an explicit stability hypothesis. In that extension, the no-count map need not have the single-Kraus form $K_t(\cdot)K_t^\dagger$.

Affinity is a mathematical parameter of the jump pair. Identifying $k_{\mathrm B}\Sigma$ with physical entropy produced per net tick requires the additional tightly coupled local-detailed-balance realization in the [thermodynamic interface](../science/thermodynamic_interface.md). The construction has net rate $\Theta(\Gamma d^{-2})$; precision growth is not a fixed-rate claim.

## 6. What the anchor does not supply

The project supplies the chain of arguments from its model to the research result:

| Additional step | Authoritative local account |
| --- | --- |
| Stable active sector and the two integrated absorption identities | [Precision proof, §§1–2](../science/precision_bound.md#1-active-subspace-and-eventual-absorption) |
| Accretive-resolvent compression and $A\le(1+r)^{-1}$ | [Precision proof, §3](../science/precision_bound.md#3-positivity-limits-consecutive-ticks-of-the-same-sign) |
| Positive-tick regeneration with correlated duration and reward | [Precision proof, §4](../science/precision_bound.md#4-renewal-blocks-and-their-signed-rewards) |
| Nonnegative-duration relaxation giving the precision ceiling | [Precision proof, §5](../science/precision_bound.md#5-optimizing-over-all-nonnegative-block-durations) |
| Explicit chain, wavepacket norm bound, and finite-reverse-rate estimates | [Achievability](../science/achievability.md) |
| Entropy boundary identity and microscopic implementation limits | [Thermodynamic interface](../science/thermodynamic_interface.md) |

These are not attributed to the selected textbook. Standard matrix positivity and probability tools are combined here with the complete-reset architecture.

Research dependencies have a separate role from the educational anchor. [M25](../references/README.md#m25) supplies the motivating clock architecture and earlier exponential advantage; [HBK26](../references/README.md#hbk26) supplies the ideal exceptional-point escape mechanism; and [SB](../references/README.md#sb) supplies related absorption identities. [M26](../references/README.md#m26) records the broader reset-clock uncertainty question. The [comparison of claims](../references/related_work.md) states what is inherited and what is established locally. These citations do not introduce a second educational anchor or imply that the textbook contains the current theorem.
