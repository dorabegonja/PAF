import math
import matplotlib.pyplot as plt

M = [0.052, 0.124, 0.168, 0.236, 0.284, 0.336]
phi = [0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472]

n = len(M)

sum_xy = sum(M[i] * phi[i] for i in range(n))
sum_x2 = sum(phi[i]**2 for i in range(n))

Dt = sum_xy / sum_x2

sum_y2 = sum(M[i]**2 for i in range(n))
sigma_a = math.sqrt((1/n) * (sum_y2 / sum_x2 - Dt**2))

print("Dt =", Dt)
print("Standardna pogreška σa =", sigma_a)

plt.scatter(phi, M, label="Podatci", color="blue")

x_line = phi
y_line = [Dt * x for x in x_line]

plt.plot(x_line, y_line, color="red", label=" Model M = Dt · φ")

plt.xlabel("φ (rad)")
plt.ylabel("M (Nm)")
plt.title("Linearna regresija: M = Dt · φ")
plt.legend()
plt.grid(True)
plt.show()