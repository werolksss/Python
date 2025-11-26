import math
def root_separation_algorithm(f, a, b, h):
# алгоритм отделения корней уравнения F(x) = 0
    x1 = a
    x2 = a + h
    y1 = f(x1)

    while x2 <= b:
        y2 = f(x2)

        if y1 * y2 < 0:
            print(f"Корень найден в интервале: [{x1:.6f}, {x2:.6f}]")

        x1 = x2
        x2 = x1 + h
        y1 = y2


def bisection_method_algorithm(f, a, b, epsilon):
# метод половинного деления
    while (b - a) / 2 > epsilon:
        c = (a + b) / 2

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    x = (a + b) / 2
    return x


def simple_iteration_method_algorithm(phi, x0, epsilon):
# метод простых итераций
    x_prev = x0
    x_next = phi(x_prev)

    while abs(x_next - x_prev) > epsilon:
        x_prev = x_next
        x_next = phi(x_prev)

    x = x_next
    return x
# Пример использования алгоритмов
if __name__ == "__main__":
    # Пример функции: x*sin(x) - 1 = 0
    def example_f(x):
        return x * math.sin(x) - 1
    def example_phi(x):
        return x - 0.4 * (x * math.sin(x) - 1)

    print("алгоритм отделения корней")
    root_separation_algorithm(example_f, 0, 2, 0.1)

    print("\nметод половинного деления")
    root_bisect = bisection_method_algorithm(example_f, 1.0, 1.2, 1e-4)
    print(f"Найденный корень: {root_bisect:.6f}")

    print("\nметод простых итераций")
    root_iter = simple_iteration_method_algorithm(example_phi, 1.1, 1e-5)
    print(f"Найденный корень: {root_iter:.6f}")