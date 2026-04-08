from particle import Particle
import math
import matplotlib.pyplot as plt

v0 = 10      # m/s
angle = 45   # stupnjevi
g = 9.81

p = Particle(v0, angle)

D_num = p.range()
D_analiticki = (v0**2 * math.sin(math.radians(2*angle))) / g

print("Numerički domet:", D_num)
print("Analitički domet:", D_analiticki)
print("Odstupanje:", abs(D_num - D_analiticki))

p.plot_trajectory()