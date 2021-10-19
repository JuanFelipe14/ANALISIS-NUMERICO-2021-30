
import scipy.interpolate as spi
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
import numpy as np
from scipy.interpolate import UnivariateSpline

# Base imponible solicitada en el ejercicio
Base = 5000000

# Conjuntos de datos que nos provee el enunciado (Valores de base imponible
# cuota integra y tasa marginal)
baseImp = np.array([4410000, 4830000, 5250000,5670000])
quota = np.array([1165978, 1329190, 1501474,1682830])
tipoMarginal = np.array([0.3886, 0.4102, 0.4318,0.4534])

# Interpolaciones Lineal, cuadrática y cúbica para cálculo de cuota
fun = spi.interp1d(baseImp, quota , kind = 'linear')
tipoCuadratic = spi.interp1d(baseImp, quota, kind='quadratic')
tipoCubic = CubicSpline(baseImp, quota)

# Interpolación para cálculo de tipo marginal
marg1 = spi.interp1d(baseImp, tipoMarginal , kind = 'linear',fill_value='extrapolate')
marg2 = spi.interp1d(baseImp, tipoMarginal, kind = 'quadratic',fill_value='extrapolate')
marg3 = CubicSpline(baseImp, tipoMarginal)

# Arreglos de datos para posterior graficación
linear=np.array([fun(4410000), fun(4830000), fun(5250000),fun(5670000)])
acuad=np.array([tipoCuadratic(4410000), tipoCuadratic(4830000), tipoCuadratic(5250000),tipoCuadratic(5670000)])
acub=np.array([tipoCubic(4410000), tipoCubic(4830000), tipoCubic(5250000),tipoCubic(5670000)])


#Impresión de resultados (tipo marginal calculado y costo final de la cuota)
print("Tipo marginal obtenido con cuadrática: {:.12f}".format(marg2(Base)*100), '%')
print("Tipo marginal obtenido con cúbica: {:.12f}".format(marg3(Base)*100), '%')

print("Cuota con lineal: {:.0f}".format(fun(Base)))
print("Cuota con cuadrática: {:.5f}".format(tipoCuadratic(Base)))
print("Cuota con cúbica: {:.5f}".format(tipoCubic(Base)))


#Graficas de los valores (Cuota de acuerdo a la base imponible)
plt.plot(baseImp,linear, 'o', color='darkred',linestyle='--')
plt.plot(baseImp,acub,color='darkblue',linestyle='--')
plt.plot(baseImp,acuad,color='orange',linestyle='--')
plt.xlabel("Base imponible")
plt.ylabel("Cuota")
plt.show()
