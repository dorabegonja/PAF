import math
import matplotlib.pyplot as plt
import calculus4

def f(x):
    return x**2

def F(x):
    return x**3/3

a=0
b=2
I_analiticki=F(b)-F(a)
n_vrijednosti=[5, 10, 20, 50, 100]
pravokutnik_greske=[]
trapez_greske=[]

for n in n_vrijednosti:
    donja, gornja = calculus4.pravokutna_aproksimacija(f, a, b, n)
    trapez = calculus4.trapezna_metoda(f, a, b, n)
    pravokutnik = (donja + gornja)/2
    pravokutnik_greske.append(abs(pravokutnik - I_analiticki))
    trapez_greske.append(abs(trapez - I_analiticki))

plt.plot(n_vrijednosti, pravokutnik_greske, label="Pravokutna aproksimacija")
plt.plot(n_vrijednosti, trapez_greske, label="Trapezna metoda")
plt.xlabel(f'Broj podjela n')
plt.ylabel(f'Greška')
plt.title(f'Greška numeričke integracije')
plt.legend()
plt.grid()
plt.show()