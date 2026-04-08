import math
import matplotlib.pyplot as plt

g = 9.81

class Particle:
    def __init__(self, v0=0, angle=0, x0=0, y0=0):
        self.v0 = v0
        self.angle = math.radians(angle)
        self.x0 = x0
        self.y0 = y0

        self.reset()

    def reset(self):
        self.x = self.x0
        self.y = self.y0
        self.vx = self.v0 * math.cos(self.angle)
        self.vy = self.v0 * math.sin(self.angle)
        self.t = 0

        self.x_list = [self.x]
        self.y_list = [self.y]

    def __move(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.vy -= g * dt
        self.t += dt

        self.x_list.append(self.x)
        self.y_list.append(self.y)

    def range(self, dt=0.01):
        self.reset()

        while self.y >= 0:
            self.__move(dt)

        return self.x

    def plot_trajectory(self, dt=0.01):
        self.reset()

        while self.y >= 0:
            self.__move(dt)

        plt.plot(self.x_list, self.y_list)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Putanja projektila")
        plt.grid()
        plt.show()