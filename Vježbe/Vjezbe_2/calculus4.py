import math
import numpy as np

def derivacija_tocka(f, x, epsilon, metoda="three-step"):
    if metoda == "two-step":
        dertocka = (f(x + epsilon) - f(x)) / epsilon
    else:
        dertocka = (f(x + epsilon) - f(x - epsilon)) / (2 * epsilon)
    return dertocka

def derivacija_interval(f, donjag, gornjag, epsilon, metoda="three-step"):
    derinterval = []
    tocke = np.linspace(donjag, gornjag, 100)
    for x in tocke:
        derinterval.append(derivacija_tocka(f, x, epsilon, metoda))
    return tocke, derinterval

def pravokutna_aproksimacija(f, a, b, n):
    dx=(b-a)/n
    donja_suma=0
    gornja_suma=0
    x=a
    for i in range(n):
        donja_suma += f(x)
        gornja_suma += f(x+dx)
        x += dx
    return donja_suma*dx, gornja_suma*dx

def trapezna_metoda(f, a, b, n):
    dx=(b-a)/n
    suma=0
    x=a
    for i in range(n):
        suma += (f(x)+f(x+dx))/2
        x += dx
    return suma*dx