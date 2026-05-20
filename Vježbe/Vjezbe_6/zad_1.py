import math

#Funkcije iz vježbe 5
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

#Valjak 1
D1 = aritm_sredina(d1)
sD1 = sigma(d1)
R1 = D1 / 2
sR1 = sD1 / 2

L1 = aritm_sredina(l1)
sL1 = sigma(l1)

M1 = aritm_sredina(m1)
sM1 = sigma(m1)

print("Valjak 1:")
print("R =", R1, "+-", sR1)
print("L =", L1, "+-", sL1)
print("m =", M1, "+-", sM1)
print()

#Valjak 2
D2 = aritm_sredina(d2)
sD2 = sigma(d2)
R2 = D2 / 2
sR2 = sD2 / 2

L2 = aritm_sredina(l2)
sL2 = sigma(l2)

M2 = aritm_sredina(m2)
sM2 = sigma(m2)

print("Valjak 2:")
print("R =", R2, "+-", sR2)
print("L =", L2, "+-", sL2)
print("m =", M2, "+-", sM2)
print()

#Valjak 3
D3 = aritm_sredina(d3)
sD3 = sigma(d3)
R3 = D3 / 2
sR3 = sD3 / 2

L3 = aritm_sredina(l3)
sL3 = sigma(l3)

M3 = aritm_sredina(m3)
sM3 = sigma(m3)

print("Valjak 3:")
print("R =", R3, "+-", sR3)
print("L =", L3, "+-", sL3)
print("m =", M3, "+-", sM3)