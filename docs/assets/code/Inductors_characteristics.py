"""Module providing Inductance of single-layer coils."""

# All credits go to
# http://electronbunker.ca/eb/CalcMethods1a.html

import math

#################################################
# Input
#################################################

# mean radius in m
RADIUS = 0.5 * 105e-3

# Length / thickness in m
COIL_LENGHT = 4e-3

# number of spires
NB_SPIRES = 26

#################################################

# Nagaoka's formula: Ls = k*(2*pi*N*r)²/l
# Ls is inductance of the coil in H
# N is the number of turns
# r is the radius of the coil in m
# l is the length / thickness of the coil in m
# k is Nagaoka's coefficient, computed from diameter/length

# returns: Nagaoka's coefficient, aka: field non-uniformity coefficient
# parameter: u = diameter/length
# comments: this function uses the arithmetic-geometric mean method to compute
# the 2 elliptic integrals K and E in Nagoaka's formula and thus determine
# Nagoaka's coefficient

DIAMETER = 2 * RADIUS


def nagaoka(u):
    if u == 0:
        return 1
    else:
        uu = u * u  # (diameter/length)²
        m = uu / (1 + uu)  # square of modulus
        m2 = 4 * math.sqrt(1 + uu)
        a = 1  # arithmetic mean
        b = math.sqrt(1 - m)  # geometric mean
        c = a - b
        ci = 1
        cs = c * c / 2 + m
        co = c

        while c < co:
            ao = (a + b) / 2
            b = math.sqrt(a * b)
            a = ao
            co = c
            c = a - b
            cs = cs + ci * c * c  # Sum for n = 0 to infinity of (2^n * c²)
            ci = 2 * ci

        cs = cs / 2
        K = math.pi / (a + a)  # elliptic integral K = pi/(2a)
        KmE = K * cs  # K - E
        E = K * (1 - cs)  # elliptic integral E

        return (m2 / uu * (KmE) + m2 * E - 4 * u) / (3 * math.pi)


k = nagaoka(DIAMETER / COIL_LENGHT)
# Inductor in µHenries
Ls = (
    k
    * 4
    * pow(math.pi, 2)
    / 10000000
    * pow(RADIUS, 2)
    * pow(NB_SPIRES, 2)
    / COIL_LENGHT
    * 1000000
)  # µ0 = 4π×10-7

print(f"Nagaoka coefficient is {k}")
print(f"inductor is {Ls} µH")

wire_length = NB_SPIRES * DIAMETER * math.pi

print(f"Wire length is {wire_length} m")
