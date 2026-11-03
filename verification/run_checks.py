"""Reproduce finite checks of the reset-clock affinity bounds.

Analytical proofs live in science/. This suite checks independent numerical
representations, exact finite polynomial identities, and stated boundary cases.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from math import comb
from pathlib import Path
import json
import platform

import numpy as np
import scipy
from scipy.linalg import solve


SEED = 70905


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def vec(x: np.ndarray) -> np.ndarray:
    return x.reshape(-1, order="F")


def projector(a: np.ndarray) -> np.ndarray:
    return np.outer(a, a.conj())


def dissipator(jump: np.ndarray) -> np.ndarray:
    ident = np.eye(len(jump))
    q = jump.conj().T @ jump
    return np.kron(jump.conj(), jump) - (
        np.kron(ident, q) + np.kron(q.T, ident)
    ) / 2


def generators(h: np.ndarray, r: float, a: np.ndarray, b: np.ndarray,
               noise: tuple[np.ndarray, ...] = ()) -> dict:
    """Column-vectorized superoperators, with forward rate Gamma=1."""
    d = len(h)
    ident = np.eye(d)
    pa, pb = projector(a), projector(b)
    jp = np.outer(a, b.conj())
    jm = np.sqrt(r) * jp.conj().T
    q = pb + r * pa
    background = -1j * (np.kron(ident, h) - np.kron(h.T, ident))
    for jump in noise:
        background += dissipator(jump)
    l0 = background - (np.kron(ident, q) + np.kron(q.T, ident)) / 2
    gp, gm = np.kron(jp.conj(), jp), np.kron(jm.conj(), jm)
    return dict(d=d, pa=pa, pb=pb, trace=vec(ident).conj(),
                no_count=l0, full=l0 + gp + gm,
                plus=gp, minus=gm, first=gp - gm, second=gp + gm)


def cumulants(g: dict) -> dict:
    """Stationary tilted-generator derivatives, without finite differencing."""
    l, tr, d = g["full"], g["trace"], g["d"]
    constrained = l.copy()
    constrained[0, :] = tr
    rhs = np.zeros(d * d, complex)
    rhs[0] = 1
    rho = solve(constrained, rhs)
    current = float(np.real(tr @ g["first"] @ rho))
    rhs = -(g["first"] - current * np.eye(d * d)) @ rho
    rhs[0] = 0
    derivative = solve(constrained, rhs)
    variance_rate = float(np.real(tr @ (
        g["second"] @ rho + 2 * g["first"] @ derivative
    )))
    return dict(current=current, variance_rate=variance_rate,
                fano=variance_rate / current,
                stationary_residual=float(np.linalg.norm(l @ rho)),
                trace_error=float(abs(tr @ rho - 1)),
                density_min_eigenvalue=float(np.linalg.eigvalsh(
                    (rho.reshape((d, d), order="F") +
                     rho.reshape((d, d), order="F").conj().T) / 2
                ).min()))


def converse_case(h: np.ndarray, r: float, a: np.ndarray, b: np.ndarray,
                  noise: tuple[np.ndarray, ...] = (), **labels) -> dict:
    g = generators(h, r, a, b, noise)
    values = cumulants(g)
    require(values["current"] > 1e-12, "Case has no positive operating current")
    c = np.empty((2, 2))
    endpoints = (g["pa"], g["pb"])
    for j, state in enumerate(endpoints):
        integrated = solve(-g["no_count"], vec(state)).reshape(h.shape, order="F")
        for i, effect in enumerate(endpoints):
            c[i, j] = np.real(np.trace(effect @ integrated))
    a_prob = float(c[1, 0])
    bound = r * r * (1 + r) / (1 - r)
    row = dict(d=len(h), r=r, A=a_prob, A_ceiling=1 / (1 + r),
               reciprocity_error=float(abs(c[0, 1] - c[1, 0])),
               endpoint_min_eigenvalue=float(np.linalg.eigvalsh((c + c.T) / 2).min()),
               fano_bound=bound, fano_to_bound=values["fano"] / bound,
               endpoint_overlap=float(abs(np.vdot(a, b))), **values, **labels)
    require(a_prob <= 1 / (1 + r) + 1e-8, "Endpoint transfer ceiling failed")
    require(row["reciprocity_error"] < 1e-7, "Integrated reciprocity failed")
    require(row["endpoint_min_eigenvalue"] >= -1e-8, "Endpoint PSD failed")
    require(row["fano_to_bound"] >= 1 - 1e-7, "Precision bound failed")
    require(row["stationary_residual"] < 1e-8, "Stationary solve residual")
    require(row["density_min_eigenvalue"] >= -1e-8, "Stationary positivity")
    return row


def random_converse_cases() -> list[dict]:
    rng = np.random.default_rng(SEED)
    rows = []
    for d in (2, 3, 4, 6, 8):
        a, b = np.eye(d)[:, 0], np.eye(d)[:, -1]
        for r in (.01, .1, .5, .9):
            for real in (True, False):
                for _ in range(4):
                    z = rng.normal(size=(d, d))
                    if not real:
                        z = z + 1j * rng.normal(size=(d, d))
                    h = (z + z.conj().T) / (2 * np.sqrt(d))
                    h *= 10 ** rng.uniform(-1, 1)
                    rows.append(converse_case(h, r, a, b, family="random_H", real_H=real))
    for d in (3, 5, 9):
        a, b = np.eye(d)[:, 0], np.eye(d)[:, -1]
        couplings = np.sqrt(np.arange(1, d) * (d - np.arange(1, d))) / d
        h = np.diag(couplings, 1) + np.diag(couplings, -1)
        for r in (.01, .1, .5):
            rows.append(converse_case(h, r, a, b, family="perfect_transfer_chain"))
    for d in (2, 4):
        for r in (.1, .8):
            for _ in range(4):
                a = rng.normal(size=d) + 1j * rng.normal(size=d)
                b = rng.normal(size=d) + 1j * rng.normal(size=d)
                a, b = a / np.linalg.norm(a), b / np.linalg.norm(b)
                z = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
                h = (z + z.conj().T) / (2 * np.sqrt(d))
                rows.append(converse_case(h, r, a, b, family="nonorthogonal_ports"))
    for d in (3, 5):
        a, b = np.eye(d)[:, 0], np.eye(d)[:, -1]
        for r in (.2, .7):
            for gamma in (.1, 2.):
                z = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
                h = (z + z.conj().T) / (2 * np.sqrt(d))
                noise = (np.sqrt(gamma) * np.diag(np.linspace(-1, 1, d)),)
                rows.append(converse_case(h, r, a, b, noise, family="unital_dephasing"))
    for r in (.1, .8):
        row = converse_case(np.zeros((1, 1)), r, np.ones(1), np.ones(1),
                            family="labeled_Poisson_boundary")
        require(abs(row["fano"] - (1 + r) / (1 - r)) < 1e-10, "Poisson boundary")
        rows.append(row)
    return rows


def polynomial_add(a, b):
    c = [Fraction(0)] * max(len(a), len(b))
    for i, x in enumerate(a):
        c[i] += x
    for i, x in enumerate(b):
        c[i] += x
    return c


def exact_characteristic_checks() -> list[int]:
    """Check the tridiagonal determinant recurrence with exact rationals."""
    checked = []
    for d in range(2, 31):
        q0, q1 = [Fraction(1)], [Fraction(0), Fraction(1)]
        for k in range(2, d):
            j = k - 1
            g2 = Fraction(j * (2 * d - j), (2 * d - 2 * j - 1) * (2 * d - 2 * j + 1))
            q0, q1 = q1, polynomial_add([Fraction(0)] + q1, [g2 * x for x in q0])
        j = d - 1
        g2 = Fraction(j * (2 * d - j), (2 * d - 2 * j - 1) * (2 * d - 2 * j + 1))
        p = polynomial_add(polynomial_add([Fraction(0)] + q1, [d * x for x in q1]),
                           [g2 * x for x in q0])
        require(p == [Fraction(comb(d, k)) for k in range(d + 1)], f"EP recurrence at d={d}")
        checked.append(d)
    return checked


def ep_hamiltonian(d: int) -> np.ndarray:
    j = np.arange(1, d, dtype=float)
    couplings = np.sqrt(j * (2 * d - j) /
                        (4 * d * d * (2 * d - 2 * j - 1) * (2 * d - 2 * j + 1)))
    return np.diag(couplings, 1) + np.diag(couplings, -1)


def block_moments(g: dict) -> dict:
    """Kill only at positive ticks; keep negative jumps inside each block."""
    killed = g["full"] - g["plus"]
    resolvent = lambda x: solve(-killed, x)
    tr, rho, jm = g["trace"], vec(g["pa"]), g["minus"]
    r1 = resolvent(rho)
    r2 = resolvent(r1)
    mu = float(np.real(tr @ r1))
    v = float(2 * np.real(tr @ r2))
    m = float(np.real(tr @ jm @ r1))
    factorial = float(2 * np.real(tr @ jm @ resolvent(jm @ r1)))
    mixed = float(np.real(tr @ (resolvent(jm @ r1) + jm @ r2)))
    fano = (1 - m) * v / mu**2 - 1 + 2 * mixed / mu + factorial / (1 - m)
    return dict(mean_time=mu, second_time=v, expected_negative_ticks=m,
                factorial_negative_moment=factorial, mixed_time_count=mixed,
                current=(1 - m) / mu, fano=fano, precision=1 / fano)


def construction_checks() -> list[dict]:
    rows = []
    for d in (2, 3, 4, 5, 8, 12):
        h = ep_hamiltonian(d)
        a, b = np.eye(d)[:, 0], np.eye(d)[:, -1]
        require(np.linalg.norm(h, 2) <= 1 / np.sqrt(3), "Hamiltonian strength")
        for r in (0., 1 / (65536 * d**3)):
            g = generators(h, r, a, b)
            block = block_moments(g)
            tilt = cumulants(g)
            err = abs(block["fano"] - tilt["fano"])
            require(err < 1e-7, f"Independent Fano calculations at d={d}")
            require(abs(block["current"] - tilt["current"]) < 1e-9, "Independent current")
            if r == 0:
                require(abs(block["mean_time"] / (d * (2 * d - 1)) - 1) < 1e-8, "Erlang mean")
                require(abs(block["fano"] * (2 * d - 1) - 1) < 1e-7, "Erlang Fano")
            else:
                require(block["precision"] >= d, "Finite-bias construction precision")
                require(block["fano"] <= 1 / (2 * d - 1) + 8000 * r * d**2,
                        "Finite-bias perturbation envelope")
                require(1 / (6 * d**2) <= block["current"] <= 4 / (3 * d**2), "Tick rate bounds")
            rows.append(dict(d=d, r=r, h_norm=float(np.linalg.norm(h, 2)),
                             tilted_fano=tilt["fano"], fano_method_error=err, **block))
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("results.json"))
    args = parser.parse_args()
    rows = random_converse_cases()
    exact = exact_characteristic_checks()
    construction = construction_checks()
    summary = dict(
        converse_cases=len(rows),
        max_absorption_excess=max(x["A"] - x["A_ceiling"] for x in rows),
        max_reciprocity_error=max(x["reciprocity_error"] for x in rows),
        min_endpoint_eigenvalue=min(x["endpoint_min_eigenvalue"] for x in rows),
        min_fano_to_bound=min(x["fano_to_bound"] for x in rows),
        max_stationary_residual=max(x["stationary_residual"] for x in rows),
        exact_characteristic_dimensions=exact,
        construction_cases=len(construction),
        max_fano_method_error=max(x["fano_method_error"] for x in construction),
        min_finite_bias_precision_per_dimension=min(x["precision"] / x["d"]
                                                   for x in construction if x["r"] > 0),
    )
    result = dict(status="passed", seed=SEED,
                  environment=dict(python=platform.python_version(), numpy=np.__version__, scipy=scipy.__version__),
                  summary=summary, converse_cases=rows, construction_cases=construction)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
