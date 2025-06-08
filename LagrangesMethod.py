import numpy as np
import matplotlib.pyplot as plt

def lagrange_interpolation(x_points, y_points, x):
    total = 0
    n = len(x_points)
    
    for i in range(n):
        term = y_points[i]
        for j in range(n):
            if j != i:
                term *= (x - x_points[j]) / (x_points[i] - x_points[j])
        total += term
    
    return total


x_points = np.array([5,7,11,13,17])
y_points = np.array([150,392,1452,2366,5202])

print(f"Interplated Val {lagrange_interpolation(x_points, y_points, 9)}")

x_values = np.linspace(min(x_points), max(x_points), 500)
y_values = np.array([lagrange_interpolation(x_points, y_points, xv) for xv in x_values])

plt.scatter(x_points, y_points, color='red', label='Data points')
plt.plot(x_values, y_values, label='Lagrange Interpolation')
plt.title('Lagrange Interpolation Polynomial')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

