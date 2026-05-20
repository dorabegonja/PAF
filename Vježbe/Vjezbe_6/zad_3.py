import math

#Vrijednosti izrečunate u prvom i drugom zadatku
#Valjak 1
M1 = 138.984
sM1 = 0.0556
V1 = 15.68
sV1 = 0.12

#Valjak 2
M2 = 128.55
sM2 = 0.0570
V2 = 16.39
sV2 = 0.05

#Valjak 3
M3 = 71.826
sM3 = 0.0369
V3 = 27.10
sV3 = 0.07


def gustoca(m, V):
    return m / V

def sigma_gustoca(m, sm, V, sV):
    dRdm = 1 / V
    dRdV = -m / (V**2)
    return math.sqrt((dRdm * sm)**2 + (dRdV * sV)**2)


rho1 = gustoca(M1, V1)
srho1 = sigma_gustoca(M1, sM1, V1, sV1)

rho2 = gustoca(M2, V2)
srho2 = sigma_gustoca(M2, sM2, V2, sV2)

rho3 = gustoca(M3, V3)
srho3 = sigma_gustoca(M3, sM3, V3, sV3)


print("Valjak 1:", rho1, "g/cm^3", "sigma =", srho1)
print("Valjak 2:", rho2, "g/cm^3", "sigma =", srho2)
print("Valjak 3:", rho3, "g/cm^3", "sigma =", srho3)