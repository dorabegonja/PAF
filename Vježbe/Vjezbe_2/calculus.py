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