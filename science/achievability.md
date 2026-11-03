# A finite-affinity clock attaining logarithmic cost

The [precision bound](precision_bound.md) shows that a single thermally paired rank-one interface needs affinity at least of order $\log p$ to reach precision $p$. This page constructs a clock that attains that order with a real nearest-neighbor Hamiltonian whose norm stays bounded.

The starting escape mechanism is an inherited one: a maximal exceptional point produces an Erlang waiting-time law. [Holst, Blasi and Khandelwal](../references/README.md#hbk26) derive this mechanism for a chain with terminal loss, and [Meier and collaborators](../references/README.md#m25) establish the broader possibility of exponential precision enhancement in coherent clocks. The task here is to close the escape process into an autonomous clock with a finite backward tick rate, and to control its long-time signed-count precision rigorously.

The resulting clock becomes slower as it becomes more precise. This rate cost is part of the construction.

## Constructive theorem

For every integer $d\ge2$, there is a $d$-dimensional clock in the [single-interface model](model.md) with orthogonal interface states, a real nearest-neighbor Hamiltonian, and forward tick rate normalized to $\Gamma=1$, such that

$$
\|H\|\le\frac1{\sqrt3},
\qquad
0<r\le\frac1{65536\,d^3}
\quad\Longrightarrow\quad
\mathcal P_r\ge d.
$$

With $r=1/(65536d^3)$, its affinity is

$$
\Sigma=3\log d+16\log2.
$$

Its mean interval between positive ticks is $\Theta(d^2)$, and its net tick rate is $\Theta(d^{-2})$. Restoring a general rate $\Gamma$ multiplies $H$ and all rates by $\Gamma$, so the net tick rate becomes $\Theta(\Gamma/d^2)$ without changing the precision or affinity.

The constants are conservative. The theorem establishes the logarithmic order of affinity cost; it does not optimize its coefficient, the clock dimension, or the resolution at a given precision.

## 1. A bounded real chain with one exceptional point

Take a path basis $|1\rangle,\ldots,|d\rangle$, interface states

$$
|a\rangle=|1\rangle,
\qquad
|b\rangle=|d\rangle,
\qquad
\kappa=\frac1d,
$$

and the Hamiltonian

$$
H=\sum_{j=1}^{d-1}g_j
\bigl(|j\rangle\langle j+1|+|j+1\rangle\langle j|\bigr),
$$

where

$$
\boxed{
g_j^2=
\frac{\kappa^2j(2d-j)}
{4(2d-2j-1)(2d-2j+1)}.
}
$$

All couplings are positive. Setting $k=d-j$ rewrites them as

$$
g_j^2=\frac{d^2-k^2}{4d^2(4k^2-1)}<\frac1{12}.
$$

The row-sum bound therefore gives $\|H\|\le2\max_jg_j<1/\sqrt3$.

First omit backward ticks. The forward jump is $J_+=|a\rangle\langle b|$, and the no-tick amplitude matrix is

$$
G_0=-iH-\frac12P_b.
$$

Its characteristic polynomial is

$$
\boxed{\det(sI-G_0)=(s+\kappa/2)^d.}
$$

Thus $G_0+\kappa I/2$ is nilpotent. The nonzero path couplings make an endpoint a cyclic vector, so the repeated eigenvalue forms a single Jordan block. All eigenvalues nevertheless have negative real part, and no-tick survival decays to zero.

### Polynomial proof of the characteristic identity

Rescale temporarily to $\kappa=2$, for which the terminal rate is $\Gamma=2d$. Let $q_n(s)$ be the determinant of the undamped leading $n\times n$ block of $sI+iH$. The tridiagonal determinant recurrence is

$$
q_0=1,\qquad q_1=s,
$$

$$
q_{n+1}
=s q_n+
\frac{n(2d-n)}{(2d-2n-1)(2d-2n+1)}q_{n-1}.
$$

For $\lambda=\tfrac12-d$, its solution is the monic polynomial

$$
q_n(s)=
\sum_{k=0}^{\lfloor n/2\rfloor}
\frac{(-1)^k n!(\lambda)_{n-k}}
{4^k k!(n-2k)!(\lambda)_n}
s^{n-2k},
$$

where $(x)_m=x(x+1)\cdots(x+m-1)$ and $(x)_0=1$. The half-integer parameter ensures that none of the denominators vanishes. Substituting the coefficients verifies the recurrence and the initial conditions. This is also the monic Gegenbauer recurrence at the stated parameter.

At $n=d$, use $(\tfrac12-k)_k=(-1)^k(\tfrac12)_k$ and $4^kk!(\tfrac12)_k=(2k)!$. At $n=d-1$, use the corresponding identities with $\tfrac32$. The coefficients reduce to $\binom d{2k}$ and $d^{-1}\binom d{2k+1}$, respectively. Therefore

$$
q_d(s)=\frac{(s+1)^d+(s-1)^d}{2},
$$

$$
q_{d-1}(s)=\frac{(s+1)^d-(s-1)^d}{2d}.
$$

Adding the terminal damping adds $d q_{d-1}$ to the determinant, giving

$$
\det(sI-G_0)=q_d+dq_{d-1}=(s+1)^d
$$

in the rescaled variables. Scaling all amplitudes and rates by $\kappa/2$ proves the physical identity $(s+\kappa/2)^d$.

## 2. The ideal escape law

For a tridiagonal path, the endpoint entry of the resolvent has constant numerator:

$$
\langle b|(sI-G_0)^{-1}|a\rangle
=\frac{(-i)^{d-1}\prod_{j=1}^{d-1}g_j}
{(s+\kappa/2)^d}.
$$

Inverting its Laplace transform gives

$$
\langle b|e^{tG_0}|a\rangle
=\frac{(-i)^{d-1}\prod_jg_j}{(d-1)!}
t^{d-1}e^{-\kappa t/2}.
$$

The coupling product is

$$
\prod_{j=1}^{d-1}g_j^2
=\frac{\kappa^{2d-2}(d-1)!^2}{d(2d-2)!}.
$$

Since $\Gamma=d\kappa=1$, the first positive tick has density

$$
\boxed{
w_0(t)=\kappa e^{-\kappa t}
\frac{(\kappa t)^{2d-2}}{(2d-2)!}.
}
$$

It is an Erlang distribution with shape $2d-1$ and rate $\kappa$. If $T_0$ denotes that waiting time, then

$$
\mu_0:=\mathbb E T_0=d(2d-1),
\qquad
\operatorname{Var}T_0=d^2(2d-1),
$$

$$
v_0:=\mathbb E T_0^2=2d^3(2d-1),
\qquad
F_0=\frac1{2d-1}.
$$

Resetting to $|a\rangle$ after this escape makes successive ideal waiting times iid. However, $r=0$ corresponds to infinite affinity. The finite-affinity theorem requires an estimate that remains valid after adding backward ticks.

## 3. A resolvent bound that survives the exceptional point

Eigenvalue perturbation is ill-conditioned at a high-order exceptional point. The relevant waiting-time quantities instead admit a direct norm bound.

Let

$$
\mathcal L_0(X)=-i[H,X]-\frac12\{P_b,X\},
\qquad
\mathcal R_0=(-\mathcal L_0)^{-1}
=\int_0^\infty e^{tG_0}(\cdot)e^{tG_0^\dagger}\,dt.
$$

This is the evolution killed at its first positive tick. Define the emitted-wavepacket map

$$
(W\psi)(t)=\langle b|e^{tG_0}|\psi\rangle.
$$

The [absorption identity](precision_bound.md#2-integrated-transfer-is-reciprocal) with $Q=P_b$ gives $W^\dagger W=I$. Hence $W$ is an isometry into $L^2(\mathbb R_+)$. The nilpotent form of $G_0+\kappa I/2$ shows that its image lies in

$$
E_d=\operatorname{span}\{
e^{-\kappa t/2}t^k:0\le k<d
\}.
$$

Both spaces have dimension $d$, so the image equals $E_d$.

An orthonormal basis of $E_d$ is

$$
\ell_n(t)=\sqrt\kappa\,e^{-\kappa t/2}L_n(\kappa t),
\qquad n=0,\ldots,d-1,
$$

where $L_n$ are ordinary Laguerre polynomials. Their identities

$$
\int_0^\infty e^{-x}L_n(x)L_m(x)\,dx=\delta_{nm},
$$

$$
xL_n(x)=(2n+1)L_n(x)-(n+1)L_{n+1}(x)-nL_{n-1}(x)
$$

follow, for example, by integration by parts from the Rodrigues formula $L_n(x)=e^x(n!)^{-1}(d/dx)^n(e^{-x}x^n)$. Thus the compression of multiplication by $t$ to $E_d$ is tridiagonal, with diagonal $(2n+1)/\kappa$ and neighboring entries $-(n+1)/\kappa$. Its absolute row sums are at most $4d/\kappa$.

The mean waiting-time operator is

$$
S_0=\mathcal R_0^\dagger(I)
=\int_0^\infty e^{tG_0^\dagger}e^{tG_0}\,dt
=W^\dagger tW.
$$

The last equality follows by integrating $-t\,d(e^{tG_0^\dagger}e^{tG_0})/dt$; the boundary term vanishes. Therefore

$$
\|S_0\|\le\frac{4d}{\kappa}=4d^2.
$$

For a completely positive map $\Phi$, trace/operator norm duality gives $\|\Phi\|_{1\to1}=\|\Phi^\dagger(I)\|$. One may verify the upper bound using a Stinespring representation and obtain equality on a positive unit-trace eigenstate of $\Phi^\dagger(I)$. Applying it to $\mathcal R_0$ proves

$$
\boxed{\|\mathcal R_0\|_{1\to1}\le B:=4d^2.}
$$

This bound concerns all initial states, not only the endpoint used in the ideal Erlang calculation.

## 4. Adding finite backward ticks

Now add $J_-=\sqrt r\,V$, where $V=|b\rangle\langle a|$. In an interval ending at the next positive tick, negative ticks are retained and only positive ticks terminate the evolution. Its generator is

$$
\mathcal L_r=\mathcal L_0+r\mathcal D[V],
\qquad
\mathcal D[V](X)=VXV^\dagger-\frac12\{P_a,X\}.
$$

In particular, this is not the evolution conditioned on no tick of either sign.

### Stability before perturbing the inverse

The operator $S_0$ is positive definite, because every nonzero initial vector has positive survival probability on an interval after time zero. It obeys

$$
\mathcal L_0^\dagger(S_0)=-I,
\qquad
\|S_0\|\le B.
$$

Since $\|\mathcal D[V]\|_{1\to1}\le2$, its adjoint has operator norm at most $2$. Hence

$$
\mathcal L_r^\dagger(S_0)
\le-(1-2rB)I.
$$

For a positive killed state $\rho_t=e^{t\mathcal L_r}\rho_0$, let $V_0(t)=\operatorname{Tr}(S_0\rho_t)$. If $2rB<1$, then

$$
V_0'(t)
\le-(1-2rB)\operatorname{Tr}\rho_t
\le-\frac{1-2rB}{B}V_0(t).
$$

Because $\lambda_{\min}(S_0)>0$, this proves exponential decay of the survival probability. Absorption at a positive tick is almost sure, all block-time moments exist, and the inverse has the integral representation

$$
\mathcal R_r=(-\mathcal L_r)^{-1}
=\int_0^\infty e^{t\mathcal L_r}\,dt.
$$

The identity is therefore justified before using its Neumann series.

### Resolvent estimates

If $2rB\le1/2$, that series and the resolvent identity yield

$$
\|\mathcal R_r\|_{1\to1}\le2B,
\qquad
\|\mathcal R_r-\mathcal R_0\|_{1\to1}\le4rB^2.
$$

Both integrated maps are completely positive. Their norm estimates will control the joint waiting-time and signed-count fluctuations.

## 5. Joint block moments

Start each interval from $P_a$. Let $T$ be its duration and $M$ the number of negative ticks before its terminal positive tick. Its net reward is $Y=1-M$. Introduce

$$
\mu=\mathbb E T,\quad v=\mathbb E T^2,\quad
m=\mathbb E M,\quad
f_2=\mathbb E[M(M-1)],\quad
w=\mathbb E(TM).
$$

The positive exit functional and the reverse recycling map are

$$
\ell_+(X)=\operatorname{Tr}(P_bX),
\qquad
\mathcal I_-(X)=VXV^\dagger.
$$

Trace loss is entirely through the positive exit: $\operatorname{Tr}\mathcal L_r(X)=-\ell_+(X)$. Integrating gives the identity

$$
\ell_+\mathcal R_r(X)=\operatorname{Tr}X.
$$

The joint Laplace/probability-generating transform is, in a neighborhood of $(s,u)=(0,1)$,

$$
\mathbb E[e^{-sT}u^M]
=\ell_+\left[
s\,\operatorname{id}-\mathcal L_r-r(u-1)\mathcal I_-
\right]^{-1}(P_a).
$$

Stability makes this transform analytic there. Differentiating and using the exit identity gives

$$
\mu=\operatorname{Tr}(\mathcal R_rP_a),
\qquad
v=2\operatorname{Tr}(\mathcal R_r^2P_a),
$$

$$
m=r\operatorname{Tr}(\mathcal I_-\mathcal R_rP_a),
$$

$$
f_2=2r^2\operatorname{Tr}
(\mathcal I_-\mathcal R_r\mathcal I_-\mathcal R_rP_a),
$$

$$
w=r\operatorname{Tr}
\left[(\mathcal R_r\mathcal I_-\mathcal R_r
+\mathcal I_-\mathcal R_r^2)P_a\right].
$$

Since $\|\mathcal I_-\|_{1\to1}=1$, the resolvent estimates imply

| Quantity | Bound |
|---|---:|
| Mean-time change | $\lvert\mu-\mu_0\rvert\le4rB^2$ |
| Second-moment change | $\lvert v-v_0\rvert\le24rB^3$ |
| Mean negative count | $m\le2rB$ |
| Second factorial negative count | $f_2\le8r^2B^2$ |
| Mixed time/count moment | $w\le8rB^2$ |

For example, the second-moment estimate uses $\mathcal R_r^2-\mathcal R_0^2=\mathcal R_r(\mathcal R_r-\mathcal R_0)+(\mathcal R_r-\mathcal R_0)\mathcal R_0$. The other estimates follow directly from the displayed moment expressions.

Because $\mathbb E Y=1-m$ and $\mathbb E(TY)=\mu-w$, the [renewal-reward formula](precision_bound.md#4-renewal-blocks-and-their-signed-rewards) becomes the exact identity

$$
\boxed{
F_r=(1-m)\frac v{\mu^2}-1
+\frac{2w}{\mu}+\frac{f_2}{1-m}.
}
$$

This identity includes the correlations between negative ticks and block duration.

## 6. An explicit finite-affinity estimate

Suppose $rd^2\le1/128$. With $B=4d^2$, all preceding perturbation conditions hold. In addition,

$$
|\mu-\mu_0|\le\mu_0/2,
\qquad m\le1/2,
\qquad\mu_0\ge d^2,
\qquad v_0\le2\mu_0^2.
$$

The ratio of time moments obeys

$$
\frac v{\mu^2}-\frac{v_0}{\mu_0^2}
\le\frac{96rB^3}{\mu_0^2}
+\frac{80rB^2}{\mu_0}
\le7424rd^2.
$$

To obtain the first inequality, use $\mu\ge\mu_0/2$ in the second-moment change and

$$
\left|\frac1{\mu^2}-\frac1{\mu_0^2}\right|
\le\frac{10|\mu-\mu_0|}{\mu_0^3}
$$

in the denominator change. The remaining positive terms satisfy

$$
\frac{2w}{\mu}\le512rd^2,
\qquad
\frac{f_2}{1-m}\le256r^2d^4\le64rd^2.
$$

Dropping the nonpositive contribution $-mv/\mu^2$ in the exact Fano expression therefore proves

$$
\boxed{
F_r\le\frac1{2d-1}+8000rd^2.
}
$$

Now take $0<r\le1/(65536d^3)$. For $d\ge2$,

$$
F_r\le
\frac1{2d-1}+\frac{8000}{65536d}
\le\frac1d\left(\frac23+\frac{8000}{65536}\right)
<\frac1d.
$$

This proves $\mathcal P_r\ge d$.

The mean duration remains between $\mu_0/2$ and $3\mu_0/2$, and the mean reward lies between $1/2$ and $1$. Consequently a convenient explicit rate estimate is

$$
\frac1{6d^2}\le
j_r=\frac{1-m}{\mu}
\le\frac4{3d^2}.
$$

Thus the construction's higher precision comes with a lower net tick rate, while all native coherent and jump strengths remain bounded.

## 7. The logarithmic affinity-cost law

For $p\ge2$, define $\Sigma_{\min}(p)$ as the infimum of the affinity over clocks in the [model](model.md) whose long-time precision is at least $p$. The converse gives

$$
\Sigma_{\min}(p)\ge\frac12\log p.
$$

For the upper bound, take $d=\lceil p\rceil$ in the construction and $r=1/(65536d^3)$. It gives

$$
\Sigma_{\min}(p)
\le3\log\lceil p\rceil+16\log2.
$$

Therefore

$$
\boxed{\Sigma_{\min}(p)=\Theta(\log p)\qquad(p\to\infty).}
$$

The two constants multiplying $\log p$ do not match. The result establishes the order of the cost and a finite ceiling at fixed affinity; it leaves the optimal exponential coefficient open. The ideal exceptional-point escape law and earlier exponential clock advantage retain their original attribution. The finite-affinity estimates above show explicitly how the inherited escape mechanism can operate as a resetting clock without treating its backward ticks as absent.
