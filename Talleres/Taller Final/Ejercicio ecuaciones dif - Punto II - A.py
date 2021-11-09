import math
import numpy as np
import matplotlib.pyplot as plt

def funcion(x,y):
    ec = x * math.exp(3*x) - 40*y
    return ec

def cont_digitos(n):
    cant = 1
    while n > 9:
        n = n / 10
        cant = cant + 1
    return cant

def digitos(n):
    return list(map(int, str(n)))


def error(n, capacidad):
    exponente = cont_digitos(n)
    notacion = int(n * (pow(10, exponente - 1)))
    arreglo = digitos(notacion)

    truncamiento = 0
    for i in range(capacidad, len(arreglo)):
        truncamiento = (truncamiento * 10) + arreglo[i]

    valor = truncamiento / 10
    error = exponente - capacidad

    print("El error de redondeo es ", valor, "x10^", error)

h =  float( input("Tamaño de paso: "))
s =  float( input("Hasta que valor? "))
n = int((s / h) + 1)
x = np.zeros(n)
y = np.zeros(n)

print(x[0], y[0])

for i in np.arange(1,n):
    y[i] = y[i - 1] + (funcion(x[ i - 1], y[i - 1])) * h
    x[i] = x[i - 1] + h
    print(x[i],y[i])

error(n,int(h))
plt.scatter(x,y)
plt.show()

