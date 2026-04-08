import math
import matplotlib.pyplot as plt
import numpy as np
from calculus import derivacija_tocka as dt
from calculus import derivacija_interval as di

def kubna(x):
    return x**3
def trig(x):
    return np.sin(x)

def analiticko_kubna(x):
    return 3*x**2
def analiticko_sinus(x):
    return np.cos(x)

d_granicasinus=-6
g_granicasinus=6

d_granicakosinus=-3
g_granicakosinus=3

epsiloni=[0.5, 0.1, 0.0001]

plt.subplot(1, 2, 1)
xs=np.linspace(d_granicasinus, g_granicasinus, 400)
plt.plot(xs, analiticko_sinus(xs), linewidth=1, color="blue", label="Analitička derivacija")
for epsilon in epsiloni:
    tockes, derivacijes = di(trig, d_granicasinus, g_granicasinus, epsilon)
    plt.scatter(tockes, derivacijes, label=f"ε={epsilon}")
plt.title("Derivacija sin(x) ")
plt.grid()
plt.legend()
    
plt.subplot(1, 2, 2)
xk = np.linspace(d_granicakosinus, g_granicakosinus, 400)
plt.plot(xk, analiticko_kubna(xk), linewidth=1, color="red", label="Analitička derivacija")
for epsilon in epsiloni:
    tockek, derivacijek = di(kubna, d_granicakosinus, g_granicakosinus, epsilon)
    plt.scatter(tockek, derivacijek, label=f"ε={epsilon}")
plt.title("Derivacija x^3")
plt.grid()
plt.legend()
plt.show()
