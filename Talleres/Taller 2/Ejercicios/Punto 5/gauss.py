import numpy as np


def gauss(A):
    D = np.diag(np.diag(A))
    try:
        LU = A - D
    except:
        print("🔴 La matriz no es simetrica")
    else:
        BJ = np.dot(np.linalg.inv(D), -LU)
        print(BJ)
