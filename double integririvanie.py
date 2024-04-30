import numpy as np

def double_integral(f, a, b, c, d, n=100, m=100):


# Computes the double integral of a function f over the rectangle [a, b] x [c, d]
# using the double trapezoidal rule.

# Args:
# f: The function to integrate.
# a: The lower bound of the integration interval in the x-direction.
# b: The upper bound of the integration interval in the x-direction.
# c: The lower bound of the integration interval in the y-direction.
# d: The upper bound of the integration interval in the y-direction.
# n: The number of subintervals in the x-direction.
# m: The number of subintervals in the y-direction.

# Returns:
# The approximate value of the double integral.


    # Create a meshgrid of the points in the integration interval.
    x = np.linspace(a, b, n + 1)
    y = np.linspace(c, d, m + 1)
    X, Y = np.meshgrid(x, y)

    # Evaluate the function at the meshgrid points.
    Z = f(X, Y)

    # Compute the double integral using the trapezoidal rule.
    dx = (b - a) / n
    dy = (d - c) / m
    integral = dx * dy * np.sum(Z)

    return integral

# Example usage
f = lambda x, y: x**2 + y**2
a = 0
b = 1
c = 0
d = 1
n = 100
m = 100
result = double_integral(f, a, b, c, d, n, m)
print(result)
