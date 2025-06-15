import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return x - y


def FNF(X,Y):
    return -X*X*Y*Y


def RK2(x0,x1, y0, h=0.2, steps=75):
    DataX = np.zeros(steps)
    DataY = np.zeros(steps)

    for i in range(steps):
        DataX[i]=x0
        DataY[i]=y0
        if(x0>(x1-0.000001)):
            return DataX, DataY
        K1 = h*FNF(x0,y0)
        K2 = h * FNF(x0 + h, y0 + K1)
        x0 = x0 + h
        y0 = y0 +(K1+K2)/2
    
    return DataX, DataY

def euler(x0, y0, h=0.2, steps=15):
    DataX = np.zeros(steps)
    DataY = np.zeros(steps)
    
    for i in range(steps):
        DataX[i] = x0
        DataY[i] = y0
        y0 = y0 + h * f(x0, y0)
        x0 += h        
    return DataX, DataY

DataX, DataY = RK2(0, 10, 1, 0.2)

plt.plot(DataX, DataY, marker='o')
plt.xlabel('x')
plt.ylabel('y')
plt.title("Euler's Method Approximation")
plt.grid(True)
plt.show()
