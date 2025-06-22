import numpy as np
import matplotlib.pyplot as plt

def polynomial_fit_matrix_method(x, y, degree):
    """
    Fit a polynomial of given degree to data using the normal equation (matrix method).
    Returns the coefficients of the fitted polynomial.
    """
    x = np.array(x)
    y = np.array(y)

    # Construct the Vandermonde matrix
    X = np.vander(x, N=degree + 1, increasing=True)

    # Normal equation: (X^T X) a = X^T y
    XT_X = np.dot(X.T, X)
    XT_y = np.dot(X.T, y)

    # Solve for coefficients
    coefficients = np.linalg.solve(XT_X, XT_y)
    return coefficients

def display_polynomial(coefficients):
    """
    Returns the string representation of the polynomial.
    """
    terms = []
    for i, coef in enumerate(coefficients):
        term = f"{coef:.4f}"
        if i == 1:
            term += "x"
        elif i >= 2:
            term += f"x^{i}"
        terms.append(term)
    return " + ".join(terms)

def plot_polynomial_fit(x, y, coefficients):
    """
    Plot the original data and the fitted polynomial curve.
    """
    x_vals = np.linspace(min(x), max(x), 500)
    y_vals = np.polynomial.polynomial.polyval(x_vals, coefficients)

    plt.scatter(x, y, color='blue', label='Data Points')
    plt.plot(x_vals, y_vals, color='red', label='Fitted Polynomial')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Polynomial Fit')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    # Sample data
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8 ]
    y = [0.5, 1.4,  25, 36, 49, 64,4, 9, 16]

    degree = int(input("Enter the degree of the polynomial to fit: "))

    coefficients = polynomial_fit_matrix_method(x, y, degree)
    poly_str = display_polynomial(coefficients)
    
    print("\nFitted Polynomial:")
    print("f(x) =", poly_str)

    plot_polynomial_fit(x, y, coefficients)

if __name__ == "__main__":
    main()
