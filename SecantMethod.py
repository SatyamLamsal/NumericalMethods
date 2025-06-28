#Secant Method 

def f(x):
    return x**2 - 4*x + 4

def secant_method(x0, x1, tol=1e-6, max_iter=100):
    print(f"{'Iter':<5}{'x0':<15}{'x1':<15}{'x2':<15}{'f(x2)':<15}")
    
    for i in range(max_iter):
        f_x0 = f(x0)
        f_x1 = f(x1)

        if f_x1 - f_x0 == 0:
            print("Division by zero error.")
            return None

        x2 = (x0*f(x1) - x1*f(x0))/(f_x1 - f_x0)
        print(f"{i+1:<5}{x0:<15.8f}{x1:<15.8f}{x2:<15.8f}{f(x2):<15.8f}")

        if abs(x2 - x1) < tol:
            print(f"\nConverged to root: {x2:.8f}")
            return x2

        x0, x1 = x1, x2

    print("Method did not converge within the maximum number of iterations.")
    return None

secant_method(1, 2)

