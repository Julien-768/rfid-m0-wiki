"""Module providing complete elliptic integrals."""

import math


def complete_elliptic_integrals(u):
    """Calculate the complete elliptic integrals used by Nagaoka's formula.

    The arithmetic-geometric mean (AGM) method is used.

    Args:
        u (float): Diameter/length ratio.

    Returns:
        tuple[float, float, float, float]:
            m2, K, K-E, and E.
    """
    if u == 0:
        return 4, math.pi / 2, 0, math.pi / 2

    uu = u * u
    m = uu / (1 + uu)
    m2 = 4 * math.sqrt(1 + uu)

    a = 1
    b = math.sqrt(1 - m)
    c = a - b
    ci = 1
    cs = c * c / 2 + m
    co = c + 1

    while c < co:
        ao = (a + b) / 2
        b = math.sqrt(a * b)
        a = ao
        co = c
        c = a - b
        cs += ci * c * c
        ci *= 2

    cs /= 2
    k = math.pi / (a + a)
    km_e = k * cs
    e = k * (1 - cs)

    return m2, k, km_e, e
