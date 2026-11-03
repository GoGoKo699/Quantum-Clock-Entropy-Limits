# Model, observable and resource convention

[Repository overview](../README.md) · [Precision proof](precision_bound.md) · [Construction](achievability.md)

## 1. A complete reset interface

Let $\mathcal H$ be a finite-dimensional Hilbert space, $H=H^\dagger$ a time-independent Hamiltonian, and $|a\rangle,|b\rangle$ normalized states. In units with $\hbar=1$, the density operator evolves as

```math
\frac{d\rho}{dt}=\mathcal L(\rho)
=-i[H,\rho]+\mathcal D[J_+](\rho)+\mathcal D[J_-](\rho),
```

where

```math
\mathcal D[J](X)=JXJ^\dagger-\frac12\{J^\dagger J,X\},
\qquad
J_+=\sqrt\Gamma\,|a\rangle\langle b|,
\qquad
J_-=\sqrt{\Gamma r}\,|b\rangle\langle a|.
```

The forward rate coefficient is $\Gamma>0$ and $0 \lt r \lt 1$. The dimensionless rate affinity is $\Sigma=-\log r>0$. These are jump-operator coefficients; the actual mean event rates also depend on the clock state.

A positive jump prepares $P_a=|a\rangle\langle a|$ and a negative jump prepares $P_b=|b\rangle\langle b|$, independently of the pre-jump state. This full reset is the structural assumption that makes successive blocks between positive ticks independent. If the physical clock includes an ancilla, the counted operators must reset it too. An operator of the form $|a\rangle\langle b|\otimes I_A$ is generally higher rank and is outside the main model.

Orthogonality of $a,b$ is unnecessary for the mathematics. Orthogonal terminal ports are used in the construction and in the motivating thermal implementation. For coincident endpoints, the two jump labels must remain physically distinguishable if their signed record is to be an observable.

The baseline generator has no other dissipators. The [unital extension](extensions.md) states exactly which additional unobserved channels can be included without changing the proof.

## 2. Counting convention and operating sector

The output is the signed unit count

```math
N(t)=N_+(t)-N_-(t).
```

Every forward event contributes one and every reverse event contributes minus one. Grouping ticks into larger units changes this convention and must change the corresponding entropy-per-unit accounting as well.

For the Hamiltonian model, work on the cyclic space

```math
\mathcal H_{\mathrm{act}}
=\mathrm{span}\{H^k|a\rangle,H^k|b\rangle:k\ge0\}.
```

Its orthogonal complement is invariant under $H$ and cannot be reached after a reset. The [proof](precision_bound.md) shows that the no-count generator is exponentially stable on this active space. A running clock additionally requires positive stationary signed current. This excludes a disconnected interface whose forward and reverse counts merely alternate.

One may initialize the process immediately after a positive jump, in $P_a$. Any initialization whose first positive jump has a finite second moment has the same asymptotic current and variance rate: that initial segment contributes only a transient. An inaccessible dark component is handled separately in [the boundary discussion](extensions.md); it is not silently included in the positive-current regenerative premise.

For each fixed finite clock, define

```math
j=\lim_{t\to\infty}\frac{\mathbb E N(t)}{t}>0,
\qquad
D=\lim_{t\to\infty}\frac{\mathrm{Var}N(t)}{t},
\qquad
F=\frac{D}{j},
\qquad
\mathcal P=F^{-1}.
```

Here $D$ is the variance growth rate, with **no factor of two** absorbed into its definition. $\mathcal P$ is dimensionless precision per net tick, sometimes called an inverse Fano factor. The long-time limit is taken before increasing the clock dimension.

If $\widehat t=N(t)/j$ is calibrated as a time estimator, then its long-time variance is $Dt/j^2$. Thus the relevant error depends on both precision and ticking rate. A large $\mathcal P$ alone does not imply accurate estimation on a fixed laboratory timescale.

## 3. What the order law optimizes

Let $\Sigma_{\min}(P)$ denote the infimum of affinities among finite-dimensional clocks in the baseline class whose signed-current precision is at least a prescribed $P$. Dimension, static Hamiltonian and overall timescale may vary; there is no fixed-rate requirement in this optimization.

The [converse](precision_bound.md) and [construction](achievability.md) prove, for $P\ge2$,

```math
\frac12\log P\le\Sigma_{\min}(P)
\le3\log\lceil P\rceil+16\log2.
```

For the lower inequality, $\mathcal P\le e^{2\Sigma}\tanh(\Sigma/2) \lt e^{2\Sigma}$. For the upper inequality, choose the integer dimension $d=\lceil P\rceil$ in the explicit finite-bias family. These two statements optimize over the same clock class and use the same signed-current convention. They establish logarithmic order; the numerical coefficients and additive constant are not optimality claims.

Multiplying $H$ and both jump rates by a common positive timescale factor multiplies $j,D$ equally. It preserves $F,\mathcal P,r$ and $\Sigma$. With $\Gamma=1$, the construction satisfies $`\|H\|\le1/\sqrt3`$ but $j=\Theta(d^{-2})$. Restoring a general $\Gamma$ gives $`\|H\|\le\Gamma/\sqrt3`$ and $j=\Theta(\Gamma d^{-2})$. Maintaining a fixed rate by increasing $\Gamma$ would therefore increase the dynamical strength resource.

## 4. Affinity and entropy are separate premises

The Lindblad equation above specifies event statistics, not all reservoir temperatures or heat flows. The general theorem is an affinity statement. In the tightly coupled local-detailed-balance implementation described in [the thermodynamic account](thermodynamic_interface.md), the steady reservoir entropy rate is $k_{\mathrm B}\Sigma j$. Under that additional premise, $\Sigma$ is entropy produced per net tick in units of $k_{\mathrm B}$.

The optimization does not price apparatus fabrication, bath preparation, detector memory, record erasure or all implementation errors. It also does not declare an arbitrary phenomenological $H$ and reset pair to be an autonomous global thermal generator. The construction's finite reverse rate is included exactly in the effective model; a finite-rate microscopic elimination requires its own error analysis.

## 5. Reading the proof

The [precision proof](precision_bound.md) first constrains the probabilities of successive tick directions using quantum absorption. It then groups the output into independent positive-tick blocks and keeps their joint duration and signed reward. This avoids imposing direction–time independence on a quantum waiting-time kernel.

The [construction](achievability.md) begins with an inherited Erlang escape law and controls its finite-bias recycled version through resolvent moments. The [extensions](extensions.md) explain why unital noise preserves the converse and why retained memory or a different time estimator changes the problem. The [related-work account](../references/related_work.md) identifies the source of each inherited ingredient.
