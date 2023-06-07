"""Module providing Inductance of single-layer coils."""

# All credits go to
# http://electronbunker.ca/eb/CalcMethods1a.html

import math

#################################################
# Input
#################################################

# Mean radius in m
RADIUS = 36 / 2 / 1000

# Wire diameter (external)
WIRE_DIAMETER = 0.2

# Target inductance of the coil
TARGER_INDUCTANCE_UH = 192

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

def nagaoka(u):
# returns Nagaoka's coefficient,
# aka: field non-uniformity coefficient
# where u=diameter/length
    if (u==0):
        return 1
    else:
        uu = u * u                # (diameter/length)²
        m = uu / (1 + uu)         # square of modulus
        m2 = 4 * math.sqrt(1 + uu)
        a = 1                       # arithmetic mean
        b = math.sqrt(1 - m)        # geometric mean
        c = a - b
        ci = 1
        cs = c * c / 2 + m
        co = c + 1
        
        while (c < co) :
            ao = (a + b) / 2
            b = math.sqrt(a * b)
            a = ao
            co = c
            c = a - b
            cs = cs + ci * c * c  # Sum for n = 0 to infinity of (2^n * c²)
            ci = 2 * ci

        cs = cs / 2
        K = math.pi / (a + a)   # elliptic integral K = pi/(2a)
        KmE = K * cs            # K - E
        E = K * (1 - cs)        # elliptic integral E

    return(1/(3*math.pi)*(m2/uu*(KmE)+m2*E-4*u))

Ls = 0
iterationNumber = 0
WIRE_LENGTH = 0
NB_SPIRES = 0
COIL_LENGHT = 0
DIAMETER = 2 * RADIUS

while ((Ls < TARGER_INDUCTANCE_UH ) and iterationNumber < 20000):
    
    # Increment length of the wire
    WIRE_LENGTH = WIRE_LENGTH + 0.001
    
    # Compute updated coil characteristics
    NB_SPIRES = WIRE_LENGTH / math.pi / DIAMETER
    # Length / thickness in m
    COIL_LENGHT = WIRE_DIAMETER * math.ceil(NB_SPIRES) / 1000
    
    k = nagaoka(DIAMETER / COIL_LENGHT)
    # Inductor in µHenries
    Ls = 4 * pow(math.pi, 2) * pow(NB_SPIRES, 2) * pow(RADIUS, 2) * k / COIL_LENGHT /10
    
    iterationNumber = iterationNumber + 1

if iterationNumber != 20000:
    print(f'{iterationNumber} iterations realized :')
    print(f'|- Nagaoka coefficient is {k}')
    print(f'|- Inductor is {Ls} µH')
    print(f'|- Wire length is {WIRE_LENGTH} m')
    print(f'|- Nb spires is {NB_SPIRES}')
    print(f'|- Coil length is {COIL_LENGHT * 1000} mm')
else:
    print('No result found')