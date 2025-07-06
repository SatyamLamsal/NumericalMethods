def gauss_jordan(matrix):
    n = len(matrix)
    
    for i in range(n):
        if matrix[i][i] == 0.0:
            for j in range(i+1, n):
                if matrix[j][i] != 0:
                    matrix[i], matrix[j] = matrix[j], matrix[i]
                    break
                else:
                    raise ValueError("Matrix is singular or system has no unique solution.")

        divisor = matrix[i][i]
        for k in range(len(matrix[i])):
            matrix[i][k] /= divisor


        for j in range(n):
            if i != j:
                factor = matrix[j][i]
                for k in range(len(matrix[j])):
                    matrix[j][k] -= factor * matrix[i][k]

    return [row[-1] for row in matrix]

augmented_matrix = [
    [2, 1, -1,   8,10],
    [-3, -1, 2, -11,20],
    [-2, 1, -8,  -3,30],
    [-4,1,3,-4, 40]
]

solution = gauss_jordan(augmented_matrix)
print("Solution:", solution)
