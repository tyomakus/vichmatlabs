import math


def golden_section(f, a, b, tol=1e-6):
    GRat = (math.sqrt(5) + 1) / 2
    x1 = b - (b - a) / GRat
    x2 = a + (b - a) / GRat

    f1 = f(x1)
    f2 = f(x2)

    while abs(b - a) > tol:
        if f1 < f2:
            b = x2
            x2 = x1
            x1 = b - (b - a) / GRat
            f2 = f1
            f1 = f(x1)
        else:
            a = x1
            x1 = x2
            x2 = a + (b - a) / GRat
            f1 = f2
            f2 = f(x2)

    return (a + b) / 2


# Пример использования
f = lambda x: (x - 2) ** 2
a = 0
b = 5

result = golden_section(f, a, b)
print("Минимум функции в точке:", result, "значение функции:", f(result))