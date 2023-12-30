def newton_raphson(f, f_prime, x0, tol=1e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        if abs(fx) < tol:
            return x
        x -= fx / f_prime(x)
    raise ValueError("Newton-Raphson method did not converge")

def find_square_root(c):
    def f(x):
        return x**2 - c
    def f_prime(x):
        return 2 * x
    initial_guess = c / 2.0
    root = newton_raphson(f, f_prime, initial_guess)
    return root

number_to_find_square_root = 3
square_root = find_square_root(number_to_find_square_root)
print(f"The square root of {number_to_find_square_root} is approximately: {square_root}")
