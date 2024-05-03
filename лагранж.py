import numpy as np
from scipy.integrate import odeint

def lagrange_method(dy_dx, x0, y0, x_end, h):

    # Solve a differential equation using Lagrange's method.

    # Parameters:
    # dy_dx : function
    # The function representing the differential equation dy/dx = f(x, y).
    # x0 : float
    # Initial value of x.
    # y0 : float
    # Initial value of y at x0.
    # x_end : float
    # Final value of x.
    # h : float
    # Step size.

    # Returns:
    # x_values : array
    # Array containing the x values.
    # y_values : array
    # Array containing the corresponding y values.

    x_values = np.arange(x0, x_end + h, h)
    y_values = [y0]

    for i in range(1, len(x_values)):
        x_i = x_values[i]
        y_i = y_values[-1]
        y_new = y_i + h * dy_dx(x_i, y_i)
        y_values.append(y_new)

    return x_values, np.array(y_values)

# Example usage:
def dy_dx(x, y):
    return x * y
x0 = 0
y0 = 1
x_end = 1
h = 0.1

x_values, y_values = lagrange_method(dy_dx, x0, y0, x_end, h)
print("x values:", x_values)
print("y values:", y_values)