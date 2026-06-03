import numpy as np
import matplotlib.pyplot as plt

class Projectile:
    def __init__(self, v0, angle, Cd=0.47, rho=1.225, A=0.01, m=1.0, g=9.81):
        self.v0 = v0
        self.angle = np.radians(angle)
        self.Cd = Cd
        self.rho = rho
        self.A = A
        self.m = m
        self.g = g
        self.otpor = 0.5 * Cd * rho * A

        self.vx0 = v0 * np.cos(self.angle)
        self.vy0 = v0 * np.sin(self.angle)

    def akceleracija(self, vx, vy):
        v = np.sqrt(vx**2 + vy**2)
        ax = -self.otpor * v * vx / self.m
        ay = -self.otpor * v * vy / self.m - self.g
        return ax, ay

    def simulate_euler(self, dt):
        x, y = 0.0, 0.0
        vx, vy = self.vx0, self.vy0

        xs, ys = [x], [y]

        while y >= 0:
            ax, ay = self.akceleracija(vx, vy)

            vx += ax * dt
            vy += ay * dt
            x += vx * dt
            y += vy * dt

            xs.append(x)
            ys.append(y)

        return xs, ys

    def simulate_rk4(self, dt):
        x, y = 0.0, 0.0
        vx, vy = self.vx0, self.vy0

        xs, ys = [x], [y]

        while y >= 0:

            #k1
            ax1, ay1 = self.akceleracija(vx, vy)
            k1vx, k1vy = ax1, ay1
            k1x, k1y = vx, vy

            #k2
            ax2, ay2 = self.akceleracija(vx + 0.5*k1vx*dt, vy + 0.5*k1vy*dt)
            k2vx, k2vy = ax2, ay2
            k2x, k2y = vx + 0.5*k1vx*dt, vy + 0.5*k1vy*dt

            #k3
            ax3, ay3 = self.akceleracija(vx + 0.5*k2vx*dt, vy + 0.5*k2vy*dt)
            k3vx, k3vy = ax3, ay3
            k3x, k3y = vx + 0.5*k2vx*dt, vy + 0.5*k2vy*dt

            #k4
            ax4, ay4 = self.akceleracija(vx + k3vx*dt, vy + k3vy*dt)
            k4vx, k4vy = ax4, ay4
            k4x, k4y = vx + k3vx*dt, vy + k3vy*dt

            vx += (dt/6)*(k1vx + 2*k2vx + 2*k3vx + k4vx)
            vy += (dt/6)*(k1vy + 2*k2vy + 2*k3vy + k4vy)
            x  += (dt/6)*(k1x  + 2*k2x  + 2*k3x  + k4x)
            y  += (dt/6)*(k1y  + 2*k2y  + 2*k3y  + k4y)

            xs.append(x)
            ys.append(y)

        return xs, ys

proj = Projectile(50, 45)
dt = 1

xs_e, ys_e = proj.simulate_euler(dt)
xs_rk, ys_rk = proj.simulate_rk4(dt)

plt.figure()
plt.plot(xs_e, ys_e, label="Euler dt=0.01")
plt.plot(xs_rk, ys_rk, label="RK4 dt=0.01")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("Euler vs Runge–Kutta 4 (dt = 0.01)")
plt.legend()
plt.grid()
plt.show()