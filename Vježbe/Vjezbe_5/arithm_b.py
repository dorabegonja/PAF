#b)

import statistics
import math

x = []
print("Unesite 10 brojeva:")
for i in range(10):
    x.append(float(input()))

x_bar = statistics.mean(x)

n = len(x)
zbroj_kvadrata = sum((xi - x_bar)**2 for xi in x)
sigma = math.sqrt(zbroj_kvadrata / (n * (n - 1)))

print("Aritmetička sredina =", x_bar)
print("Standardna devijacija =", sigma)