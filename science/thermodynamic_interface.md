# Thermodynamic meaning of the reset affinity

The [precision theorem](precision_bound.md) is an exact statement about the rate ratio of a pair of counted quantum jumps. Interpreting that ratio as entropy produced per tick requires a physical reservoir model. This page specifies a tightly coupled autonomous interface for which that interpretation holds, derives its entropy accounting, and separates the effective clock theorem from microscopic approximation errors. The [related-work comparison](../references/related_work.md) identifies the scientific antecedents and their scope.

Throughout, entropy is measured in units of Boltzmann's constant and $\hbar=1$.

## 1. Mathematical affinity and the measured current

The [clock model](model.md) has counted jumps

$$
J_+=\sqrt{\Gamma}\,|a\rangle\langle b|,
\qquad
J_-=\sqrt{\Gamma r}\,|b\rangle\langle a|,
\qquad
r=e^{-\Sigma}\in(0,1).
$$

Its signed output is

$$
N(t)=N_+(t)-N_-(t),
\qquad
j=\lim_{t\to\infty}\frac{\mathbb E N(t)}{t}>0.
$$

Here $\Sigma=\log(\Gamma_+/\Gamma_-)$ is a dimensionless **jump affinity**, regardless of how the generator is implemented. The mathematical result concerns the inverse Fano precision

$$
\mathcal P
=\lim_{t\to\infty}
\frac{\mathbb E N(t)}{\operatorname{Var}N(t)}.
$$

The generator alone does not identify bath temperatures, heat quanta, or the resource used to implement its Hamiltonian. For example, a coherent coupling may arise from a static resonant interaction or from an externally applied field in a rotating frame. These implementations can have different thermodynamic accounts despite sharing an effective equation.

The construction below realizes the orthogonal endpoint case using a static Hamiltonian and two reservoirs. The converse also permits nonorthogonal reset states and more general Hermitian Hamiltonians; we do not claim a microscopic thermal realization for every member of that larger mathematical class.

## 2. An autonomous five-level interface

Meier et al. describe a five-level ticking element, a one-excitation latch, and elimination of intermediate levels to obtain the same effective biased reset pair. Their proposed implementation is the physical antecedent for the interface considered here; see the Methods section “Applicability of the master equation” in [M25](../references/README.md#m25).

We make the idealized interface assumptions explicit. Let its levels be

$$
|g\rangle,\quad|\ell\rangle,\quad|m\rangle,\quad|e\rangle,\quad|r\rangle.
$$

The complete excitation cycle is

$$
g\longrightarrow\ell\longrightarrow m
\longrightarrow e\longrightarrow r\longrightarrow g.
$$

The $g\leftrightarrow\ell$ and $r\leftrightarrow g$ transitions couple coherently to opposite ends of the transport chain. The middle three transitions form the thermally driven reset path. We identify the effective endpoint states as $b=\ell$ and $a=r$ after eliminating $m$ and $e$.

The latch has a specific role: while one excitation is propagating through the chain, the interface is in $g$, which the thermal transitions do not address. A second excitation cannot be emitted during that interval. On its return, the excitation enables the reset path. The complete relevant Hilbert space therefore contains one propagating or interface excitation, rather than an independently pumped many-particle stream.

Choose equal bare endpoint energies

$$
E_\ell=E_r=\omega.
$$

The cold reservoir, with inverse temperature $\beta_C$, mediates $\ell\leftrightarrow m$ and $e\leftrightarrow r$. The hot reservoir, with $\beta_H<\beta_C$, mediates $m\leftrightarrow e$. Define

$$
q_1=E_\ell-E_m>0,\qquad
Q=E_e-E_m>0,\qquad
q_2=E_e-E_r>0.
$$

Endpoint resonance gives $q_1+q_2=Q$. In one forward reset, the interface releases $q_1$ and $q_2$ into the cold bath and absorbs $Q$ from the hot bath. Thus the reservoir entropy increment of a completed forward reset is

$$
\Sigma_{\mathrm{cycle}}
=\beta_C(q_1+q_2)-\beta_HQ
=(\beta_C-\beta_H)Q.
$$

The reverse cycle carries the opposite entropy increment. With local detailed balance on each thermal edge,

$$
\frac{k_{\ell m}}{k_{m\ell}}=e^{\beta_Cq_1},
\qquad
\frac{k_{me}}{k_{em}}=e^{-\beta_HQ},
\qquad
\frac{k_{er}}{k_{re}}=e^{\beta_Cq_2}.
$$

Consequently,

$$
\frac{k_{\ell m}k_{me}k_{er}}
     {k_{m\ell}k_{em}k_{re}}
=e^{\Sigma_{\mathrm{cycle}}}.
$$

A controlled Markovian elimination of the serial intermediate states yields effective forward and reverse reset rates with this ratio. In that effective model,

$$
\Sigma=\Sigma_{\mathrm{cycle}}
=(\beta_C-\beta_H)Q.
$$

This equality depends on the specified serial path and local detailed balance. It is not inferred merely from the notation $J_-=e^{-\Sigma/2}J_+^\dagger$.

## 3. Exact entropy accounting before elimination

The serial interface has a useful conservation identity that does not assume instantaneous reset. Let $N_1$, $N_H$, and $N_2$ be the signed counts on $\ell\leftrightarrow m$, $m\leftrightarrow e$, and $e\leftrightarrow r$, respectively, positive along the forward path. Let $n_m,n_e\in\{0,1\}$ be the intermediate-state occupancies in a resolved jump trajectory.

Because no additional edge enters or leaves $m$ or $e$,

$$
\Delta n_m=N_1-N_H,\qquad
\Delta n_e=N_H-N_2.
$$

The reservoir entropy change is

$$
S_{\mathrm{env}}(t)
=\beta_Cq_1N_1(t)-\beta_HQN_H(t)
 +\beta_Cq_2N_2(t).
$$

Eliminating $N_H$ and $N_2$ gives the exact identity

$$
\boxed{
S_{\mathrm{env}}(t)
=\Sigma N_1(t)
 +(\beta_HQ-\beta_Cq_2)\Delta n_m(t)
 -\beta_Cq_2\Delta n_e(t).
}
$$

The last two terms are bounded interface-state terms at each fixed set of energy gaps and bath temperatures. Repeated unsuccessful excursions through part of the path do not create an unaccounted steady heat leak: their signed edge counts cancel except for these endpoint terms.

The three signed edge currents therefore have the same long-time mean. In a stationary positive-current regime,

$$
\dot S_{\mathrm{env}}
=\lim_{t\to\infty}
 \frac{\mathbb E S_{\mathrm{env}}(t)}{t}
=\Sigma j.
$$

The mean system entropy has no extensive growth in a finite stationary clock. Thus $\Sigma$ is also its steady entropy production per net completed reset, for this tightly coupled realization.

Replacing one signed interface-edge count by another changes it by a bounded occupancy term. If the stationary counting variance grows linearly in time, this replacement leaves its diffusion coefficient unchanged: the covariance with a bounded term is at most of order $\sqrt t$, so it vanishes after division by $t$. This establishes equivalence of these microscopic count conventions in the long-time limit. It does **not** establish equivalence of a finite-rate microscopic model and an adiabatically eliminated generator; that is a separate dynamical approximation.

The output must remain the signed net count. If only forward events are registered, their rate is $j_+$ and the reservoir entropy per registered forward event is $\Sigma j/j_+$, generally different from $\Sigma$. A theorem for $N_+-N_-$ is not a theorem for every statistic obtainable from a complete detection record.

## 4. Effective dynamics and microscopic accuracy

There are two distinct levels of exactness:

1. **Given the effective generator**, the precision ceiling and finite-affinity construction are mathematical statements with no adiabatic-elimination error.
2. **Given a finite-rate physical interface**, its entropy identity above is exact under the stated serial local-detailed-balance model, but its reduced timing statistics need not equal those of the effective generator.

The implementation discussed in [M25](../references/README.md#m25) uses a separation between the large bare excitation frequency and the dissipation and coherent-transport scales. Our effective description additionally requires the eliminated levels to relax sufficiently rapidly compared with the retained transport and reset dynamics. A symbolic scale hierarchy alone does not bound the error in a long-time variance.

To transfer a precision claim to a particular finite-rate device, one would need to control its reduced generator or, more directly, the first two relevant counting cumulants. For a growing family of clocks, that control must remain adequate as the desired Fano factor decreases. A fixed absolute error can overwhelm a precision scaling whose ideal Fano factor tends to zero. No uniform microscopic elimination estimate is proved here.

Local bath jumps are assigned the bare transition heats in this model. At finite coherent interaction strength, a globally derived thermal generator may resolve dressed energy differences instead. The present account therefore does not identify every phenomenological choice of $H$ and local dissipators with an exact microscopic thermal master equation at arbitrary coupling.

A related obstruction explains why a single equilibrium reservoir is insufficient for the running orthogonal-port clock. A rank-one thermal jump that is an eigenoperator of the same Hamiltonian,

$$
[H,|a\rangle\langle b|]
=\nu |a\rangle\langle b|,
$$

forces distinct orthogonal $a$ and $b$ to be energy eigenstates. That Hamiltonian supplies no coherent route between these ports. With only the paired jumps, the two levels equilibrate and the signed stationary current vanishes. The two-temperature interface supplies the nonequilibrium bias needed for autonomous circulation. This argument concerns distinct orthogonal ports; it is not an argument about arbitrary overlapping reset states.

## 5. Additional channels and retained memory

The [unital extension](extensions.md) permits a time-independent, trace-preserving unital Lindbladian between the counted resets, provided the no-count evolution is stable on the operating sector. Thus certain unobserved noise channels can be included in the mathematical affinity ceiling.

That extension does not declare unital noise thermodynamically free. Its physical implementation may exchange heat, generate entropy, or consume another resource. The serial-interface identity still accounts for the entropy carried by its three specified thermal edges when no extra edge changes $n_m$ or $n_e$; it need not equal the total entropy of an enlarged device.

Arbitrary nonunital loss or reinjection, additional reset pairs, or heat-leak cycles require a new analysis. Substituting a measured total entropy per tick for $\Sigma$ does not automatically prove a bound for the altered generator.

Complete reset also concerns all degrees of freedom that participate in subsequent timing. An output jump of the form $|a\rangle\langle b|\otimes I_A$ leaves an ancillary memory intact and is not rank one on the full clockwork. It need not regenerate the process assumed in the theorem.

## 6. Precision, rate, and the resources being counted

The [explicit construction](achievability.md) uses a real nearest-neighbor Hamiltonian with bounded coupling strengths in units of a fixed forward rate $\Gamma$. For dimension $d$, it attains

$$
\mathcal P\ge d,\qquad
\Sigma=3\log d+16\log2,
\qquad
j=\Theta(\Gamma d^{-2}).
$$

The logarithmic affinity cost is accompanied by a slower tick rate. It does not establish growing precision at fixed resolution, nor an optimal precision–rate tradeoff. Multiplying the Hamiltonian and all rates by a common factor changes the speed without changing $\Sigma$ or $\mathcal P$, but consumes a correspondingly larger dynamical scale.

The resource priced here is steady operating entropy per signed net tick. The theorem does not price fabrication, Hamiltonian complexity, maintaining the reservoirs, detector memory, record erasure, or every preparation resource. A finite initial preparation is amortized only by taking the long-time limit at each fixed finite clock size. Ideal passive monitoring is the output convention; externally timed control and feedback are different dynamical models.

With these assumptions explicit, the thermodynamic implication is precise: in this tightly coupled reset architecture, increasing coherent dimension alone cannot yield unbounded signed-count precision at a fixed finite entropy per net tick. The logarithmic cost law concerns that architecture and that observable.
