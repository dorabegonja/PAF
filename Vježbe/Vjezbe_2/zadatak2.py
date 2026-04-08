import numpy as np
import matplotlib.pyplot as plt
import math
import particle as p

g = 9.81

dt_values = np.linspace(0.0001, 0.1, 100)
rel_pogreska = []

for t in dt_values:
    p1 = p.Particle(10, 60, 0, 0)
    domet_num = p1.range(dt=t)
    angle_rad = math.radians(60)
    domet_analiticki = (10**2 * math.sin(2 * angle_rad)) / g
    r_pog = abs(domet_num - domet_analiticki) / domet_analiticki
    rel_pogreska.append(r_pog)

plt.plot(dt_values, rel_pogreska)
plt.xlabel('Δt')
plt.ylabel('Relativna pogreška')
plt.title('Ovisnost relativne pogreške o vremenskom koraku')
plt.grid()
plt.show()