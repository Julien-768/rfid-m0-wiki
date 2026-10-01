"""Module providing Inductance of single-layer coils."""

# All credits go to
# http://electronbunker.ca/eb/CalcMethods1a.html

import math

from elliptic_integral import complete_elliptic_integrals

#################################################
# Input
#################################################

# mean radius in m
RADIUS = 0.5 * 105e-3

# Length / thickness in m
COIL_LENGTH = 4e-3

# number of spires
NB_SPIRES = 26

#################################################

# Nagaoka's formula: Ls = k*(2*pi*N*r)²/l
# Ls is inductance of the coil in H
# N is the number of turns
# r is the radius of the coil in m
# l is the length / thickness of the coil in m
# k is Nagaoka's coefficient, computed from diameter/length

DIAMETER = 2 * RADIUS


def nagaoka(u):
    """Calculate Nagaoka's coefficient for coil inductance calculation.

    Args:
        u (float): Diameter/length ratio.

    Returns:
        float: Nagaoka's coefficient.
    """
    if u == 0:
        return 1

    m2, _, km_e, e = complete_elliptic_integrals(u)

    return (m2 / (u * u) * km_e + m2 * e - 4 * u) / (3 * math.pi)


k = nagaoka(DIAMETER / COIL_LENGTH)

# Inductor in µHenries
Ls = (
    k * 4 * pow(math.pi, 2) / 10000000 * pow(RADIUS, 2) * pow(NB_SPIRES, 2) / COIL_LENGTH * 1000000
)  # µ0 = 4π×10-7

print(f"Nagaoka coefficient is {k}")
print(f"inductor is {Ls} µH")

wire_length = NB_SPIRES * DIAMETER * math.pi

print(f"Wire length is {wire_length} m")
