import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
mase_ciste = np.random.normal(loc=2.06, scale=0.05, size=57).tolist()

def histogram(podaci, k):
    xmin = min(podaci)
    xmax = max(podaci)

    h = (xmax - xmin) / k

    rubovi = [xmin + i * h for i in range(k + 1)]

    frekvencije = [0] * k

    for x in podaci:
        if x == xmax:
            frekvencije[-1] += 1
            continue

        indeks = int((x - xmin) // h)
        frekvencije[indeks] += 1

    print("Tekstualni histogram:\n")
    for i in range(k):
        lijevi = rubovi[i]
        desni = rubovi[i+1]
        print(f"{i+1}. [{lijevi:.2f}, {desni:.2f}): {frekvencije[i]}")

    return rubovi, frekvencije


k = 10
rubovi, frekvencije = histogram(mase_ciste, k)

sredine = [(rubovi[i] + rubovi[i+1]) / 2 for i in range(k)]

plt.bar(sredine, frekvencije, width=(rubovi[1] - rubovi[0]), edgecolor='black')
plt.xlabel("Masa zvijezde (u masama Sunca)")
plt.ylabel("Frekvencija")
plt.title("Histogram masa (ručno izračunat)")
plt.show()