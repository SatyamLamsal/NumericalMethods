import numpy as np
import matplotlib.pyplot as plt

def least_squares_fit(x, y):

    n = len(x)
    if n != len(y):
        raise ValueError("x and y must have the same length.")

    x = np.array(x)
    y = np.array(y)

    # Calculate means
    x_mean = np.mean(x)
    y_mean = np.mean(y)

    # Calculate coefficients
    m = np.sum((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean)**2)
    b = y_mean - m * x_mean

    return m, b

def plot_data_and_fit(x, y, m, b):
    """
    Plots the original data points and the fitted line.
    """
    plt.scatter(x, y, color='blue', label='Data Points')
    plt.plot(x, m * np.array(x) + b, color='red', label=f'Best Fit Line: y = {m:.2f}x + {b:.2f}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Least Squares Linear Fit')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    x = [1, 2, 3, 4, 5,6,7,8]
    y = [2, 4, 5, 4, 5,6,7,8]

    m, b = least_squares_fit(x, y)
    print(f"Slope (m): {m}")
    print(f"Intercept (b): {b}")
    plot_data_and_fit(x, y, m, b)
