import math

import numpy as np
import matplotlib.pyplot as plt
#Realizado por: Juan Felipe Arias-Laura Jiménez
                #Esteban Rojas-Natalia Gaona
funcion = lambda x : x**3-2*(x)-5

xa = -1
xb = 3

def biseccion(funcion, xa, xb, iteraciones, errormaximo):
    x = (xa + xb) / 2
    for i in range(iteraciones):
        if (funcion(x) * funcion(xb) < 0):  # la raiz contiene el cambio de signo al superior
            xa = x
        elif (funcion(x) * funcion(xb) > 0):  # la raiz contiene el cambio de signo al inferior
            xb = x
        else:
            break  # la funcion vale cero
        xAnterior = x
        x = (xa + xb) / 2
        e = abs((
                            x - xAnterior) / x)  # sacar el error nuevo con valor absoluto,recuerden que es la diferencia de una iteracion a la siguiente se saca con la formula de error va a ser igual a valor absoluto de x sub i +1(el valor mayor ) menos x sub i (el valor menor)
        if (e < errormaximo):  # se corta el ciclo si el error nuevo es mayor al error inicial
            break
        print(i, x, funcion(x), e)


biseccion(funcion, 0, 2, 1000,1e-56)  # le pasamos la funcion, el intervalo menor, el intervalo mayor, las iteraciones y el error(la tolerancia)

xi = np.linspace(xa,xb)
fx = funcion
fi = fx(xi)
dx = (xa + xb) / 2
pendiente = (fx(xa+dx)-fx(xa))/(xa+dx-xa)
b0 = fx(xa) - pendiente*xa
tangentei = pendiente*xi+b0

fxa = fx(xa)
xb = xa + dx
fxb = fx(xb)

plt.plot(xi,fi, label='f(x)')

plt.plot(xi,tangentei, label='Biseccion')
plt.plot(xa,fx(xa),'go', label='xa')
plt.plot(xa+dx,fx(xa+dx),'ro', label='xb')
plt.plot((-b0/pendiente),0,'yo', label='xc')

plt.plot([xa,xa],[0,fxa],'m')
plt.plot([xb,xb],[0,fxb],'m')

plt.axhline(0, color='k')
plt.title('Método de biseccion')
plt.legend()
plt.grid()
plt.show()