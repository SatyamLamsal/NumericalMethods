import numpy as np

def gauss_jordan(A, B):
    A = A.astype(float)
    B = B.astype(float)
    n = len(B)

    for j in range(n):
        if abs(A[j, j]) < 1e-12:
            print('Zero at main diagonal error')
            return None
        
        for i in range(n):
            if i != j:
                ratio = A[i, j] / A[j, j]
                A[i, :] = A[i, :] - ratio * A[j, :]
                B[i] = B[i] - ratio * B[j]
    # Solution vector
    X = np.zeros(n)
    for i in range(n):
        X[i] = B[i] / A[i, i]
        
    return X


A = np.array([[2, 1, -1],
              [-3, -1, 2],
              [-2, 1, 2]], dtype=float)

B = np.array([8, -11, -3], dtype=float)

X = gauss_jordan(A, B)

print("Solution X:")

for i, x in enumerate(X):
    print(f"x{i+1} = {x:.4f}")
