#Интегрирование с двойным пересчеч
def integrate_double_step(f, a, b, h, tol):
    def single_step(f, a, b, h):
        x = a
        integral = 0
        while x < b:
            integral += h * f(x + 0.5 * h)
            x += h
        return integral
    
    integral1 = single_step(f, a, b, h)
    integral2 = single_step(f, a, b, h/2)
    error = abs(integral1 - integral2)
    
    if error < tol * 9:
        return integral2 + (abs(integral2 - integral1)/3)
    else:
        return integrate_double_step(f, a, b, h/2, tol * 9)

# Пример использования
def f(x):
    return x**2

a = 0
b = 2
h = 0.1
tol = 0.00001
integral_result = integrate_double_step(f, a, b, h, tol)
print("Результат интегрирования с точностью 0.00001:", integral_result)
