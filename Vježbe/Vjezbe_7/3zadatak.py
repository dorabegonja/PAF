import numpy as np

def medijan(podaci):
    p = sorted(podaci)
    n = len(p)
    
    if n % 2 == 1:
        indeks = n // 2
        return p[indeks]
    else:
        i1 = n // 2 - 1
        i2 = n // 2
        return (p[i1] + p[i2]) / 2

a = [3, 1, 4, 1, 5, 9, 2, 6]      # paran n = 8
b = [3, 1, 4, 1, 5, 9, 2, 6, 5]   # neparan n = 9

print("Medijan(a) =", medijan(a))
print("Medijan(b) =", medijan(b))


print("numpy.median(a) =", np.median(a))
print("numpy.median(b) =", np.median(b))


np.random.seed(42)
mase_ciste = np.random.normal(loc=2.06, scale=0.05, size=57).tolist()
mase = mase_ciste + [6.0, 1.2, 3.2, 4.5, 8.5, 7.8, 0.08, 0.02]

print("\nMedijan(mase) =", medijan(mase))
print("numpy.median(mase) =", np.median(mase))