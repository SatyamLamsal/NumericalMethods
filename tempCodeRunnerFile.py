import numpy as np
import matplotlib.pyplot as plt

<<<<<<< HEAD
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
=======
def least_squares_fit_for_exponential(x, y):
    x = np.array(x)
    y = np.array(y)

    if any(y <= 0):
        raise ValueError("All y values must be positive for logarithmic transformation.")

    log_y = np.log(y)

    # Perform linear regression on x and log(y)
    n = len(x)
    x_mean = np.mean(x)
    log_y_mean = np.mean(log_y)

    b = np.sum((x - x_mean) * (log_y - log_y_mean)) / np.sum((x - x_mean) ** 2)
    log_a = log_y_mean - b * x_mean
    a = np.exp(log_a)

    return a, b  # Returns a and b where y = a * e^(b * x)

def plot_data_and_fit(x, y, a, b):
    x = np.array(x)
    y_fit = a * np.exp(b * x)

    plt.scatter(x, y, color='blue', label='Data Points')
    plt.plot(x, y_fit, color='red', label=f'Best Fit: y = {a:.2f}e^({b:.2f}x)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Exponential Fit')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    y = [0.5, 1.4, 4, 9, 16, 25, 36, 49, 64]  # Must be all > 0

    a, b = least_squares_fit_for_exponential(x, y)
    plot_data_and_fit(x, y, a, b)
>>>>>>> master
