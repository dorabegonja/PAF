import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
mase_ciste = np.random.normal(loc=2.06, scale=0.05, size=57).tolist()

k = 10

plt.hist(mase_ciste, bins=k, edgecolor='black')
plt.xlabel("Masa zvijezde (u masama Sunca)")
plt.ylabel("Frekvencija")
plt.title("Histogram masa (plt.hist)")

sredina = np.mean(mase_ciste)
medijan = np.median(mase_ciste)

plt.axvline(sredina, color='red', linestyle='--', label=f"Sredina = {sredina:.3f}")
plt.axvline(medijan, color='green', linestyle='--', label=f"Medijan = {medijan:.3f}")

plt.legend()
plt.show()

counts, edges = np.histogram(mase_ciste, bins=k)

print("\nFrekvencije iz plt.hist:")
for i in range(k):
    print(f"{i+1}. [{edges[i]:.2f}, {edges[i+1]:.2f}): {counts[i]}")