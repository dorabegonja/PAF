import math
import matplotlib.pyplot as plt
import calculus4

def f(x):
    return x**2

def F(x):
    return x**3/3

a=0
b=3
I_analiticki=F(b)-F(a)

donjagranica=[]
gornjagranica=[]
trapez=[]

for n in range(1, 101):
    donja, gornja = calculus4.pravokutna_aproksimacija(f, a, b, n)
    trapez.append(calculus4.trapezna_metoda(f, a, b, n))
    donjagranica.append(donja)
    gornjagranica.append(gornja)
    
plt.plot(range(1, 101), donjagranica, label="Donja granica")
plt.plot(range(1, 101), gornjagranica, label="Gornja granica")
plt.plot(range(1, 101), trapez, label="Trapezna metoda") 
plt.axhline(y=I_analiticki, color='r', linestyle='--', label="Analitički rezultat")
plt.xlabel("Broj podjela n")
plt.ylabel("Vrijednost integrala")
plt.title("Numerička integracija funkcije")
plt.legend()
plt.grid()
plt.show()