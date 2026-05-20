import numpy as np

malo_n = [99.8, 100.1, 99.9, 100.2, 100.0]

np.random.seed(42)
veliko_n = np.random.normal(loc=100.0, scale=0.2, size=10000).tolist()

def s(x):
    x = np.array(x)
    return np.sqrt(np.sum((x - x.mean())**2) / (len(x) - 1))

def sigma_x(x):
    return s(x) / np.sqrt(len(x))

def sigma_n(x):
    x = np.array(x)
    return np.sqrt(np.sum((x - x.mean())**2) / len(x))

print("a)")
print("Mali skup:")
print("s =", s(malo_n))
print("sigma_x =", sigma_x(malo_n))

print("\nVeliki skup:")
print("s =", s(veliko_n))
print("sigma_x =", sigma_x(veliko_n))

print("\nb)")
print(f"Mali skup: {abs(sigma_n(malo_n) - s(malo_n)) / s(malo_n) * 100} %")
print(f"Veliki skup: {abs(sigma_n(veliko_n) - s(veliko_n)) / s(veliko_n) * 100} %")

print("\nc)")
print("Mali skup:", np.std(malo_n))
print("Veliki skup:", np.std(veliko_n))