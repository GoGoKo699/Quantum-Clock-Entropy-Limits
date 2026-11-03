# A precision bound independent of clock size

A coherent delay can make successive ticks much more regular than a purely dissipative clock. The remaining question is whether enlarging that delay can make the precision arbitrarily high while the bias of its tick interface stays fixed. For the [single-interface model](model.md), the answer is no: the precision is bounded by a function of that bias alone.

This page proves the bound. The [construction](achievability.md) then shows that logarithmic affinity cost is achievable. An [extension](extensions.md) explains which additional unital dynamics preserve the converse.

## Theorem

Let $H$ be any time-independent Hermitian operator on a finite-dimensional clockwork. Fix normalized states $|a\rangle,|b\rangle$, a rate $\Gamma>0$, and $0<r<1$. The two resolved tick channels are

$$
J_+=\sqrt{\Gamma}\,|a\rangle\langle b|,
\qquad
J_-=\sqrt{\Gamma r}\,|b\rangle\langle a|.
$$

The states need not be orthogonal. The generator on this page contains $-i[H,\cdot]$ and these two dissipators only. The counted observable is the net number of signed ticks,

$$
N(t)=N_+(t)-N_-(t),
\qquad
\Sigma=-\log r.
$$

Work on the active subspace defined below, and assume that the asymptotic net current $j$ is positive. Then the limits

$$
j=\lim_{t\to\infty}\frac{\mathbb E N(t)}{t},
\qquad
v_N=\lim_{t\to\infty}\frac{\operatorname{Var}N(t)}{t}
$$

exist, and the Fano factor $F=v_N/j$ and precision $\mathcal P=1/F$ satisfy

$$
\boxed{
F\ge\frac{r^2(1+r)}{1-r},
\qquad
\mathcal P\le
\frac{1-r}{r^2(1+r)}
=e^{2\Sigma}\tanh\!\left(\frac{\Sigma}{2}\right).
}
$$

The bound is uniform in the clock dimension, the spectrum and matrix elements of $H$, the states defining the interface, and the overall rate $\Gamma$. It does not assert that its coefficient or exponential coefficient is optimal. The [model](model.md) distinguishes the rate-ratio statement from its interpretation as thermodynamic entropy flow.

The proof uses two facts about the physical dynamics. A tick resets the state, so complete intervals ending at positive ticks can be treated as independent renewal blocks. In addition, the integrated coherent transfer between the two interface states obeys a positivity constraint. A freely chosen semi-Markov waiting-time model need not obey that constraint.

## 1. Active subspace and eventual absorption

Write $P_a=|a\rangle\langle a|$ and $P_b=|b\rangle\langle b|$. The active space is the smallest $H$-invariant subspace containing both interface states:

$$
\mathcal K=\operatorname{span}\{H^k|a\rangle,H^k|b\rangle:k\ge0\}.
$$

All operators below are restricted to $\mathcal K$, and $I$ denotes its identity. Its orthogonal complement is an invariant dark sector: neither tick acts there. An initial state entirely in that complement is not a ticking clock. Starting immediately after a positive tick places the state in $\mathcal K$ automatically.

Between ticks, the unnormalized state evolves as $K_t\rho K_t^\dagger$, where

$$
Q=\Gamma(P_b+rP_a),
\qquad
G=-iH-\frac{Q}{2},
\qquad
K_t=e^{tG}.
$$

Every eigenvalue of $G$ on $\mathcal K$ has strictly negative real part. To see this, first note that $G+G^\dagger=-Q\le0$, so all real parts are nonpositive. If $G|\psi\rangle=i\omega|\psi\rangle$, then taking the real part of its expectation gives $\langle\psi|Q|\psi\rangle=0$. Since $r>0$, both $\langle a|\psi\rangle$ and $\langle b|\psi\rangle$ vanish. The eigenvalue equation then makes $|\psi\rangle$ an eigenvector of $H$, orthogonal to every vector generating $\mathcal K$. This is impossible for a nonzero vector in $\mathcal K$.

Finite dimensionality therefore gives exponentially decaying no-tick survival, with constants that may depend on the individual clock. In particular, the next tick occurs almost surely and its waiting time has an exponential moment near the origin. These clock-dependent decay constants are used only to justify convergence; they do not enter the final precision bound.

## 2. Integrated transfer is reciprocal

Differentiating $K_t^\dagger K_t$ and $K_tK_t^\dagger$, and integrating their decay from $I$ to zero, gives

$$
\int_0^\infty K_t^\dagger QK_t\,dt=I,
\qquad
\int_0^\infty K_tQK_t^\dagger\,dt=I.
$$

For the second identity, use the fact that $K_t$ commutes with $G$ and $K_t^\dagger$ commutes with $G^\dagger$:

$$
\frac{d}{dt}(K_tK_t^\dagger)
=K_t(G+G^\dagger)K_t^\dagger
=-K_tQK_t^\dagger.
$$

These contraction and active-sector identities are shared with the [source-balance argument](../references/README.md#sb). Their role here is to constrain current fluctuations after resetting, rather than to estimate an absorption-based steady current.

Define four integrated transition intensities,

$$
C_{ij}=\int_0^\infty
|\langle i|K_t|j\rangle|^2\,dt,
\qquad i,j\in\{a,b\}.
$$

Sandwiching the two contraction identities with $|a\rangle$ gives

$$
\Gamma C_{ba}+\Gamma r C_{aa}=1,
\qquad
\Gamma C_{ab}+\Gamma r C_{aa}=1.
$$

Hence $C_{ab}=C_{ba}$. This is **integrated two-port reciprocity**. It requires neither a real Hamiltonian nor time-reversal symmetry of the instantaneous transition amplitudes. It also does not require orthogonal interface states.

Set

$$
A=\Gamma C_{ba}.
$$

Starting from $|a\rangle$, $A$ is the probability that the next tick is positive. Starting from $|b\rangle$, integrated reciprocity makes the probability of a negative tick $rA$. The normalization identities give

$$
C_{aa}=\frac{1-A}{\Gamma r},
\qquad
C_{bb}=\frac{1-rA}{\Gamma},
\qquad
C_{ab}=C_{ba}=\frac{A}{\Gamma}.
$$

## 3. Positivity limits consecutive ticks of the same sign

The endpoint matrix

$$
C=\begin{pmatrix}C_{aa}&C_{ab}\\C_{ba}&C_{bb}\end{pmatrix}
$$

is positive semidefinite. This assertion concerns an integrated quantum evolution; positivity of the individual entries alone would not establish it.

Define the no-tick superoperator and its integrated map by

$$
\mathcal L_0(X)=-i[H,X]-\frac12\{Q,X\},
\qquad
\mathcal R=(-\mathcal L_0)^{-1}
=\int_0^\infty K_t(\cdot)K_t^\dagger\,dt.
$$

The inverse exists by the stability just proved. With the Hilbert–Schmidt inner product $\langle X,Y\rangle=\operatorname{Tr}(X^\dagger Y)$, the operator $\mathscr A=-\mathcal L_0$ is accretive:

$$
\operatorname{Re}\langle X,\mathscr A X\rangle
=\frac12\left(
\|Q^{1/2}X\|_2^2+
\|XQ^{1/2}\|_2^2
\right)\ge0.
$$

Its inverse is also accretive. Indeed, if $Y=\mathscr A^{-1}X$, then

$$
\operatorname{Re}\langle X,\mathscr A^{-1}X\rangle
=\operatorname{Re}\langle\mathscr A Y,Y\rangle\ge0.
$$

For real $x,y$, take the Hermitian operator $D=xP_a+yP_b$. The map $\mathcal R$ preserves Hermiticity, so

$$
\operatorname{Tr}[D\mathcal R(D)]
=\begin{pmatrix}x&y\end{pmatrix}
C
\begin{pmatrix}x\\y\end{pmatrix}
\ge0.
$$

Together with $C_{ab}=C_{ba}$, this proves the claim even when $P_a,P_b$ are not orthogonal.

Its determinant is nonnegative. Substituting the previous expressions yields

$$
(1-A)(1-rA)\ge rA^2,
$$

and therefore

$$
\boxed{A\le\frac{1}{1+r}.}
$$

The interface consequently retains a minimum chance of interrupting a run of positive ticks. That restriction cannot be removed by increasing the coherent dimension.

## 4. Renewal blocks and their signed rewards

Each positive tick returns the clockwork to $P_a$. Consider the interval from immediately after one positive tick through the next positive tick. Denote its duration by $T$, the number of intervening negative ticks by $M$, and its net reward by

$$
Y=1-M.
$$

The pairs $(T,Y)$ of successive blocks are independent and identically distributed. Waiting time and reward within one block may be correlated; the proof retains that correlation throughout.

The embedded sign process has transition probabilities

| Previous tick | Next positive tick | Next negative tick |
|---|---:|---:|
| Positive | $A$ | $1-A$ |
| Negative | $1-rA$ | $rA$ |

Accordingly,

$$
\Pr(Y=1)=A,
\qquad
\Pr(Y=-k)=(1-A)(1-rA)(rA)^k,
\quad k=0,1,2,\ldots.
$$

The reward mean is

$$
q:=\mathbb E Y
=\frac{A(1-r)}{1-rA}.
$$

Thus $A>0$ is exactly the positive-current case. If $A=0$, ticks alternate and the net count does not accumulate. For $A>0$, the remaining moments needed below are

$$
\mathbb E\!\left[Y^2\mathbf 1_{\{Y\le0\}}\right]
=\frac{(1-A)rA(1+rA)}{(1-rA)^2},
\qquad
\frac qA=\frac{1-r}{1-rA}\le1.
$$

### Why the long-time variance formula applies

Both the waiting times and the block rewards have sufficiently strong tails. To make this explicit, let $\widehat w_{\sigma|\tau}(\theta)$ be the exponential transform of the next-tick density, conditioned on the previous sign. The no-tick stability established above makes each transform finite for $\theta$ in a neighborhood of zero. Summing over negative runs gives

$$
\mathbb E[e^{\theta T+zM}]
=\widehat w_{+|+}(\theta)
+\frac{e^z\widehat w_{-|+}(\theta)
\widehat w_{+|-}(\theta)}
{1-e^z\widehat w_{-|-}(\theta)}.
$$

At the origin the denominator is $1-rA>0$, so this joint transform is finite in a neighborhood of $(0,0)$. In particular, all moments used in the renewal argument exist. There is no accumulation of infinitely many ticks in finite time because the total tick intensity is bounded by $\Gamma(1+r)$.

Let $\mu=\mathbb E T$. The renewal-reward law and variance formula therefore give

$$
j=\frac q\mu,
\qquad
v_N=\frac{\mathbb E[(Y-jT)^2]}{\mu},
\qquad
\boxed{F=\frac{\mathbb E[(Y-jT)^2]}q.}
$$

One way to see the variance formula is to center each complete block by $Z_i=Y_i-jT_i$. These are iid mean-zero variables. Applying the iid sum variance identity at the first block crossing time, then the renewal law for the number of blocks, gives a variance per unit time of $\mathbb E Z_i^2/\mu$. The unfinished block and the initial waiting interval have uniformly bounded second moments under the exponential-moment condition; their contribution and covariance are sublinear in time. The same argument justifies convergence of the second moments, not only convergence in distribution. The reset-clock perspective and its distinction from clocks retaining intertick quantum memory are discussed in [the clock literature](../references/README.md#m26).

## 5. Optimizing over all nonnegative block durations

Only nonnegativity of duration is now needed. Put $Z=jT\ge0$, so $\mathbb E Z=q$. On the event $Y\le0$,

$$
(Y-Z)^2\ge Y^2.
$$

On the event $Y=1$, nonnegativity outside that event implies

$$
\mathbb E[Z\mid Y=1]\le\frac qA\le1.
$$

Conditional Jensen's inequality, followed by monotonicity of $(1-x)^2$ for $x\le1$, gives

$$
\mathbb E[(Y-Z)^2]
\ge A\left(1-\frac qA\right)^2
+\mathbb E\!\left[Y^2\mathbf 1_{\{Y\le0\}}\right]
=\frac{A(1-A)r(1+r)}{(1-rA)^2}.
$$

This is a relaxation of the actual dynamics: it even permits all nonpositive-reward blocks to take zero time. A bound surviving that relaxation applies to the physical clock.

Dividing by $q$ yields

$$
F\ge
\frac{r(1+r)(1-A)}{(1-r)(1-rA)}.
$$

For fixed $r\in(0,1)$, the right-hand side decreases with $A$, because

$$
\frac{d}{dA}\frac{1-A}{1-rA}
=-\frac{1-r}{(1-rA)^2}<0.
$$

Using $A\le1/(1+r)$ proves the theorem.

## Consequence and boundary

At fixed finite $\Sigma$, increasing the clock dimension cannot make $\mathcal P$ diverge. Near equilibrium the bound is $\mathcal P\le\Sigma/2+O(\Sigma^2)$; at large bias it is exponential. The [finite-affinity chain](achievability.md) realizes exponential-order growth, so the minimum affinity needed for precision $p$ grows as $\Theta(\log p)$ in this model.

Exponential precision enhancement was already demonstrated by [Meier and collaborators](../references/README.md#m25). The converse here addresses its ultimate order for a specified single rank-one interface. It is not a theorem for every autonomous quantum clock: additional nonunital resources, higher-rank resets, retained quantum information after ticks, or a different tick statistic require their own accounting. The [model boundaries](model.md) and [extensions](extensions.md) state these distinctions explicitly.
