def igual(A):
    x = []
    for i in range(len(A)):
        for j in range(len(A[i])):
            x.append(A[i][j])
    return x


def desenfoque(A):
    d = []
    for i in range(len(A)):
        for j in range(len(A[i])):
            B = []
            if i-1 < 0:
                B.append(0.)
            else:
                B.append(A[i-1, j])
            if i+1 > len(A[i]) - 1:
                B.append(0.)
            else:
                B.append(A[i+1, j])
            if j-1 < 0:
                B.append(0.)
            else:
                B.append(A[i, j-1])
            if j+1 > len(A[i]) - 1:
                B.append(0.)
            else:
                B.append(A[i, j+1])
            d.append(B)
    return d

