import numpy as np
import math

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

def funkcija(x):
    return x**2



#zadatak 4

def meda(f, donjag, gornjag, N):
    if donjag>gornjag:
        donjag, gornjag= gornjag, donjag
    elif donjag==gornjag:
        return 0, 0
    else:
        gornja=0
        donja=0
        x=np.linspace(donjag, gornjag, N+1)
        dx=(gornjag-donjag)/N
        for i in range(N):
            donja+=f(x)*dx 
        print(donja)
        for i in range(1, n+1):
            gornja+=a

def funkcija(x):
    return x**2
