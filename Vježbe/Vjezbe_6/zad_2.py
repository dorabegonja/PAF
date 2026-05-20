import math

def aritm_sredina(x):
    return sum(x) / len(x)

def sigma(x):
    m = aritm_sredina(x)
    s = 0
    for a in x:
        s += (a - m)**2
    return math.sqrt(s / (len(x) * (len(x) - 1)))

d1 = [19.98, 20.18, 20.10, 20.08, 19.74]
d2 = [19.92, 19.82, 19.96, 19.98, 19.88]
d3 = [24.96, 24.98, 24.98, 24.92, 24.94]

l1 = [49.80, 49.00, 50.48, 49.80, 49.96]
l2 = [52.56, 52.50, 52.62, 52.58, 52.54]
l3 = [55.34, 55.40, 55.30, 55.44, 55.48]

m1 = [138.92, 138.98, 139.20, 138.90, 138.92]
m2 = [128.65, 128.60, 128.65, 128.35, 128.50]
m3 = [71.89, 71.90, 71.79, 71.85, 71.70]


#Izracunamo R, L i sigme (kao u zad 1)
#Valjak 1
D1 = aritm_sredina(d1)
sD1 = sigma(d1)
R1 = D1 / 2
sR1 = sD1 / 2

L1 = aritm_sredina(l1)
sL1 = sigma(l1)

#Valjak 2
D2 = aritm_sredina(d2)
sD2 = sigma(d2)
R2 = D2 / 2
sR2 = sD2 / 2

L2 = aritm_sredina(l2)
sL2 = sigma(l2)

#Valjak 3
D3 = aritm_sredina(d3)
sD3 = sigma(d3)
R3 = D3 / 2
sR3 = sD3 / 2

L3 = aritm_sredina(l3)
sL3 = sigma(l3)


def volumen_valjka(R, L):
    return math.pi * R**2 * L

def sigma_volumena(R, sR, L, sL):
    dVdR = 2 * math.pi * R * L
    dVdL = math.pi * R**2
    return math.sqrt((dVdR * sR)**2 + (dVdL * sL)**2)


#mm u cm (jer su mjerenja u mm)
R1c = R1 / 10
sR1c = sR1 / 10
L1c = L1 / 10
sL1c = sL1 / 10

R2c = R2 / 10
sR2c = sR2 / 10
L2c = L2 / 10
sL2c = sL2 / 10

R3c = R3 / 10
sR3c = sR3 / 10
L3c = L3 / 10
sL3c = sL3 / 10


V1 = volumen_valjka(R1c, L1c)
sV1 = sigma_volumena(R1c, sR1c, L1c, sL1c)

V2 = volumen_valjka(R2c, L2c)
sV2 = sigma_volumena(R2c, sR2c, L2c, sL2c)

V3 = volumen_valjka(R3c, L3c)
sV3 = sigma_volumena(R3c, sR3c, L3c, sL3c)


print("Valjak 1:")
print("V =", "{:.3e}".format(V1), "cm^3", "  sigma_V =", "{:.3e}".format(sV1), "cm^3")
print()

print("Valjak 2:")
print("V =", "{:.3e}".format(V2), "cm^3", "  sigma_V =", "{:.3e}".format(sV2), "cm^3")
print()

print("Valjak 3:")
print("V =", "{:.3e}".format(V3), "cm^3", "  sigma_V =", "{:.3e}".format(sV3), "cm^3")