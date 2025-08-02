import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return x   

def RK4(x0, x1, y0, h=0.2):
    DataX = []
    DataY = []
    x = x0
    y = y0
    while x < x1 + 1e-9:  # Small tolerance to include x1
        DataX.append(x)
        DataY.append(y)
        K1 = h * f(x, y)
        K2 = h * f(x + h/2, y + K1/2)
        K3 = h * f(x + h/2, y + K2/2)
        K4 = h * f(x + h, y + K3)
        y = y + (K1 + 2*K2 + 2*K3 + K4) / 6
        x = x + h
    return np.array(DataX), np.array(DataY)

# Example usage:
DataX, DataY = RK4(0, 10, 1, 0.2)

plt.plot(DataX, DataY, marker='o')
plt.xlabel('x')
plt.ylabel('y')
plt.title("RK4 Method Approximation")
plt.grid(True)
plt.show()
