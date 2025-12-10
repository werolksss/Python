# Интерполяция по Лагранжу и Ньютону
def lagrange_interpolation(x_points, y_points, x):
    n = len(x_points)
    result = 0.0
    for i in range(n):
        term = y_points[i]
        for j in range(n):
            if i != j:
                term *= (x - x_points[j]) / (x_points[i] - x_points[j])
        result += term
    return result

def newton_interpolation(x_points, y_points, x):
    n = len(x_points)
    table = [[0] * n for _ in range(n)]
    for i in range(n):
        table[i][0] = y_points[i]

    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = (table[i + 1][j - 1] - table[i][j - 1]) / (x_points[i + j] - x_points[i])

    result = table[0][0]
    product = 1.0
    for j in range(1, n):
        product *= (x - x_points[j - 1])
        result += table[0][j] * product
    return result

def print_finite_differences(x_points, y_points):
    n = len(x_points)
    table = [[0] * n for _ in range(n)]
    for i in range(n):
        table[i][0] = y_points[i]

    print("Таблица конечных разностей:")
    print("x\t\tf(x)\t\tΔ1\t\tΔ2\t\tΔ3\t\tΔ4\t\tΔ5\t\tΔ6")

    for j in range(1, n):
        for i in range(n - j):
            table[i][j] = table[i + 1][j - 1] - table[i][j - 1]

    for i in range(n):
        row = f"{x_points[i]:.4f}\t{y_points[i]:.6f}"
        for j in range(1, min(7, n - i)):
            row += f"\t{table[i][j]:.6f}"
        print(row)

# 2
print("Задание 2: Интерполяция по Лагранжу")

x_vals = [0.27, 0.93, 1.46, 2.11, 2.87]
y_vals = [2.60, 2.43, 2.06, 0.25, -2.60]

points_to_calc = [1.02, 0.65, 1.28]
for point in points_to_calc:
    value = lagrange_interpolation(x_vals, y_vals, point)
    print(f"L({point:.2f}) = {value:.4f}")

#5
print("Задание 5: Проверка значений")

x_task5 = [1.25, 1.30, 1.35, 1.40, 1.45, 1.50]
y_task5 = [1.60, 1.71, 1.81, 1.88, 1.94, 1.98]

check_points = [1.30, 1.45]
for point in check_points:
    value = lagrange_interpolation(x_task5, y_task5, point)
    print(f"L({point:.2f}) = {value:.6f}")

# 7
print("Задание 7: Натуральный логарифм")

x_log = [1.05, 1.06, 1.07, 1.08, 1.09, 1.10, 1.11]
y_log = [0.04879, 0.058269, 0.067659, 0.076961, 0.086178, 0.09531, 0.10436]

print_finite_differences(x_log, y_log)

print("\nИнтерполяция по Ньютону:")
points_to_find = [1.065, 1.083]
for point in points_to_find:
    value_newton = newton_interpolation(x_log, y_log, point)
    value_lagrange = lagrange_interpolation(x_log, y_log, point)

    import math

    real_value = math.log(point)

    print(f"\nx = {point:.3f}:")
    print(f"  Ньютон:  {value_newton:.6f}")
    print(f"  Лагранж: {value_lagrange:.6f}")
    print(f"  Реальное: {real_value:.6f}")
    print(f"  Погрешность: {abs(value_newton - real_value):.6f}")

# проверка L1(x)
print("Проверка L1(x) = 2x - 1.28")

x_test = [0.48, 0.83]
y_test = [-0.32, 0.38]
for i in range(2):
    L1_val = 2 * x_test[i] - 1.28
    print(f"x={x_test[i]}: {L1_val:.2f} (ожидается {y_test[i]:.2f})")

print("программа завершена")
