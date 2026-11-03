# Sources and attribution

[Repository overview](../README.md) · [Comparison of claims](related_work.md)

The labels below identify the specific sources used in the scientific account. A citation supplies attribution or a stated premise; it does not transfer a theorem between different operational models. Machine-readable metadata are provided in [sources.json](sources.json).

## WM10

Howard M. Wiseman and Gerard J. Milburn, **Quantum Measurement and Control**, Cambridge University Press (2010), ISBN 978-0-521-80442-4. [Publisher frontmatter](https://assets.cambridge.org/97805218/04424/frontmatter/9780521804424_frontmatter.pdf) · [Publisher contents](https://assets.cambridge.org/97805218/04424/toc/9780521804424_toc.pdf).

The selected educational anchor for Lindblad dynamics, quantum jumps and monitoring. The [learning bridge](../learning/anchor.md) identifies the relevant sections and the additional renewal, resolvent and thermodynamic reasoning supplied by this project. The clock ceiling and finite-bias estimates are not attributed to this textbook.

## M25

Florian Meier et al., **Precision is not limited by the second law of thermodynamics**, *Nature Physics* **21**, 1147–1152 (2025). [DOI:10.1038/s41567-025-02929-2](https://doi.org/10.1038/s41567-025-02929-2) · [Open full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC12263443/) · [arXiv:2407.07948](https://arxiv.org/abs/2407.07948).

Source of the motivating biased quantum-clock architecture, existing exponential precision–entropy advantage, and five-level thermal interface. The main text and relevant Methods were inspected. The full microscopic supplementary derivation is not reproduced here.

## M26

Florian Philippe Meier, **Quantum limits in timekeeping**, doctoral dissertation, TU Wien (2026). [Institutional PDF](https://repositum.tuwien.at/bitstream/20.500.12708/228728/1/Meier%20Florian%20Philippe%20-%202026%20-%20Quantum%20limits%20in%20timekeeping.pdf).

Section 2.2.2, printed pages 49–50, discusses quantum reset clocks and the conjectured extension of an exponential semi-Markov thermodynamic uncertainty relation. The single-pair ceiling proved here does not settle the thesis's more general or sharp conjecture.

## HBK26

Daniel Holst, Gianmichele Blasi and Shishir Khandelwal, **Non-Markovian exceptional points and information backflow: a Heisenberg reaction-coordinate approach**, arXiv:2610.26620v1 (19 October 2026). [Versioned primary HTML](https://arxiv.org/html/2610.26620v1) · [arXiv record](https://arxiv.org/abs/2610.26620).

Section VIII.1 and Appendix H derive the maximal-exceptional-point Erlang escape law under terminal irreversible loss. Section IX discusses autonomous recycling as a possible extension. This mechanism is inherited; the finite-reverse-rate bounds in this repository are separately derived.

## EVS22

Benjamin Ertel, Jann van der Meer and Udo Seifert, **Operationally Accessible Uncertainty Relations for Thermodynamically Consistent Semi-Markov Processes**, *Physical Review E* **105**, 044113 (2022). [DOI:10.1103/PhysRevE.105.044113](https://doi.org/10.1103/PhysRevE.105.044113) · [arXiv:2111.13113](https://arxiv.org/abs/2111.13113).

Reference for the semi-Markov setting discussed in M26. Direction–time consistency assumptions must be checked before a classical semi-Markov entropy is identified with the quantum jump affinity.

## BS25

Kay Brandner and Keiji Saito, **Thermodynamic Uncertainty Relations for Coherent Transport**, *Physical Review Letters* **135**, 046302 (2025). [DOI:10.1103/6nww-8wcp](https://doi.org/10.1103/6nww-8wcp) · [arXiv:2502.07917v2](https://arxiv.org/abs/2502.07917v2).

An exponential uncertainty relation for coherent fermionic transport. The inspected proof uses the Landauer scattering setting; its hypotheses differ from a single excitation reset after every counted jump.

## VHS26

Tan Van Vu, Ryotaro Honma and Keiji Saito, **Universal Precision Limits in General Open Quantum Systems**, *Physical Review Letters* **136**, 190401 (2026). [DOI:10.1103/kldv-l3wl](https://doi.org/10.1103/kldv-l3wl) · [arXiv:2508.21567](https://arxiv.org/abs/2508.21567). See also the [erratum, *Physical Review Letters* **137**, 129901](https://doi.org/10.1103/8hbn-pp39).

The comparison here concerns the quantities entering the general precision bounds, including total entropy and additional trajectory information. No argument relies on an unexamined exact formula in the erratum.

## KL25

Euijoon Kwon and Jae Sung Lee, **A unified framework for classical and quantum uncertainty relations using stochastic representations**, *Communications Physics* **8**, 444 (2025). [DOI:10.1038/s42005-025-02348-y](https://doi.org/10.1038/s42005-025-02348-y) · [Primary preprint HTML](https://arxiv.org/html/2412.04988v2).

Equation (51), the steady-state examples and the reset-process appendix retain a dynamics-dependent quantum correction. They do not immediately give the affinity-only ceiling used here.

## NH25

Tomohiro Nishiyama and Yoshihiko Hasegawa, **Quantum Thermodynamic Uncertainty Relations without Quantum Corrections: A Coherent-Incoherent Correspondence Approach**, arXiv:2505.09973v3 (2025). [Primary HTML](https://arxiv.org/html/2505.09973v3).

Equation (2) imposes a Hamiltonian eigenoperator condition on the jumps. That condition is material when comparing with arbitrary coherent transport between the reset ports.

## MAC24

Katarzyna Macieszczak, **Ultimate Kinetic Uncertainty Relation and Optimal Performance of Stochastic Clocks**, arXiv:2407.09839v1 (2024). [Primary HTML](https://arxiv.org/html/2407.09839v1) · [arXiv record](https://arxiv.org/abs/2407.09839).

The semi-Markov extension and optimal observables depend on conditional waiting-time information. This is a source for the distinction between a fixed signed-count precision and an optimized time estimator.

## CORR26

Florian Meier, Yuri Minoguchi, Gianmichele Blasi, Géraldine Haack and Marcus Huber, **Exponential gain in clock precision using quantum correlated ticks**, arXiv:2601.10785 (2026), accepted in *Physical Review X*. [Accepted article](https://journals.aps.org/prx/accepted/10.1103/ftym-1117) · [arXiv record](https://arxiv.org/abs/2601.10785).

Relevant context for clocks retaining correlations between output events. The comparison uses its non-reset architecture; it is not a full audit of that paper's proof.

## SB

**Quantum Current without Equilibration**, source account at commit `98f5365e36a8b0fc9862222b2242f867ba1232ad`: [source balance](https://github.com/GoGoKo699/Quantum-Current-without-Equilibration/blob/98f5365e36a8b0fc9862222b2242f867ba1232ad/science/source_balance.md).

The contraction/source-balance identities and bright–dark decomposition are shared ingredients. They are rederived in the precision proof so that the present account is self-contained. The fluctuation/affinity consequence is a separate statement.

## QTP

**Quantum Transport Precision**, source account at commit `eec1dd6147facc422b5ea372ba385dd96f213963`: [model](https://github.com/GoGoKo699/Quantum-Transport-Precision/blob/eec1dd6147facc422b5ea372ba385dd96f213963/science/model.md) · [size bound](https://github.com/GoGoKo699/Quantum-Transport-Precision/blob/eec1dd6147facc422b5ea372ba385dd96f213963/science/size_bound.md).

The inspected account concerns serial noninteracting fermionic transport and its size/contact resources. Its jump and retained-state structure differ from the full-reset model here.
