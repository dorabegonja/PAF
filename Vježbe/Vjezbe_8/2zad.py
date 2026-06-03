import numpy as np
import matplotlib.pyplot as plt

g = 9.81

kut_deg = np.array([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85])
kut_rad = np.radians(kut_deg)

T_120 = np.array([0.8020, 0.8187, 0.8327, 0.8660, 0.8980, 0.9153, 0.9293, 0.9653,
                  0.9747, 1.0200, 1.0373, 1.1160, 1.1780, 1.2733, 1.4180, 1.6373,
                  1.9100, 2.5460])

T_240 = np.array([1.0140, 1.0320, 1.0433, 1.0673, 1.0840, 1.1320, 1.1440, 1.1720,
                  1.1980, 1.2293, 1.2813, 1.3573, 1.4200, 1.5600, 1.7413, 1.9840,
                  2.4473, 3.1573])

L_120 = 0.120
L_240 = 0.240


def teor_model(theta, l):
    return 2*np.pi*np.sqrt(l/(g*np.cos(theta)))


def manual_curve_fit(theta, T):

    
    X = np.cos(theta)
    Y = T**2

    
    Z = 1 / X

    k = np.sum(Z * Y) / np.sum(Z * Z)

    
    l_fit = k * g / (4*np.pi**2)

    
    sigma_k = np.sqrt((np.sum(Y*Y)/np.sum(Z*Z) - k*k) / len(Y))
    sigma_l = sigma_k * g / (4*np.pi**2)

    return l_fit, sigma_l


l_fit_120, sigma_l_120 = manual_curve_fit(kut_rad, T_120)
l_fit_240, sigma_l_240 = manual_curve_fit(kut_rad, T_240)


rel_error_120 = abs(l_fit_120 - L_120) / L_120 * 100
rel_error_240 = abs(l_fit_240 - L_240) / L_240 * 100


kut_fit_deg = np.linspace(min(kut_deg), max(kut_deg), 1000)
kut_fit_rad = np.radians(kut_fit_deg)

T_fit_120 = teor_model(kut_fit_rad, l_fit_120)
T_fit_240 = teor_model(kut_fit_rad, l_fit_240)

T_teor_120 = teor_model(kut_fit_rad, L_120)
T_teor_240 = teor_model(kut_fit_rad, L_240)

plt.figure()
plt.scatter(kut_deg, T_120, color="red", label="Eksperimentalni podaci")
plt.plot(kut_fit_deg, T_teor_120, color="blue", label="Teorijsko predviđanje")
plt.plot(kut_fit_deg, T_fit_120, color="green", label="Fit funkcija")
plt.xlabel("θ [°]")
plt.ylabel("T [s]")
plt.title("Period titranja u ovisnosti o kutu za L = 120 mm")
plt.grid(True)
plt.legend()
plt.show()

plt.figure()
plt.scatter(kut_deg, T_240, color="red", label="Eksperimentalni podaci")
plt.plot(kut_fit_deg, T_teor_240, color="blue", label="Teorijsko predviđanje")
plt.plot(kut_fit_deg, T_fit_240, color="green", label="Fit funkcija")
plt.xlabel("θ [°]")
plt.ylabel("T [s]")
plt.title("Period titranja u ovisnosti o kutu za L = 240 mm")
plt.grid(True)
plt.legend()
plt.show()


print(f"\nl_120 = ({np.round(l_fit_120, 4)} ± {np.round(sigma_l_120, 4)}) m")
print(f"Relativna pogreška = {np.round(rel_error_120, 2)} %")

print(f"\nl_240 = ({np.round(l_fit_240, 3)} ± {np.round(sigma_l_240, 3)}) m")
print(f"Relativna pogreška = {np.round(rel_error_240, 2)} %\n")