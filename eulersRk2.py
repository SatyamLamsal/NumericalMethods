import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return x            #You can change this to any function f(x, y)

def RK2(x0, x1, y0, h=0.2):
    DataX = []
    DataY = []
    x = x0
    y = y0
    while x <= x1:
        DataX.append(x)
        DataY.append(y)
        K1 = h * f(x, y)
        K2 = h * f(x + h, y + K1)
        y = y + (K1 + K2) / 2
        x = x + h
    return np.array(DataX), np.array(DataY)

# Example usage for Euler's RK2 method:
DataX, DataY = RK2(0, 10, 1, 0.2)

plt.plot(DataX, DataY, marker='o')
plt.xlabel('x')
plt.ylabel('y')
plt.title("Euler's RK2 Method Approximation")
plt.grid(True)
plt.show()