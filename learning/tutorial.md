# From quantum jumps to a clock precision limit

[Overview](../README.md) · [Settled milestone map](milestones.md) · [Educational anchor and notation](anchor.md)

A ticking clock produces a random sequence of detector reports. A calibrated clock can estimate elapsed time by counting those reports. Coherent dynamics can make their timing more regular, while a reverse reset subtracts from the accumulated count and can change the time until the next forward event.

This project asks how much bias the reset interface needs to support a given precision. The result concerns one complete pair of rank-one resets and the signed count of its two output labels. It allows arbitrary finite coherent clockwork behind that interface.

The tutorial follows the settled map's two phases. Wiseman and Milburn's *Quantum Measurement and Control* (2010) is the sole educational anchor. Its verified section pointers and the local symbol dictionary are on the [anchor page](anchor.md). The scientific pages supply the project-specific arguments.

| Milestones | Part of the story |
| --- | --- |
| [M01–M06](milestones.md#m01) | States, resolved events, complete reset, and no-count evolution |
| [M07–M12](milestones.md#m07) | Active operation, random blocks, precision, and the resource question |
| [M13–M18](milestones.md#m13) | A physical constraint on tick signs becomes an affinity-only converse |
| [M19–M24](milestones.md#m19) | An ideal timing law becomes a controlled finite-affinity clock |
| [M25–M28](milestones.md#m25) | Noise, retained memory, entropy accounting, and device-level scope |
| [M29–M30](milestones.md#m29) | Attribution and evidence support the logarithmic cost law |

## 1. A detector report prepares the next starting state

**M01–M06.** The density operator $\rho$ describes the clock's probabilities and quantum coherences. It is positive and has trace one. A Hermitian Hamiltonian $H$ generates the coherent part of its evolution. The two resolved event channels are

```math
J_+=\sqrt{\Gamma}\,|a\rangle\langle b|,
\qquad
J_-=\sqrt{\Gamma r}\,|b\rangle\langle a|,
\qquad 0\lt r\lt 1.
```

Here $a$ and $b$ are normalized states, $\Gamma$ is a rate coefficient, and $r$ is the ratio of the reverse and forward coefficients. The affinity is $\Sigma=-\log r$. A smaller $r$ means a stronger preference for the forward channel.

The observed event rate also depends on the state. For example, the instantaneous positive-event intensity is $\Gamma\langle b|\rho|b\rangle$. Conditional on a positive event,

```math
\rho\longmapsto
\frac{J_+\rho J_+^\dagger}
{\mathrm{Tr}(J_+\rho J_+^\dagger)}
=P_a,
\qquad P_a=|a\rangle\langle a|.
```

The incoming state affects whether the event occurs, but its normalized output is always $P_a$. A negative event similarly prepares $P_b$. This complete reset is the link between quantum dynamics and the independent blocks used later. Every persistent degree of freedom must be included when checking it.

Between counted events, define

```math
Q=\Gamma(P_b+rP_a),
\qquad
G=-iH-\frac Q2,
\qquad
K_t=e^{tG}.
```

If neither label has occurred by time $t$, the unnormalized surviving state is

```math
\widetilde\rho(t)=K_t\rho_0K_t^\dagger.
```

Its trace is the probability of having seen no tick. The negative term $-Q/2$ removes the weight assigned to trajectories in which a tick has already occurred. Averaging the no-count part together with both possible jump updates gives the trace-preserving Lindblad equation in the [model](../science/model.md).

The adjoint description evolves observables instead of states. The trace pairing,

```math
\mathrm{Tr}[O\,\Phi(\rho)]
=\mathrm{Tr}[\Phi^\dagger(O)\rho],
```

makes the two descriptions equivalent. In particular, an adjoint identity involving $I$ can express a statement about survival for every initial state.

## 2. Active operation and the quantity called precision

**M07–M12.** A state that never reaches either counted channel belongs to a dark sector. The Hamiltonian model is therefore analyzed on the smallest $H$-invariant space containing $a$ and $b$. The [stability argument](../science/precision_bound.md#1-active-subspace-and-eventual-absorption) shows that no-count survival decays exponentially on this active space. Waiting-time moments and the integrated evolution are then well defined.

Absorption alone does not guarantee a running signed clock. For example, two orthogonal ports with no coherent coupling merely alternate positive and negative ticks. The net count stays bounded. The theorem additionally assumes a positive long-time signed current.

Define the recorded output and its two long-time rates by

```math
N(t)=N_+(t)-N_-(t),
\qquad
j=\lim_{t\to\infty}\frac{\mathbb E N(t)}t>0,
\qquad
D=\lim_{t\to\infty}\frac{\mathrm{Var}N(t)}t.
```

The convention is $\mathrm{Var}N(t)\sim Dt$. There is **no factor of two** in $D$. The signed-count Fano factor and precision are

```math
F=\frac Dj,
\qquad
\mathcal P=\frac1F=\frac jD.
```

Thus larger $\mathcal P$ means smaller count variance per mean net tick. Rate remains a separate quantity. The calibrated estimator $\widehat t=N(t)/j$ has asymptotic variance

```math
\mathrm{Var}\widehat t
\sim\frac{Dt}{j^2}
=\frac{t}{j\mathcal P}.
```

A precision improvement can therefore be offset by slower operation on a fixed laboratory timescale.

Complete positive resets suggest a useful way to group the record. Start a block immediately after one positive tick and end it at the next positive tick. Let $T$ be its duration and $M$ the number of negative ticks inside it. Its net reward is

```math
Y=1-M.
```

Successive pairs $(T,Y)$ are independent and identically distributed because each block starts from the same full state under the same generator. Duration and reward within one block can remain correlated.

The optimization asks for the smallest affinity needed to achieve a target $\mathcal P$. Dimension, Hamiltonian, and overall timescale may vary within the stated architecture. No fixed-rate requirement is imposed. The additional assumptions needed to call $\Sigma$ an entropy per tick are addressed below.

## 3. Worked example: two labeled Poisson channels on the same state

**A complete example for M01–M12, revisited in M26.** Take a one-dimensional clockwork with $a=b=u$ and $H=0$. Keep the two detector labels distinct:

```math
J_+=\sqrt\Gamma\,|u\rangle\langle u|,
\qquad
J_-=\sqrt{\Gamma r}\,|u\rangle\langle u|.
```

Every event leaves the state unchanged. Nevertheless, the monitored environment produces a random labeled record. Both intensities are constant, so $N_+$ and $N_-$ are independent Poisson counts with respective rates $\Gamma$ and $\Gamma r$. A Poisson count with mean $\lambda t$ also has variance $\lambda t$.

The survival probability and next-label probabilities are

```math
S(t)=e^{-\Gamma(1+r)t},
\qquad
\Pr(+)=\frac1{1+r},
\qquad
\Pr(-)=\frac r{1+r}.
```

Adding independent variances, while subtracting the means for the signed count, gives

```math
\mathbb E N(t)=\Gamma(1-r)t,
\qquad
\mathrm{Var}N(t)=\Gamma(1+r)t.
```

Consequently,

```math
j=\Gamma(1-r),\qquad D=\Gamma(1+r),
\qquad
F=\frac{1+r}{1-r},
\qquad
\mathcal P=\frac{1-r}{1+r}
=\tanh(\Sigma/2).
```

For $\Gamma=1$ in the chosen time unit and $r=1/4$, these are $j=3/4$, $D=5/4$, $F=5/3$, and $\mathcal P=3/5$. The general precision ceiling will be $48/5$ at this affinity. The example lies well below that ceiling.

The block description retains a correlation even in this simple model. Since positive events form a Poisson process,

```math
T\sim\mathrm{Exp}(\Gamma),
\qquad
\mathbb E[M\mid T]=\Gamma rT.
```

A longer interval to the next positive tick admits more negative events. Using $\mathrm{Var}T=\Gamma^{-2}$,

```math
\mathrm{Cov}(T,Y)
=-\mathrm{Cov}(T,M)
=-\Gamma r\,\mathrm{Var}T
=-\frac r\Gamma.
```

Thus independent positive-tick blocks do not imply independent block duration and reward.

This example illustrates the count convention and reset structure. It does not demonstrate a coherent precision advantage, and assigning the kinetic affinity $\Sigma=\log4$ does not by itself specify a thermal entropy flow. Its physical interpretation also requires the two output labels to be separately observable.

## 4. A quantum constraint on a classical sign process

**M13–M14.** After integrating over waiting time, the next tick has a positive or negative sign. Those probabilities are constrained by the quantum generator that produces them.

For $i,j\in\lbrace a,b\rbrace$, define

```math
C_{ij}=\int_0^\infty
|\langle i|K_t|j\rangle|^2\,dt.
```

The [two absorption identities](../science/precision_bound.md#2-integrated-transfer-is-reciprocal) give $C_{ab}=C_{ba}$. This equality concerns integrated transfer. It does not require equality of instantaneous amplitudes, a real Hamiltonian, or time-reversal symmetry.

Set $A=\Gamma C_{ba}$, the probability of a positive tick after a positive reset. Normalization fixes the endpoint matrix:

```math
C=\frac1\Gamma
\begin{pmatrix}
(1-A)/r&A\\
A&1-rA
\end{pmatrix}.
```

The crucial additional fact is that $C$ is positive semidefinite. Nonnegative entries alone would not establish this. The [proof](../science/precision_bound.md#3-positivity-limits-consecutive-ticks-of-the-same-sign) obtains the quadratic-form condition by compressing an accretive inverse generator onto $P_a$ and $P_b$.

Its determinant then gives

```math
(1-A)(1-rA)\ge rA^2,
\qquad
\boxed{A\le\frac1{1+r}.}
```

No larger internal Hilbert space can remove this restriction within the model. In the same-state example, $A=1/(1+r)$ exactly, even though its final precision does not saturate the general ceiling. Saturating this one intermediate step is therefore insufficient for optimal precision.

## 5. Keeping the timing correlations closes the converse

**M15–M18.** The complete sign kernel is

| Previous tick | Next positive tick | Next negative tick |
| --- | ---: | ---: |
| Positive | $A$ | $1-A$ |
| Negative | $1-rA$ | $rA$ |

A positive-tick block has reward $Y=1$ if it contains no negative tick. One negative tick gives $Y=0$, two give $Y=-1$, and so on. Hence

```math
\Pr(Y=1)=A,
\qquad
\Pr(Y=-k)=(1-A)(1-rA)(rA)^k,
\quad k=0,1,\ldots.
```

The mean reward is $q=A(1-r)/(1-rA)$. With $\mu=\mathbb ET$, the renewal-reward relations are

```math
j=\frac q\mu,
\qquad
\boxed{
F=\frac{\mathbb E[(Y-jT)^2]}q.
}
```

The difference $Y-jT$ measures how much a block's actual signed output differs from the average output expected over its duration. Keeping the square of this difference retains the reward–duration covariance. Replacing it with $\mathrm{Var}Y$ would omit part of the counting noise. The [canonical proof](../science/precision_bound.md#4-renewal-blocks-and-their-signed-rewards) establishes the needed moments and controls the unfinished block.

The remaining bound needs only nonnegative elapsed time. Write $Z=jT\ge0$ and $\mathbb EZ=q$. When $Y\le0$, a nonnegative $Z$ cannot cancel that negative reward. The proof allows even an idealized assignment in which unfavorable blocks take zero time and then minimizes over all remaining duration choices. This enlarged set of choices can only lower the residual variance, so its minimum is a valid lower bound for the physical clock.

The resulting inequality is

```math
F\ge
\frac{r(1+r)(1-A)}{(1-r)(1-rA)}
\ge\frac{r^2(1+r)}{1-r},
```

where the second step uses the largest physically permitted $A$. Taking the reciprocal gives

```math
\boxed{
\mathcal P\le
\frac{1-r}{r^2(1+r)}
=e^{2\Sigma}\tanh(\Sigma/2).
}
```

The internal Hamiltonian has disappeared from the bound. Near equilibrium the upper envelope begins as $\Sigma/2+O(\Sigma^2)$; at large affinity it grows exponentially. The argument establishes a finite ceiling at every finite affinity, but it does not determine the sharp envelope.

## 6. From ideal escape to a finite-affinity clock

**M19–M24.** The constructive branch starts with a real nearest-neighbor chain of $d$ states and orthogonal endpoints. In units with $\Gamma=1$, its explicit positive couplings keep $\lVert H\rVert\le1/\sqrt3$. The [coupling formula and determinant recurrence](../science/achievability.md#1-a-bounded-real-chain-with-one-exceptional-point) produce

```math
\det(sI-G_0)=\left(s+\frac1{2d}\right)^d.
```

All decay eigenvalues coalesce into one Jordan block. This is the maximal exceptional point used in the construction. The endpoint transfer amplitude is proportional to

```math
t^{d-1}e^{-t/(2d)}.
```

Squaring its magnitude and normalizing gives the inherited Erlang first-tick law with shape $2d-1$ and rate $1/d$. An Erlang law with shape $k$ and rate $\kappa$ has mean $k/\kappa$ and variance $k/\kappa^2$. Thus the ideal clock has

```math
\mathbb ET_0=d(2d-1),
\qquad
\mathrm{Var}T_0=d^2(2d-1),
\qquad
F_0=\frac1{2d-1}.
```

Each ideal block has reward one, so this waiting-time relative variance is also the counting Fano factor. The precision grows with $d$, but the ideal process has $r=0$ and therefore infinite affinity.

Finite-affinity operation requires control of the actual backward resets. The relevant estimate bounds the integrated killed evolution for every initial state:

```math
\lVert\mathcal R_0\rVert_{1\to1}\le4d^2.
```

The [wavepacket argument](../science/achievability.md#3-a-resolvent-bound-that-survives-the-exceptional-point) obtains this by mapping an initial state to the amplitude it emits into the terminal channel. Absorption makes that map an isometry. A bound on multiplication by emission time then becomes a bound on the mean waiting-time operator. This controls physical moments without relying on sensitive eigenvalue perturbation at the exceptional point.

For a finite reverse rate, the stopping rule is now the next **positive** tick. Negative jumps remain inside the block:

```math
\mathcal L_r=\mathcal L_0
+r\,\mathcal D[|b\rangle\langle a|].
```

Here $\mathcal L_0$ is the ideal $r=0$ killed generator. The negative recycling term must be retained. A Lyapunov inequality first proves stability; resolvent bounds then control the joint moments of $T$ and $M$, including $\mathbb E(TM)$.

For $d\ge2$ and $rd^2\le1/128$, the resulting [finite-affinity estimate](../science/achievability.md#6-an-explicit-finite-affinity-estimate) is

```math
F_r\le\frac1{2d-1}+8000rd^2.
```

The ideal term is of order $d^{-1}$. Choosing a reverse rate of order $d^{-3}$ keeps the perturbation at that same order. One explicit sufficient choice is

```math
r=\frac1{65536d^3},
\qquad
\mathcal P_r\ge d,
\qquad
\Sigma=3\log d+16\log2.
```

The accompanying rate is $j=\Theta(d^{-2})$ at fixed $\Gamma=1$. Restoring units gives $j=\Theta(\Gamma d^{-2})$. The construction is increasingly precise per net tick and increasingly slow.

## 7. Architecture and thermodynamics determine the scope

**M25–M28.** The converse extends to time-independent, trace-preserving unital Lindblad dynamics between the two counted resets, provided the no-count evolution is stable on the operating sector. Unitality preserves the identity operator, while trace preservation preserves normalization. Together they supply the two balance identities and contraction property used by the proof. The [extension](../science/extensions.md) states these assumptions explicitly.

Several other changes remove a premise:

- A retained ancilla can preserve information after a tick and prevent positive-tick blocks from regenerating.
- Multiple distinct reset pairs need not reduce to the same two-port transfer matrix.
- Disconnected orthogonal ports have zero growing signed current.
- A different statistic of the output record need not satisfy a bound proved for $N_+-N_-$.

These observations identify the boundaries of the proof. They do not assert that every model outside those boundaries violates its numerical ceiling.

The same-state example makes the observable boundary concrete. At $r=1$, the signed current has zero mean, but the total count $N_++N_-$ still has rate $2\Gamma$. It can estimate elapsed time even though the positive-current signed normalization no longer applies.

The thermodynamic interpretation needs an additional physical model. In the serial two-temperature interface, one forward completed reset absorbs heat $Q_{\mathrm h}$ from the hot bath and releases the same total heat into the cold bath. Local detailed balance gives

```math
\Sigma=(\beta_C-\beta_H)Q_{\mathrm h}.
```

Here $Q_{\mathrm h}$ is a heat quantum, denoted $Q$ in the standalone thermodynamic account. It is distinct from the counted loss operator used earlier in this tutorial. Let $N_1$ be the signed count on the first thermal edge of the serial reset path. Conservation of the signed currents through the intermediate levels gives

```math
S_{\mathrm{env}}(t)=\Sigma N_1(t)
+\text{bounded interface-occupancy terms}.
```

Consequently the steady entropy rate is $\Sigma j$ in units of $k_{\mathrm B}$. The [full accounting](../science/thermodynamic_interface.md#3-exact-entropy-accounting-before-elimination) gives the boundary terms explicitly.

This is entropy per signed net reset. It is not automatically the entropy per forward detection or the total cost of an arbitrary device. Additional noise can have physical costs even when its generator is unital. Likewise, exact entropy bookkeeping does not establish that a finite-rate microscopic interface has the same timing cumulants as its effective eliminated model.

Finally, raising $\Gamma$ can compensate for the constructive rate slowdown, but it also raises the permitted dynamical strengths. The cost optimization allows timescale changes and does not claim a fixed-rate advantage at fixed coupling strength.

## 8. The global result and its evidence

**M29–M30.** Two different arguments now address the same model and observable. The converse applies to every finite clock in the class. The construction provides one explicit family with controlled finite reverse rate.

Let $\Sigma_{\min}(P)$ be the infimum affinity among these clocks with precision at least $P$. For $P\ge2$, the converse and the construction with $d=\lceil P\rceil$ give

```math
\boxed{
\frac12\log P
\le\Sigma_{\min}(P)
\le3\log\lceil P\rceil+16\log2.
}
```

The optimal affinity cost therefore has logarithmic order. The two coefficients do not match, so the sharp coefficient remains open. The long-time limit is taken at each finite dimension, and the optimization has no fixed-rate constraint.

The attribution is part of this conclusion. [Meier et al.](../references/README.md#m25) established the earlier exponential clock advantage. [Holst, Blasi, and Khandelwal](../references/README.md#hbk26) supplied the ideal exceptional-point Erlang escape mechanism. Related [source-balance work](../references/README.md#sb) supplied absorption identities. The local research argument combines an affinity-only converse with controlled finite-affinity recycling. The [related-work account](../references/related_work.md) states the precise comparisons.

The [verification account](../verification/README.md) compares finite calculations of the same counting statistics and checks finite instances of the construction. Those checks support the implementations. The all-dimension claims rely on the analytical arguments in the [precision proof](../science/precision_bound.md) and [achievability proof](../science/achievability.md).

The resulting physical statement is specific: coherent dimension can support exponential-order growth of signed-count precision with affinity, while a complete paired reset still imposes a finite ceiling at every finite affinity. Its interpretation as a logarithmic entropy cost holds under the stated tightly coupled thermal realization.
