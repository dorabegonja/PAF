x = []
print("Unesite 10 brojeva:")
for i in range(10):
    x.append(float(input()))

n = len(x)
x_bar = sum(x) / n

zbroj_kvadrata = sum((xi - x_bar)**2 for xi in x)
sigma = (zbroj_kvadrata / (n * (n - 1)))**0.5

print("Aritmetička sredina =", x_bar)
print("Standardna devijacija =", sigma)