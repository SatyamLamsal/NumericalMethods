import numpy as np

def gauss_elimination(a, b):
    A = np.array(a, dtype=float)
    B = np.array(b, dtype=float)
    n = len(B)

    for k in range(n - 1):
        if abs(A[k][k]) < 1e-12:
            raise ValueError(f"Zero pivot encountered at row {k}")
        for i in range(k + 1, n):
            factor = A[i][k] / A[k][k]
            A[i, k:] -= factor * A[k, k:]
            B[i] -= factor * B[k]

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        if abs(A[i][i]) < 1e-12:
            raise ValueError(f"Zero pivot encountered at row {i}")
        x[i] = (B[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i][i]

    return x

A = [[2, -1, 1],
     [3, 3, 9],
     [3, 3, 5]]
B = [2, -1, 4]

solution = gauss_elimination(A, B)
print("Solution:", solution)
