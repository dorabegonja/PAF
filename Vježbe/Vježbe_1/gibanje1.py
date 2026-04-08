import matplotlib.pyplot as plt
F = float(input("Unesite silu u N: "))
m = float(input("Unesite masu čestice u kg (mora biti pozitivna): "))
t_max = 10  #koliko dugo simuliramo gibanje
dt = 0.01  #vremenski korak
n = int(t_max / dt)  #koliko koraka trebamo napravit
t = [0]
x = [0]  # početna pozicija
v = [0]  # početna brzina
a = [F/m]  # akceleracija konstantna
#numeričko rješavanje (Eulerova metoda)
for i in range(n):
    t_new = t[-1] + dt  #-1 označava zadnji element liste
    v_new = v[i] + a[-1] * dt
    x_new = x[i] + v_new * dt
    t.append(t_new)
    v.append(v_new)
    x.append(x_new)
    a.append(a[-1])  #konstantna akceleracija
plt.figure(figsize=(12, 8)) #veličina grafa
#x-t graf
plt.subplot(3,1,1) #3 reda, 1 stupac, 1. graf
plt.plot(t, x, color='blue')
plt.title("x − t graf")
plt.xlabel("t [s]")
plt.ylabel("x [m]")
plt.grid(True)
#v-t graf
plt.subplot(3,1,2)
plt.plot(t, v, color='green')
plt.title("v − t graf")
plt.xlabel("t [s]")
plt.ylabel("v [m/s]")
plt.grid(True)
#a-t graf
plt.subplot(3,1,3)
plt.plot(t, a, color='red')
plt.title("a − t graf")
plt.xlabel("t [s]")
plt.ylabel("a [m/s²]")
plt.grid(True)
plt.show()