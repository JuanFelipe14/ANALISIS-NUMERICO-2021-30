import numpy as np
from scipy.integrate import odeint
import plotly.graph_objects as go
from datetime import date
from datetime import timedelta
import pylab as pl
import sympy as sy

def f(beta,S0):
    return (0.021)

# Poblacion total con valor N
N = 479853

# Valores Iniciales de los sujetos Infectados (IO) y los sujetos que se recuperaron (R0)
# El valor de sujetos infectados es 1 para que inicie la epidemia.
I0,R0 = 1, 0

# Valor inicial de sujetos suceptibles de infectarse (S0)
# Se define el valor inicial por ( (Tamaño poblacion) - I )
S0 = N - I0 - R0

#Tasa de transmision (Beta), tasa de recuperacion de 1/dias (Gamma)
beta, gamma = 0.06, 0.021

# Dias (Grafica)   1300 1300 - 652 652 - 71 71 - 60 60
t = np.linspace(0, 1300, 1300)

#PUNTO 7

R0 = (beta * 1.5 * S0) / (gamma * N)

# Ecuaciones diferenciales del modelo SIR (Definidas en el parcial)
def deriv(y, t, N, beta, gamma):
    S, I, R, = y
    #Primera Ecuacion:
    dSdt = -beta * S * I / N
    #Segunda Ecuacion:
    dIdt = beta * S * I / N - gamma * I
    #Tercera Ecuacion
    dRdt = gamma * I

    return dSdt, dIdt, dRdt
#Primera Ecuacion:

def eulerMejorado(f, x, y, h, m):
    u = np.zeros([m,2],dtype=float)
    for i in range(m):
        yn = y + h*f(x,y)
        y = y + h*(f(x,y) + f(x+h,yn))/2
        x += h
        u[i,0] = x
        u[i,1] = y
    return u
ua = eulerMejorado(f,0,1,0.1,20)

print("Ecuación3:", ua)
np.set_printoptions(precision=5)
sy.Matrix(ua)
# Vector de las condicionales iniciales
y0 = S0, I0, R0

# Resolver el sistema de ecuaciones diferenciales.
ret = odeint(deriv, y0, t, args=(N, beta, gamma))
S, I, R = ret.T

#Determinamos porcentajes de la poblacion  - PUNTO 4
def calculoPorcentajes():
    Poblacion = 479853
    infectados = 1
    recuperados = 0
    contagios = 0
    suceptibles = 479853
    duracion = 14

    inicio = date.today() - timedelta(days=609)
    lista_fecha = [inicio]
    lista_contagios = [contagios]
    lista_recuperados = [recuperados]
    lista_suceptibles = [suceptibles]
    total_contagios = 0
    total_recuperados = 0
    total_infectados = 0

    for i in range(t.size):
        contagios = infectados * 1.5 * suceptibles / Poblacion  # infectados, C, 1/N
        contagios_estadistica = contagios * 1.25 / 100
        suceptibles = suceptibles - contagios
        inicio = inicio + timedelta(days=1)
        recuperados_dia = infectados
        recuperados = recuperados + recuperados_dia
        infectados = infectados + contagios - recuperados_dia
        total_contagios = total_contagios + contagios
        total_infectados = total_infectados + infectados
        lista_fecha.append(inicio)
        lista_contagios.append(contagios)
        lista_recuperados.append(recuperados)
        lista_suceptibles.append(suceptibles)

        primerCondicional = (gamma / (beta * 1.5))
        segundoCondicional = S / N

    """        if (primerCondicional > segundoCondicional):
            print("Situacion controlada en la fecha: ", lista_fecha[i])
    """

    max = 0
    fecha = 0

    for i in range(0, len(lista_contagios)):
        if (max < lista_contagios[i]):
            max = lista_contagios[i]
            fecha = lista_fecha[i]

    print("El contagio maximo: ", max, " Fecha: ", fecha)

    PorcenteajeR = recuperados * 100 / total_contagios
    print("Porcentajes recuperados: ", round(PorcenteajeR, 2), "%")

    PorcenteajeI = total_infectados * 100 / Poblacion
    print("Porcentajes infectados: ", round(PorcenteajeI, 2), "%")


calculoPorcentajes()

# GRAFICO
fig = go.Figure()
fig.add_trace(go.Scatter(x=t, y=S,mode='lines',name = 'Suceptible'))
fig.add_trace(go.Scatter(x=t, y=I,mode='lines',name = 'Infectado'))
fig.add_trace(go.Scatter(x=t, y=R,mode='lines',name = 'Recuperado'))

fig.update_layout(
    title = "Modelo RIS - COVID 19",
    xaxis_title = "Dias",
    yaxis_title = "Poblacion (Millones)",
    legend_title = "Personas"
)

pl.plot(ua[:,0],ua[:,1],'ob')

fig.show()

