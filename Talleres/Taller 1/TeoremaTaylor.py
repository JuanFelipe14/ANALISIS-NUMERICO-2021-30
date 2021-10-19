import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from sympy.parsing.sympy_parser import parse_expr

X = sp.Symbol('x')

def TeoremaTaylor(f,x,Dx,t):
    taylor = []
    for i in range(len(x)):

        A = sp.sympify(f).subs(X,x[i])

        B = sp.diff(f,X).subs(X,x[i])
        B = (np.transpose(B) * Dx[i])

        C = 0.5 * np.transpose(Dx[i])

        D = sp.diff(f,X,2).subs(X,(x[i] + t * Dx[i]))

        C = ((C * D) * Dx[i])

        LadoDerecho = A + B + C
        taylor.append(LadoDerecho)

    return taylor

## INPUT ##
funcion = input("Ingrese una funcion univariable con 'x' (eje: x**2-4*x): " ) # x**2+6*x
funcion = parse_expr(funcion,locals())
delta = float(input("Ingrese un delta x: ")) # 0.01
t = float(input("Ingrese un valor para t: ")) #1
intervalos = input("Ingrese un intervalo (separado por coma y sin parentesis ni corchetes): ")# [-6, 1]
intervalos = intervalos.split(",")

for i in range(len(intervalos)):
    intervalos[i] = float(intervalos[i])

# Ejecucion del programa

ejex = [i for i in np.arange(intervalos[0],intervalos[1],step=0.1)]

y = []

deltax = []

for i in range(len(ejex)):
    deltax.append(delta)
    valorY = sp.sympify(funcion).subs(X, ejex[i])
    y.append(valorY)

# Grafico

plt.grid(True)
plt.plot(ejex, y, color="red", label='Exacta')
plt.plot(ejex, TeoremaTaylor(funcion, ejex, deltax, t), color="blue", label='Taylor')
plt.legend(loc="upper right")
plt.show()