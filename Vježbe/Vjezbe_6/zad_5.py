import numpy as np
import math

malo_n = [99.8, 100.1, 99.9, 100.2, 100.0]

np.random.seed(42)
veliko_n = np.random.normal(loc=100.0, scale=0.2, size=10000).tolist()


def sigma_n(x):
    xbar = sum(x) / len(x)
    s = sum((a - xbar)**2 for a in x)
    return math.sqrt(s / len(x))

def s_std(x):
    xbar = sum(x) / len(x)
    s = sum((a - xbar)**2 for a in x)
    return math.sqrt(s / (len(x) - 1))

def sigma_xbar(x):
    return s_std(x) / math.sqrt(len(x))


#Mali skup
sigma_n_m = sigma_n(malo_n)
s_m = s_std(malo_n)
sigma_xbar_m = sigma_xbar(malo_n)

#Veliki skup
sigma_n_v = sigma_n(veliko_n)
s_v = s_std(veliko_n)
sigma_xbar_v = sigma_xbar(veliko_n)


rel_m = abs(sigma_n_m - s_m) / s_m
rel_v = abs(sigma_n_v - s_v) / s_v


print("MALI SKUP (n = 5)")
print("sigma_n =", sigma_n_m)
print("s =", s_m)
print("sigma_xbar =", sigma_xbar_m)
print("relativna razlika sigma_n i s =", rel_m)
print()

print("VELIKI SKUP (n = 10000)")
print("sigma_n =", sigma_n_v)
print("s =", s_v)
print("sigma_xbar =", sigma_xbar_v)
print("relativna razlika sigma_n i s =", rel_v)
print()