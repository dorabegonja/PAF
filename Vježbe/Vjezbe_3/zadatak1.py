import numpy as np
import matplotlib.pyplot as plt

class Projectile:
    def __init__(self, x0, y0, v0, angle_deg, m=1.0, k=0.1, g=9.81):
        self.x = x0
        self.y = y0
        self.vx = v0 * np.cos(np.radians(angle_deg))
        self.vy = v0 * np.sin(np.radians(angle_deg))
        self.m = m
        self.k = k
        self.g = g

    def step(self, dt):
        v = np.sqrt(self.vx**2 + self.vy**2)

        ax = -(self.k / self.m) * v * self.vx
        ay = -self.g - (self.k / self.m) * v * self.vy

        self.vx += ax * dt
        self.vy += ay * dt
        self.x += self.vx * dt
        self.y += self.vy * dt

    def simulate(self, dt):
        xs, ys = [self.x], [self.y]
        while self.y >= 0:
            self.step(dt)
            xs.append(self.x)
            ys.append(self.y)
        return np.array(xs), np.array(ys)

def test_dt_values():
    dts = [0.1, 0.05, 0.02, 0.01, 0.005]
    plt.figure(figsize=(10, 6))

    for dt in dts:
        p = Projectile(0, 0, v0=50, angle_deg=45, k=0.05)
        x, y = p.simulate(dt)
        plt.plot(x, y, label=f"dt = {dt}")

    plt.xlabel("x [m]")
    plt.ylabel("y [m]")
    plt.title("Usporedba putanja za različite dt (Eulerova metoda)")
    plt.legend()
    plt.grid()
    plt.show()

test_dt_values()