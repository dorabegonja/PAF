import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
mase_ciste = np.random.normal(loc=2.06, scale=0.05, size=57).tolist()
mase = mase_ciste + [6.0, 1.2, 3.2, 4.5, 8.5, 7.8, 0.08, 0.02]


def medijan(podaci):
    p = sorted(podaci)
    n = len(p)
    if n % 2 == 1:
        return p[n // 2]
    else:
        return (p[n//2 - 1] + p[n//2]) / 2

sredina1 = np.mean(mase)
medijan1 = medijan(mase)

print("Sredina (sa outlierima) =", sredina1)
print("Medijan (sa outlierima) =", medijan1)

mase_bez = [x for x in mase if 1.8 < x < 2.3]


sredina2 = np.mean(mase_bez)
medijan2 = medijan(mase_bez)

print("\nSredina (bez outliera) =", sredina2)
print("Medijan (bez outliera) =", medijan2)

print("\nPromjena sredine =", abs(sredina2 - sredina1))
print("Promjena medijana =", abs(medijan2 - medijan1))

plt.hist(mase, bins=15, edgecolor='black')
plt.xlabel("Masa zvijezde")
plt.ylabel("Frekvencija")
plt.title("Histogram svih mjerenja (sa i bez outliera)")

plt.axvline(sredina1, color='red', linestyle='--', label=f"Sredina (sa) = {sredina1:.2f}")
plt.axvline(medijan1, color='green', linestyle='--', label=f"Medijan (sa) = {medijan1:.2f}")
plt.axvline(sredina2, color='orange', linestyle='-', label=f"Sredina (bez) = {sredina2:.2f}")
plt.axvline(medijan2, color='blue', linestyle='-', label=f"Medijan (bez) = {medijan2:.2f}")

plt.legend()
plt.show()