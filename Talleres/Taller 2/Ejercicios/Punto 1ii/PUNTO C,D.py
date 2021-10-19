import numpy as np
from scipy.linalg import solve

n = 3
a = []
b = []

def seidel(a, x, b):
    n = len(a)
    for j in range(0, n):
        d = b[j]
        for i in range(0, n):
            if(j != i):
                d-=a[j][i] * x[i]
        x[j] = d / a[j][j]
        para=(b[j]-d)/ a[j][j]
        if x[j]==para:
          print("FIN.")
    return x

def matrizTransicionGS(a):
  #d (diagonal).
  d = np.diag(a)
  d = np.diag(d)
  if(not(np.linalg.det(d))): #Evaluando que tenga inversa...
    return
  dInv = np.linalg.inv(d)
  #l (lower): matriz inferior triangular.
  l = np.tril(a)
  #u (upper): matriz superior triangular.
  u = np.triu(a)
  ident = np.identity(len(a))
  dInv_l = np.dot(dInv, l)
  _dInv_u = np.dot(-dInv, u)
  if(not(np.linalg.det(_dInv_u))): #Evaluando que tenga inversa...
    return
  else:
    if(np.linalg.det(ident + dInv_l)): #Evaluando que tenga inversa...
      t = np.dot(np.linalg.inv(ident + dInv_l), _dInv_u)
      return(t)
    return

def radioEspectral(a):
  t = matrizTransicionGS(a)
  eigenValues = np.linalg.eigvals(t)
  #Calcular y retornar el valor máximo de 'eigenValues'.
  return max(eigenValues)

def jacobi(A, b, x, n):
  y=[]
  D = np.diag(A)
  R = A-np.diagflat(D)
  for i in range(n):
      y=x
      x = (b-np.dot(R,x))/D
      print("({})->{}".format(i+1, x))
      if(i > 0):
        e1 = (x-y)
        print("Vector error: ",abs(e1))
  return x

def sor(a,b,w,x):
  for i in range(len(a)):
    sigma=0
    for j in range(len(a)):
        if j != i:
          sigma+=a[i][j]*x[j]
    if(a[i][i]!=0):
          x[i] += w*(((b[i]-sigma)/a[i][i])-x[i])
  return x

x = [0, 0, 0]
a = [[4, 3, 0],[3, 4, -1],[0, -1, 4]]
#a1: matriz idéntica a 'a' para radio espectral.
a1 = np.array([[4, 3, 0],
              [3, 4, -1],
              [0, -1, 4]])
a2 = [[4, 3, -2],[3, 4, -1],[0, -1, 4]]
b = [0.254,-1.425,2.978]


print("--------------- SEIDEL -------------  ")
for i in range(0, 25):
    x = seidel(a, x, b)
    print(i,x)
print('\n\n\n')

print("--------------- SIDEL ------------- ")
for i in range(0, 25):
    x = seidel(a2, x, b)
    print(i,x)
print('\n\n\n')

x=[0,0,0]
print("--------------- SOR -------------  ")
w=0
for j in range(0,15):
  w+=0.125
  print("W = ",w)
  for i in range(0, 25):
      x = sor(a,b,w,x)
      print(i,x)
  print(" ")

print('\n\n')

print("-------------- JACOBI -------------  ")
A = np.array([[4,3,0],[3,4,-1],[0,-1,4]])
b = [0.254,-1.425,2.978]
x = [1,2,3]
n = 30
x = jacobi(A, b, x, n)
print("RESULTADO -> {}".format(solve(A,b)))