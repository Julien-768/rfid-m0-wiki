"""Module providing Inductance of single-layer coils."""

# Modified from
# http://electronbunker.ca/eb/CalcMethods1a.html

import math

#################################################
# Input
#################################################

# Mean radius in mm
RADIUS_IN_MM = 105 / 2

# Wire diameter in mm (external) OR constant coil length in mm
WIRE_DIAMETER = 0.23
CONSTANT_COIL_LENGTH = True
COIL_LENGHT_CONSTANT = 4


# Target inductance of the coil
TARGET_INDUCTANCE_UH = 192

#################################################

RADIUS = RADIUS_IN_MM / 1000

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


def nagaoka(u):
    # returns Nagaoka's coefficient,
    # aka: field non-uniformity coefficient
    # where u=diameter/length
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
        co = c + 1

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

    return 1 / (3 * math.pi) * (m2 / uu * (KmE) + m2 * E - 4 * u)


DIAMETER = 2 * RADIUS
SPIRE_LENGTH = DIAMETER * math.pi

Ls = 0
COIL_LENGTH = 0
ITERATION = 0

while Ls <= TARGET_INDUCTANCE_UH and ITERATION < 20000:
    ITERATION += 1

    # Increment length of the wire
    WIRE_LENGTH = SPIRE_LENGTH * ITERATION

    # Compute updated coil characteristics
    NB_SPIRES = math.ceil(WIRE_LENGTH / math.pi / DIAMETER)
    if CONSTANT_COIL_LENGTH:
        COIL_LENGTH = COIL_LENGHT_CONSTANT / 1000
    else:
        COIL_LENGTH = WIRE_DIAMETER * NB_SPIRES / 1000

    k = nagaoka(DIAMETER / COIL_LENGTH)

    # Inductor in µHenries
    Ls_previous = Ls
    Ls = 4 * math.pi**2 * NB_SPIRES**2 * RADIUS**2 * k / COIL_LENGTH / 10

    Inductance_by_spire = Ls - Ls_previous

    # Check if the inductance has crossed the target
    if Ls + Inductance_by_spire > TARGET_INDUCTANCE_UH:
        break

if ITERATION != 2000:
    print(f"|- Radius is \t\t\t{RADIUS_IN_MM:.2f} mm")
    print(f"|- Wire diameter is \t\t{WIRE_DIAMETER:.2f} mm")
    if CONSTANT_COIL_LENGTH:
        print(f"|- Coil lenght is constraint at {COIL_LENGTH * 1000 :.2f} mm")
    print(f"|- Target inductance is \t{TARGET_INDUCTANCE_UH:.0f} µH")
    print(f"{ITERATION} iterations realized :")
    print(f"|- Nagaoka coefficient is \t{k}")
    print(f"|- Number of spires is\t \t{NB_SPIRES:.0f}")
    print(f"|- Inductance is\t\t \t{Ls:.2f} µH")
    print(f"|- Wire length is\t \t{WIRE_LENGTH:.2f} m")
    if CONSTANT_COIL_LENGTH:
        print(f"|- Ideal coil lenght would be \t{WIRE_DIAMETER * NB_SPIRES :.2f} mm")
    else:
        print(f"|- Coil lenght is\t \t{COIL_LENGTH * 1000 :.2f} mm")
    print(f"|- One turn would add\t \t{Inductance_by_spire:.2f} µH")
else:
    print("No result found")
