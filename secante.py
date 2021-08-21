# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math

import numpy as np
from matplotlib import pyplot as plt
#Realizado por: Juan Felipe Arias-Laura Jiménez
                #Esteban Rojas-Natalia Gaona
def f(x):
    return x**3-2*(x)-5


def secante(a, b, tol, max_iter):
    iter = 0
    c = (a + b) / 2
    i = 0
    while (abs(f(c)) > tol and iter < max_iter):
        c = b - (f(b) * (b - a) / (f(b) - f(a)))
        a = b
        b = c
        i = i + 1
        print("Iteracion: ", i, " raiz: ", c)

a=-1
b=3
iteraciones=200
xa = 1.5
secante(a, b, 1e-56, iteraciones)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
xi = np.linspace(a,b,iteraciones+1)
fi = f(xi)
c = (b-xa)/2
pendiente = (f(xa+c)-f(xa))/(xa+c-xa)
b0 = f(xa) - pendiente*xa
tangentei = pendiente*xi+b0

fxa = f(xa)
xb = xa + c
fxb = f(xb)

plt.plot(xi,fi, label='f(x)')
plt.plot(xi,tangentei, label='secante')
plt.plot(xa,f(xa),'go', label='xa')
plt.plot(xa+c,f(xa+c),'ro', label='xb')
plt.plot((-b0/pendiente),0,'yo', label='xc')

plt.plot([xa,xa],[0,fxa],'m')
plt.plot([xb,xb],[0,fxb],'m')

plt.axhline(0, color='k')
plt.title('Método de la Secante')
plt.legend()
plt.grid()
plt.show()