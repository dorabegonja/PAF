#Tablica gustoće materijala s interneta

rho1 = 8.86
srho1 = 0.07

rho2 = 7.84
srho2 = 0.02

rho3 = 2.65
srho3 = 0.01 

#Tablične gustoće (g/cm^3)
aluminij = 2.70
celik = 7.85
bakar = 8.96

#Relativne pogreške
rel1 = srho1 / rho1
rel2 = srho2 / rho2
rel3 = srho3 / rho3


def najblizi(rho):
    razlike = {
        "aluminij": abs(rho - aluminij),
        "čelik": abs(rho - celik),
        "bakar": abs(rho - bakar)
    }
    return min(razlike, key=razlike.get)

mat1 = najblizi(rho1)
mat2 = najblizi(rho2)
mat3 = najblizi(rho3)


print("Valjak 1:")
print("rho =", rho1, "sigma =", srho1, "rel =", rel1)
print("materijal =", mat1)
print()

print("Valjak 2:")
print("rho =", rho2, "sigma =", srho2, "rel =", rel2)
print("materijal =", mat2)
print()

print("Valjak 3:")
print("rho =", rho3, "sigma =", srho3, "rel =", rel3)
print("materijal =", mat3)