import matplotlib.pyplot as plt
def jednoliko_gibanje(F, m, t_max=10, dt=0.01):
    t = [0]
    x = [0]
    v = [0]
    a = [F/m] 
    n = int(t_max/dt)
    #Eulerova metoda
    for i in range(n):
        t_new = t[-1] + dt
        v_new = v[-1] + a[-1] * dt
        x_new = x[-1] + v[-1] * dt
        t.append(t_new)
        v.append(v_new)
        x.append(x_new)
        a.append(a[-1])
    plt.figure(figsize=(12, 8))
    #x-t graf
    plt.subplot(3,1,1)
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
F = float(input("Unesite silu u N: "))
m = float(input("Unesite masu u kg (masa mora biti pozitivna):"))
jednoliko_gibanje(F, m)