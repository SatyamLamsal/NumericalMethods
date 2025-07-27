import numpy as np
import matplotlib.pyplot as plt

def polynomial_fit_matrix_method(x, y, degree):
    x = np.array(x)
    y = np.array(y)
    X = np.vander(x, N=degree + 1, increasing=True)
    XT_X = np.dot(X.T, X)
    XT_y = np.dot(X.T, y)

    coefficients = np.linalg.solve(XT_X, XT_y)
    return coefficients

def display_polynomial(coefficients):

    terms = []
    for i, coef in enumerate(coefficients):
        term = f"{coef:.4f}"
        if i == 1:
            term += "x"
        elif i >= 2:
            term += f"x^{i}"
        terms.append(term)
    return " + ".join(terms)

def plot_polynomial_fit(x, y, coefficients, degree):

    x_vals = np.linspace(min(x), max(x), 500)
    y_vals = np.polynomial.polynomial.polyval(x_vals, coefficients)

    plt.scatter(x, y, color='blue', label='Data Points')
    plt.plot(x_vals, y_vals, color='red', label='Fitted Polynomial')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Polynomial Fit : Degree {degree}')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():

    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y = [1, 2.8, 6.1, 11.9, 20.2, 31.1, 44.7, 61.0, 80.1, 102.9, 128.4]

    degree = int(input("Enter the degree of the polynomial to fit: "))

    coefficients = polynomial_fit_matrix_method(x, y, degree)
    poly_str = display_polynomial(coefficients)
    
    print("\nFitted Polynomial:")
    print("f(x) =", poly_str)

    plot_polynomial_fit(x, y, coefficients,degree)

if __name__ == "__main__":
    main()
