import numpy as np
import matplotlib.pyplot as plt

h0 = 0.54
m = 0.5257
r = 4.025e-3
g = 9.81
h_list = [0.14 , 0.17 , 0.19 , 0.22 , 0.25 , 0.28 , 0.31 , 0.34 , 0.37 , 0.40] # m
t_mean_list = [1.740 , 1.793 , 2.043 , 2.190 , 2.280 , 2.417 , 2.540 , 2.640 , 2.670 , 2.813] # s

n = len(h_list)

#a) log-log regresija

x_list = []
y_list = []

for i in range(n):
    x_list.append(np.log(t_mean_list[i]))
    y_list.append(np.log(h_list[i]))

x = np.array(x_list)
y = np.array(y_list)

Sx = np.sum(x)
Sy = np.sum(y)
Sxx = np.sum(x**2)
Sxy = np.sum(x*y)

a = (n*Sxy - Sx*Sy) / (n*Sxx - Sx**2)
b = (Sy - a*Sx) / n

sigma2 = np.sum((y - (a*x + b))**2) / (n - 2)
sigma_a = np.sqrt(n * sigma2 / (n*Sxx - Sx**2))
sigma_b = np.sqrt(sigma2 * Sxx / (n*Sxx - Sx**2))

print("\na)")
print(f"a = ({np.round(a, 1)} ± {np.round(sigma_a, 1)})")
print(f"b = ({np.round(b, 2)} ± {np.round(sigma_b, 2)})")

x_fit = np.linspace(min(x), max(x), 1000)
y_fit = a*x_fit + b

plt.figure()
plt.scatter(x, y, color="red", label="Eksperimentalni podaci")
plt.plot(x_fit, y_fit, color="blue", label=f"y = {np.round(a,1)}x + {np.round(b,2)}")
plt.xlabel("log(t)")
plt.ylabel("log(h)")
plt.title("Linearna regresija: log(h) - log(t)")
plt.grid(True)
plt.legend()
plt.show()

#b) regresija h - t^2 (kroz ishodište)

x2_list = []
y2_list = []

for i in range(n):
    x2_list.append(t_mean_list[i]**2)
    y2_list.append(h_list[i])

x2 = np.array(x2_list)
y2 = np.array(y2_list)

a2 = np.sum(x2*y2) / np.sum(x2**2)
sigma_a2 = np.sqrt((1/n) * (np.sum(y2**2)/np.sum(x2**2) - a2**2))

print("\nb)")
print(f"a = ({np.round(a2, 3)} ± {np.round(sigma_a2, 3)}) m/s²")

x2_fit = np.linspace(min(x2), max(x2), 1000)
y2_fit = a2 * x2_fit

plt.figure()
plt.scatter(x2, y2, color="red", label="Eksperimentalni podaci")
plt.plot(x2_fit, y2_fit, color="blue", label=f"h = {np.round(a2,3)} t²")
plt.xlabel("t² [s²]")
plt.ylabel("h [m]")
plt.title("Linearna regresija: h - t²")
plt.grid(True)
plt.legend()
plt.show()

a_eff = 2 * a2
sigma_a_eff = 2 * sigma_a2

I_z = (m * g * r**2) / a_eff - m * r**2
sigma_I_z = (m * g * r**2 / a_eff**2) * sigma_a_eff

print("\nc)")
print(f"Iz = ({np.round(I_z*1e4, 1)} ± {np.round(sigma_I_z*1e4, 1)}) × 10⁻⁴ kgm²\n")