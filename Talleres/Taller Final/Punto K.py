import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate

def imprimir_resultados(x, y1, y2):
    plt.plot(x, y1, '-r',linewidth=2)
    plt.plot(x, y2, '-b',linewidth=2 )
    plt.axhline(0, color='k')
    plt.show()

x = np.arange(0,33,4).tolist()

y1 = [0, 6, 8, 8.5, 9, 8, 7, 5,0]
y2 = [0, -3, -2.5, -2.8, -3.4, -4.2, -4, -2.5, 0]

area = integrate.simpson(y1, x)
area2 = integrate.simpson(x, y2)
print("El area del derrame del petroleo es de: {:.8f}".format(area + area2))

imprimir_resultados(x,y1, y2)