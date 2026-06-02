import numpy as np
import matplotlib.pyplot as plt

m = 9.11e-31

dt = 1e-13
koraci = 4000   #broj iteracija

def putanja(q, E, B):
    r = np.array([0., 0., 0.])
    v = np.array([1e5, 2e5, 3e5])

    x, y, z = [], [], []

    for i in range(koraci):
        x.append(r[0])
        y.append(r[1])
        z.append(r[2])

        sila = q * (E + np.cross(v, B))
        a = sila / m

        v = v + a * dt
        r = r + v * dt

    return x, y, z

kombinacije = [
    (np.array([0,0,0]),     np.array([0,0,1])),      #B
    (np.array([5e5,0,0]),   np.array([0,0,1])),      #E u x smjeru
    (np.array([0,5e5,0]),   np.array([0,0,1])),      #E u y smjeru
    (np.array([0,0,5e5]),   np.array([0,0,1])),      #E paralelno s B
]

fig = plt.figure(figsize=(12, 12))

for i, (E, B) in enumerate(kombinacije, start=1):
    ax = fig.add_subplot(2, 2, i, projection="3d")

    xe, ye, ze = putanja(-1.6e-19, E, B)
    xp, yp, zp = putanja(+1.6e-19, E, B)

    ax.plot(xe, ye, ze, label="Elektron")
    ax.plot(xp, yp, zp, label="Pozitron")

    ax.set_title(f"E = {E}, B = {B}")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    ax.legend()

plt.tight_layout()
plt.show()