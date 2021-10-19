import numpy as np


def jacobi(A, b, x0, eps=1e-16, n=500):
    D = np.diag(np.diag(A))
    try:
        LU = A - D
    except:
        print("🔴 La matriz no es simetrica")
    else:
        x = x0
        for i in range(0, n):
            D_inv = np.linalg.inv(D)
            xTemp = x
            x = np.dot(D_inv, np.dot(-(LU), x) + b)
            print(f"Pasos: {i} - x: {x}")
            if np.linalg.norm(x - xTemp) < eps:
                return x
