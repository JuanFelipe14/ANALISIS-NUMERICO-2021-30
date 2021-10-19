import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

#Interpolacion de Lagrange

#INGRESAMOS LOS DATOS

xi = np.array([6, 8, 10, 12, 14, 16, 18, 20]) #Hora
fi = np.array([7, 9, 12, 18, 21, 19, 15, 10]) #Grados

#PROCEDIMIENTO

n = len(xi)
x = sym.Symbol('x')
polinomio = 0

for i in range(0,n,1):
    numerador = 1
    denominador = 1
    for j in range(0,n,1):
        if (i!=j):
            numerador = numerador * (x-xi[j])
            denominador = denominador * (xi[i] - xi[j])
        termino = (numerador / denominador) * fi[i]
    polinomio = polinomio + termino
polisimple = sym.expand(polinomio)

px = sym.lambdify(x, polinomio)

# Vectores para graficas

muestras = 51
a = np.min(xi)
b = np.max(xi)
p_xi = np.linspace(a, b, muestras)
pfi = px(p_xi)

# SALIDA

print('Polinomio')
print(polinomio)
print('Polinomio simple: ')
print(polisimple)

#GRAFICA
plt.plot(xi, fi, 'o')
plt.xlabel('Hora')
plt.ylabel('Grados')
plt.plot(p_xi,pfi)
plt.show()