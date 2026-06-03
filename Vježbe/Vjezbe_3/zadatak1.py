import numpy as np
import matplotlib.pyplot as plt

class Projectile:
    def __init__(self, v0, angle, Cd=0.47, rho=1.225, A=0.01, m=1.0, g=9.81):
        self.v0 = v0
        self.angle = np.radians(angle)
        self.Cd = Cd  #koeficijent otpora zraka
        self.rho = rho 
        self.A = A
        self.m = m
        self.g = g
       
        self.otpor = 0.5 * Cd * rho * A

        self.vx0 = v0 * np.cos(self.angle)
        self.vy0 = v0 * np.sin(self.angle)

    def simulate(self, dt):
        x, y = 0.0, 0.0 
        vx, vy = self.vx0, self.vy0 

        xs, ys = [x], [y]

        while y >= 0:
            v = np.sqrt(vx**2 + vy**2)
            
            Fx = -self.otpor * v * vx
            Fy = -self.otpor * v * vy - self.m * self.g

            ax = Fx / self.m
            ay = Fy / self.m

            #Euler
            vx += ax * dt 
            vy += ay * dt
            x += vx * dt
            y += vy * dt

            xs.append(x)
            ys.append(y)
        return xs,ys

proj = Projectile(v0=50, angle=45)
dt_vrijednosti = [1.3, 0.1, 0.05, 0.3, 0.01, 0.005]
#veci dt - manje precizno
#manji dt - preciznije

plt.figure()

for dt in dt_vrijednosti:
    xs, ys = proj.simulate(dt)
    plt.plot(xs, ys, label=f"dt={dt}")

plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("Kosi hitac s otporom zraka – Eulerova metoda")
plt.legend()
plt.grid()
plt.show()