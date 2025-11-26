import math
def newton_method(f, df, x0, eps=1e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        # проверка, что производная не слишком мала
        if abs(dfx) < 1e-12:
            break
        # итерационная формула ньютона
        x_new = x - fx / dfx
        # проверка достижения точности
        if abs(x_new - x) < eps:
            return x_new, i + 1
        x = x_new
    return x, max_iter

def chord_method(f, a, b, eps=1e-6, max_iter=100):
    for i in range(max_iter):
        fa, fb = f(a), f(b)
        # итерационная формула метода хорд
        x = a - fa * (b - a) / (fb - fa)
        fx = f(x)
        # проверка достижения точности
        if abs(fx) < eps:
            return x, i + 1
        # выбор нового интервала
        if fa * fx < 0:
            b = x
        else:
            a = x
    return x, max_iter

def combined_method(f, df, a, b, eps=1e-6, max_iter=100):
    for i in range(max_iter):
        # метод хорд (уточнение с левой стороны)
        x_chord = a - f(a) * (b - a) / (f(b) - f(a))
        # метод ньютона (уточнение с правой стороны)
        x_newton = a - f(a) / df(a)
        # проверка достижения точности
        if abs(x_chord - x_newton) < eps:
            return (x_chord + x_newton) / 2, i + 1
        # сужение интервала
        a, b = x_chord, x_newton
    return (a + b) / 2, max_iter

# пример использования методов
if __name__ == "__main__":
    def f(x):
        return 2 * x - 5 * math.log(x) - 3
    def df(x):
        return 2 - 5 / x

    # решение методом ньютона
    root1, iter1 = newton_method(f, df, 1.0)
    print(f"метод касательных: корень = {root1:.6f}, итераций = {iter1}")

    # решение методом хорд
    root2, iter2 = chord_method(f, 0.5, 1.0)
    print(f"метод хорд: корень = {root2:.6f}, итераций = {iter2}")

    # решение комбинированным методом
    root3, iter3 = combined_method(f, df, 0.5, 1.0)
    print(f"комбинированный метод: корень = {root3:.6f}, итераций = {iter3}")