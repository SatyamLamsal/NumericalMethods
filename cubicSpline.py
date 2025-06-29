import numpy as np
import matplotlib.pyplot as plt
import math

def F(x):
    return (math.cos(x)*(180/3.14) * math.cos(x)*(180/3.14) + math.cos(x)*(180/3.14) * (2.14**2*x)) * x**2 + x**3 + x**5 *2 - x**2 * 23
    

def cubic_spline_coefficients(x, y):
    n = len(x) - 1
    h = np.diff(x)
    print(f'Data values : {x}\n')
    print(f'Diff of Data Values {h}\n')

    alpha = [0] * (n)
    print(alpha)

    for i in range(1, n):
        alpha[i] = (3/h[i]) * (y[i+1] - y[i]) - (3/h[i-1]) * (y[i] - y[i-1])    # this is a matrix of 2nd derivatives multiplied by a constant 3
                
    print(f'Value of Alpha {alpha}\n')

    l = [1] + [0] * n
    mu = [0] * (n+1)
    z = [0] * (n+1)

    print(f'{l} : {mu} : {z}')
    for i in range(1, n):
        l[i] = 2*(x[i+1] - x[i-1]) - h[i-1]*mu[i-1]
        mu[i] = h[i] / l[i]
        z[i] = (alpha[i] - h[i-1]*z[i-1]) / l[i]
    print(f'{l} : {mu} : {z}\n')

    l[n] = 1
    z[n] = 0
    print(f'{l} : {mu} : {z}\n')

    a = y[:-1]
    b = [0] * n
    c = [0] * (n+1)
    d = [0] * n
    print(f'{a} : {b} : {c} : {d}\n')

    for j in reversed(range(n)):
        c[j] = z[j] - mu[j] * c[j+1]
        b[j] = ((y[j+1] - y[j]) / h[j]) - (h[j] * (c[j+1] + 2*c[j])) / 3
        d[j] = (c[j+1] - c[j]) / (3*h[j])
        print(f'{a} : {b} : {c} : {d}\n')

    return a, b, c[:-1], d

def cubic_spline_interpolate(x, a, b, c, d, x_val):
    for i in range(len(x) - 1):
        if x[i] <= x_val <= x[i+1]:
            dx = x_val - x[i]
            return a[i] + b[i]*dx + c[i]*dx**2 + d[i]*dx**3
    return None


x = []
y = []

for i in range(0,25):
    x.append(i)
    y.append(F(i))
    i+=90
x = np.array(x)
y = np.array(y)

print(f'{x} AND {y}')


a, b, c, d = cubic_spline_coefficients(x, y)


x_fine = np.linspace(x[0], x[-1], 500)
y_fine = [cubic_spline_interpolate(x, a, b, c, d, xi) for xi in x_fine]


plt.figure(figsize=(8, 5))
plt.plot(x, y, 'o', label='Data Points')
plt.plot(x_fine, y_fine, '-', label='Cubic Spline')
plt.title('Cubic Spline Interpolation (Algorithm Implementation)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()