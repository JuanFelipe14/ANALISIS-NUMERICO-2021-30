import math
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

fx = input("Introduce la expreseion : ")
xi = float(input("xi :"))
tol = 0.05
error = 100
xiAnt = 1
fx = sp.sympify(fx)

while True:
    yi = (xi + 1)**(1/3)
    zi = (yi + 1)**(1/3)
    xi1 = zi - ((zi - yi)**2 / (zi - (2*yi)+ xi))
    error = math.fabs((xi1-xiAnt)/xi1)*100

    xiAnt = xi1
    xi = xi1

    if error < tol:
        break

print("yi : ", yi)
print("xi : ",xi)
print("xi+1 : ", xi1)
print("Error : ", error)

x = np.arange(0,2,0.2)
y = x**3-x-1

plt.plot(x,y,"g-")
plt.axhline(0)
plt.axvline(0)
plt.show()