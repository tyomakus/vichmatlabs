import numpy as np

# Функция для вычисления значения уравнения
def eval_equation(equation, **variables):
    return eval(equation, {**variables})

# Метод Гаусса-Зейделя для решения линейных систем
def gauss_seidel(A, b, tolerance=1e-10, max_iterations=100):
    x = np.zeros_like(b)
    for _ in range(max_iterations):
        x_new = np.copy(x)
        for i in range(A.shape[0]):
            s1 = np.dot(A[i, :i], x_new[:i])
            s2 = np.dot(A[i, i + 1:], x[i + 1:])
            x_new[i] = (b[i] - s1 - s2) / A[i, i]
        if np.allclose(x, x_new, atol=tolerance):
            return x_new
        x = x_new
    return x

# Метод Ньютона для решения нелинейных систем
def newton_method(equation1, equation2, jacobian, initial_guess, tolerance=1e-10, max_iterations=100):
    x, y = initial_guess
    for _ in range(max_iterations):
        J = jacobian(x, y)
        F = np.array([-eval_equation(equation1, x=x, y=y), -eval_equation(equation2, x=x, y=y)])
        delta = gauss_seidel(J, F, tolerance)
        x += delta[0]
        y += delta[1]
        if np.linalg.norm(delta) < tolerance:
            return x, y
    return x, y

# Начальное приближение
initial_guess = (1, 1)

# Уравнения в виде строк
equation1 = "x**2 + y**3 - 4"
equation2 = "x/y - 2"

# Якобиан системы уравнений
def jacobian(x, y):
    return np.array([[2*x, 3*y**2], [1/y, -x/y**2]])

# Решение системы
solution = newton_method(equation1, equation2, jacobian, initial_guess)
print(f'Решение системы: x = {solution[0]}, y = {solution[1]}')