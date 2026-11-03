# Unital dynamics between ticks and boundaries of the result

The [main precision theorem](precision_bound.md) applies to a finite clockwork with a time-independent Hamiltonian and one counted pair of rank-one reset jumps. Its proof also permits a general unital quantum dynamical semigroup between the counted jumps. This page states and proves that extension, then distinguishes the signed-current observable from other ways of estimating time.

The definitions of the thermodynamic interface and of precision are in [model.md](model.md). The explicit finite-affinity construction in [achievability.md](achievability.md) uses Hamiltonian evolution and remains a special case of the extension.

## 1. Extension to a unital background generator

Let $\mathcal K$ be a finite-dimensional operating Hilbert space. Let $\mathcal G$ be a time-independent Lindblad generator on $\mathcal B(\mathcal K)$ whose semigroup is completely positive, trace preserving, and unital. Equivalently, in addition to the Lindblad condition,

$$
\mathcal G(I_{\mathcal K})=0,
\qquad
\mathcal G^\dagger(I_{\mathcal K})=0.
$$

The adjoint is taken in the Hilbert–Schmidt inner product. For normalized states $|a\rangle,|b\rangle\in\mathcal K$, not necessarily orthogonal, introduce the two counted channels

$$
J_+=\sqrt\Gamma\,|a\rangle\langle b|,
\qquad
J_-=\sqrt{\Gamma r}\,|b\rangle\langle a|,
\qquad
\Gamma>0,\quad 0<r<1.
$$

The full generator and the generator conditioned on observing neither counted channel are

$$
\mathcal L=\mathcal G+\mathcal D[J_+]+\mathcal D[J_-],
\qquad
\mathcal L_0=\mathcal G-\frac12\{Q,\,\cdot\,\},
$$

where

$$
P_a=|a\rangle\langle a|,
\quad P_b=|b\rangle\langle b|,
\quad Q=\Gamma(P_b+rP_a),
\quad
\mathcal D[J](X)=JXJ^\dagger-\frac12\{J^\dagger J,X\}.
$$

Uncounted channels belonging to $\mathcal G$ remain active during a no-count interval. Thus $e^{t\mathcal L_0}$ is generally a completely positive map with several Kraus operators, rather than evolution by one non-Hermitian Hamiltonian.

### Operating assumptions

Assume that $\mathcal L_0$ is strictly stable on $\mathcal B(\mathcal K)$: every eigenvalue has negative real part. In finite dimension this implies an exponential bound

$$
\|e^{t\mathcal L_0}\|_{1\to1}\leq C e^{-\eta t}
$$

for some $C,\eta>0$. In particular, a counted tick occurs almost surely from every state in the operating sector, and its waiting time has finite moments. Define the completely positive integrated map

$$
R=\int_0^\infty e^{t\mathcal L_0}\,dt=(-\mathcal L_0)^{-1}
$$

and the probability

$$
A=\Gamma\operatorname{tr}[P_bR(P_a)]
=\Pr(+\mid+).
$$

Assume also $A>0$. This is the positive-current condition for the paired-reset process. Stability alone does not imply it, as the disconnected-port example below demonstrates.

**Extended bound.** For the signed count $N(t)=N_+(t)-N_-(t)$, the stationary long-time precision satisfies

$$
\mathcal P
=\lim_{t\to\infty}\frac{\mathbb E N(t)}{\operatorname{Var}N(t)}
\leq
\frac{(1-r)(1-rA)}{r(1-A)(1+r)}
\leq
\frac{1-r}{r^2(1+r)}.
$$

Writing $\Sigma=-\log r$, the last expression is $e^{2\Sigma}\tanh(\Sigma/2)$. The bound is uniform in the dimension, the Hamiltonian part of $\mathcal G$, and the strength and form of its unital dissipative part. It does not assert that adding unital noise improves precision or that the bound is sharp.

## 2. Proof

### 2.1 Two normalization identities imply integrated reciprocity

Unitality and trace preservation give

$$
\mathcal L_0(I_{\mathcal K})
=\mathcal L_0^\dagger(I_{\mathcal K})=-Q.
$$

Taking inverses on the stable operating sector yields

$$
R(Q)=I_{\mathcal K},
\qquad
R^\dagger(Q)=I_{\mathcal K}.
$$

Define the nonnegative endpoint matrix elements

$$
C_{ij}=\operatorname{tr}[P_iR(P_j)],\qquad i,j\in\{a,b\}.
$$

The $P_a$ matrix element of the first inverse identity and the $P_a$ matrix element of the second identity are respectively

$$
\Gamma(C_{ab}+rC_{aa})=1,
\qquad
\Gamma(C_{ba}+rC_{aa})=1.
$$

Hence $C_{ab}=C_{ba}$. The remaining normalization equation gives

$$
C=
\frac1\Gamma
\begin{pmatrix}
(1-A)/r&A\\
A&1-rA
\end{pmatrix}.
$$

This is an integrated reciprocity identity. It does not require time-reversal symmetry or equality of the two directional waiting-time densities at each time. Normalization of $a$ and $b$ suffices; orthogonality has not been used.

### 2.2 Hilbert–Schmidt contraction bounds the transfer probability

For a unital completely positive map $\Phi_t=e^{t\mathcal G}$, the Kadison–Schwarz inequality gives

$$
\Phi_t(X)^\dagger\Phi_t(X)\leq\Phi_t(X^\dagger X).
$$

Trace preservation therefore implies $\|\Phi_t(X)\|_2\leq\|X\|_2$. Differentiating at $t=0$ shows

$$
\operatorname{Re}\langle X,-\mathcal G(X)\rangle_{\rm HS}\geq0.
$$

Consequently $\mathcal A=-\mathcal L_0$ is accretive:

$$
\operatorname{Re}\langle X,\mathcal A(X)\rangle_{\rm HS}
\geq
\frac12\operatorname{tr}(X^\dagger QX+X^\dagger XQ)
\geq0.
$$

Its inverse $R$ is accretive as well. Indeed, with $Y=R(X)$,

$$
\operatorname{Re}\langle X,R(X)\rangle_{\rm HS}
=\operatorname{Re}\langle\mathcal A(Y),Y\rangle_{\rm HS}
\geq0.
$$

For real $x,y$, substitute the Hermitian operator $D=xP_a+yP_b$. Since the endpoint matrix is real and symmetric,

$$
0\leq\operatorname{tr}[D R(D)]
=\begin{pmatrix}x&y\end{pmatrix}
C
\begin{pmatrix}x\\y\end{pmatrix}.
$$

Thus $C$ is positive semidefinite, even if $P_a,P_b$ are not independent. Its determinant gives

$$
(1-A)(1-rA)\geq rA^2,
\qquad
A\leq\frac1{1+r}.
$$

### 2.3 Regeneration and the signed reward bound

A positive counted jump resets the entire clockwork to $P_a$, while a negative counted jump resets it to $P_b$. The Markov property of the time-independent semigroup makes successive blocks between positive ticks independent and identically distributed, including all uncounted background evolution within each block.

The sign transition probabilities are $\Pr(+\mid+)=A$ and $\Pr(-\mid-)=rA$. Therefore a block's duration $T$ and signed reward $Y$ satisfy

$$
\Pr(Y=1)=A,
\qquad
\Pr(Y=-m)=(1-A)(1-rA)(rA)^m,
\quad m=0,1,\ldots.
$$

Here $Y=-m$ corresponds to $m+1$ negative ticks followed by the terminating positive tick. In particular,

$$
\mu_Y=\mathbb EY=\frac{A(1-r)}{1-rA}>0,
\qquad j=\frac{\mu_Y}{\mathbb ET}>0.
$$

The geometric sign tail and stable no-count evolution give finite block moments. The renewal-reward variance formula then reads

$$
F=\mathcal P^{-1}
=\frac{\mathbb E[(Y-jT)^2]}{\mu_Y}.
$$

The physical duration obeys $jT\geq0$ and $\mathbb E(jT)=\mu_Y$. Relaxing to all nonnegative random variables $Z$ with this mean can only lower the residual second moment. Its minimum occurs at $Z=\mu_Y/A$ on $Y=1$ and $Z=0$ on $Y\leq0$. Hence

$$
\mathbb E[(Y-jT)^2]
\geq
\frac{rA(1-A)(1+r)}{(1-rA)^2}.
$$

It follows that

$$
F\geq
\frac{r(1+r)(1-A)}{(1-r)(1-rA)}
\geq
\frac{r^2(1+r)}{1-r},
$$

where the last step uses $A\leq1/(1+r)$. No independence between waiting time and jump direction is assumed.

## 3. Choosing a valid operating sector

For the Hamiltonian-only model, the [main proof](precision_bound.md) restricts to the Hamiltonian-cyclic subspace generated by the two endpoint states. An additional unital noise channel can couple that space to other states. One must then enlarge the operating space or establish a different closed reduction.

A permitted reduction to $\mathcal K$ must retain both endpoint states and make the restricted background semigroup a completely positive, trace-preserving, unital semigroup on $\mathcal B(\mathcal K)$. Compression of a generator onto an arbitrary selected subspace need not have these properties. The stability assumption concerns that full restricted no-count generator, including its background noise.

A useful sufficient stability certificate is a positive-definite operator $S$ and a number $\epsilon>0$ such that

$$
\mathcal L_0^\dagger(S)\leq-\epsilon I_{\mathcal K}.
$$

If $s_{\min}I\leq S\leq s_{\max}I$, then for any positive unnormalized no-count state $\rho_t$,

$$
\frac{d}{dt}\operatorname{tr}(S\rho_t)
\leq-\epsilon\operatorname{tr}\rho_t
\leq-\frac{\epsilon}{s_{\max}}\operatorname{tr}(S\rho_t).
$$

Thus

$$
\operatorname{tr}\rho_t
\leq\frac{s_{\max}}{s_{\min}}
e^{-\epsilon t/s_{\max}}\operatorname{tr}\rho_0,
$$

which proves exponential absorption. Taking $S=I$ immediately works when $Q$ is positive definite. More general certificates allow rank-deficient $Q$ and transport from internal states to the counted ports.

An invariant sector with no probability of reaching either counted channel is a dark sector and fails this absorption condition. It cannot simply be retained while using the inverse $R=(-\mathcal L_0)^{-1}$. The treatment of inactive initial components in the main theorem remains relevant.

### Examples of allowed background noise

Hermitian dephasing operators give a unital generator of the form

$$
\mathcal G(X)=-i[H,X]
+\sum_k\gamma_k\left(B_kXB_k-\frac12\{B_k^2,X\}\right),
\qquad B_k=B_k^\dagger,\quad\gamma_k\geq0.
$$

Random unitary jumps, $\sum_k\gamma_k(U_kXU_k^\dagger-X)$, also provide unital backgrounds. Both examples are covered whenever the operating-sector and absorption conditions hold.

Unitality is a statement about the action of a channel on the identity operator. It does not assign zero heat, work, or entropy cost to a physical implementation. The bound above uses the counted pair's rate affinity $\Sigma=-\log r$. Identifying that quantity with a physical entropy per net tick requires the interface model in [model.md](model.md), and identifying it with a total device cost additionally requires accounting for the background dynamics and the measurement apparatus.

## 4. Boundary examples

### 4.1 Identical endpoint states and distinguishable Poisson labels

Take $a=b=u$, operate on the one-dimensional space spanned by $u$, and set $\mathcal G=0$. Both counted jumps leave the state unchanged. If their output labels are separately recorded, they generate independent Poisson counts with rates $\Gamma$ and $\Gamma r$:

$$
\mathbb E N(t)=\Gamma(1-r)t,
\qquad
\operatorname{Var}N(t)=\Gamma(1+r)t.
$$

Therefore

$$
\mathcal P=\frac{1-r}{1+r}=\tanh(\Sigma/2),
\qquad
A=\frac1{1+r}.
$$

The transfer-probability ceiling is saturated, while the final precision ceiling is loose. This also shows why nonorthogonal endpoints are mathematically legitimate and why positivity of the signed current cannot be inferred solely from a geometrical transport picture. The labels are part of the measurement specification; combining the two outputs into one count changes the observable. A nonzero assigned rate affinity in this one-dimensional example is not, by itself, a derivation of a thermal entropy flow.

### 4.2 Orthogonal disconnected ports have zero net current

Take orthogonal $a,b$, $\mathcal K=\operatorname{span}\{a,b\}$, and

$$
H=E_aP_a+E_bP_b,
\qquad \mathcal G=-i[H,\,\cdot\,].
$$

The no-count generator is stable, but $A=0$. After a positive tick the next tick must be negative, and after a negative tick the next must be positive. In the stationary state,

$$
p_a=\frac1{1+r},\qquad p_b=\frac r{1+r},
$$

and the forward and backward fluxes are equal. Along a stationary trajectory,

$$
N(t)=\mathbf1_{\{X_t=a\}}-\mathbf1_{\{X_0=a\}},
$$

so the signed count remains bounded and has zero mean. There is no positive asymptotic net tick rate, and the positive-current Fano normalization used in the theorem does not apply.

This distinction is relevant to [Nishiyama and Hasegawa](../references/README.md#nh25), whose correspondence assumes $[J_m,H]=\omega_mJ_m$ for each channel. For distinct orthogonal rank-one endpoints, that condition makes both endpoints Hamiltonian eigenvectors; with only this pair and Hamiltonian evolution, it gives the disconnected situation above. The identical-endpoint Poisson example shows why the zero-current conclusion should not be extended to all endpoint geometries.

### 4.3 A retained ancillary system changes the reset property

If a counted jump instead has the form

$$
J_+=\sqrt\Gamma\,|a\rangle\langle b|\otimes I_A,
$$

its rank is greater than one when the ancillary dimension exceeds one. Its output can retain a conditional ancillary state that depends on earlier evolution. Coupling that state back to the clockwork can correlate successive tick blocks. The independent-block step of the proof is then unavailable.

All persistent degrees of freedom must be included when checking rank one. Enlarging the clockwork remains allowed if a counted jump resets the enlarged system to one fixed pure state, possibly an entangled state. Leaving part of that enlarged system untouched is a different architecture.

### 4.4 Several counted reset pairs do not have the two-port reduction

With several independently counted pairs, a positive tick can reset the system to one of several states, and the loss operator $Q$ contains contributions from every pair. The two endpoint normalization identities no longer close into the displayed $2\times2$ matrix. The present proof therefore supplies no general ceiling for a total signed current assembled from several such interfaces, unless the model reduces to a single effective counted pair.

For example, on four orthogonal states take $J_{1,+}=\sqrt\Gamma|0\rangle\langle1|$ and $J_{2,+}=\sqrt\Gamma|2\rangle\langle3|$, together with their rate-suppressed adjoints. A positive event can leave the clockwork in either $P_0$ or $P_2$. If the interface label is discarded, the unnormalized positive-event map is $\rho\mapsto\Gamma(\rho_{11}P_0+\rho_{33}P_2)$, whose normalized output depends on the incoming state. Retaining the label identifies that output, but still gives several reset states rather than one common state after every positive event. This example identifies the failed hypothesis; it is not a claim that every such model violates the single-pair numerical bound.

Extra **uncounted** channels are permitted when their combined generator is a background $\mathcal G$ satisfying the conditions above. This is why unital dephasing is covered even though the microscopic unraveling has more than two jump operators. Generic extra thermally biased reset pairs need not form a unital background.

### 4.5 The complete event record can support a different time estimator

The theorem concerns $N_+-N_-$, rather than an arbitrary function of the event record. Even the total count $K=N_++N_-$ distinguishes the two tasks. In the identical-endpoint example,

$$
\widehat t=\frac{K}{\Gamma(1+r)}
$$

is unbiased and has variance

$$
\operatorname{Var}\widehat t=\frac{t}{\Gamma(1+r)}.
$$

At $r=1$, the zero-affinity limit, the signed current has zero mean while this total-count estimator still carries timing information. This uses only the number of events, without borrowing timestamps from an external reference clock.

[Macieszczak's ultimate kinetic uncertainty relation](../references/README.md#mac24) addresses optimal weighted transition observables and conditional waiting-time statistics in classical and semi-Markov processes, including quantum reset processes. Those observables and costs differ from the signed paired-channel current constrained here. Thus the entropy-affinity ceiling should be stated for its specified current, rather than as a bound on every estimator obtainable from a reset clock's output.
