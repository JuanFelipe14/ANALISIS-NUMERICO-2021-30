import numpy as np
import desenfoque as des
import jacobi as jac
import gauss as gau

A = np.random.rand(800, 600)
x = des.igual(A)
d = des.desenfoque(A)
x0 = np.zeros_like(x)

j = jac.jacobi(d, x, x0, n=10)
g = gau.gauss(d)
