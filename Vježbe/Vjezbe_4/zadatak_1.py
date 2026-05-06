import numpy as np
import matplotlib.pyplot as plt

m = 9.11e-31

B = np.array([0, 0, 1])
E = np.array([0, 0, 0])

dt = 1e-13
koraci = 4000

def putanja(q):
    r = np.array([0., 0., 0.])
    v = np.array([1e5, 2e5, 3e5])

    x, y, z = [], [], []

    for i in range(koraci):
        x.append(r[0])
        y.append(r[1])
        z.append(r[2])

        #Lorentzova sila
        sila = q * (E + np.cross(v, B))
        a = sila / m

        v = v + a * dt
        r = r + v * dt

    return x, y, z

xe, ye, ze = putanja(-1.6e-19)
xp, yp, zp = putanja(+1.6e-19)

fig = plt.figure()
ax = fig.add_subplot(projection="3d")

ax.plot(xe, ye, ze, label="Elektron")
ax.plot(xp, yp, zp, label="Pozitron")

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.legend()

plt.show()