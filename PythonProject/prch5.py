import numpy as np
#
#
# def simple_iteration(A, b, eps=1e-4, max_iter=1000):
#     """
#     A - матрица коэффициентов (n x n)
#     b - вектор правых частей
#     Метод простых итераций: приводим систему к виду x = B*x + d
#     """
#     n = len(b)
#     B = np.zeros((n, n))
#     d = np.zeros(n)
#
#     # Преобразование: x_i = (b_i - sum_{j!=i} A[i][j]*x_j) / A[i][i]
#     for i in range(n):
#         d[i] = b[i] / A[i][i]
#         for j in range(n):
#             if i != j:
#                 B[i][j] = -A[i][j] / A[i][i]
#
#     x = np.zeros(n)
#     for it in range(max_iter):
#         x_new = B @ x + d
#         if np.linalg.norm(x_new - x, ord=np.inf) < eps:
#             print(f"Сошлось за {it + 1} итераций")
#             return x_new
#         x = x_new
#     print("Достигнут максимум итераций")
#     return x
#
#
# # Тест для системы из задания 3(a)
# A = np.array([
#     [14.95, -0.68, -0.86],
#     [0.516, -1.38, -0.53],
#     [-2.484, 8.18, 8.68]
# ])
#
# b = np.array([0.76, -69.69, 4.71])
#
# sol = simple_iteration(A, b, eps=1e-6)
# print("Решение:", np.round(sol, 4))

def seidel_method(A, b, eps=1e-4, max_iter=1000):
    n = len(b)
    x = np.zeros(n)

    for it in range(max_iter):
        x_new = x.copy()
        for i in range(n):
            s1 = sum(A[i][j] * x_new[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - s1 - s2) / A[i][i]

        if np.linalg.norm(x_new - x, ord=np.inf) < eps:
            print(f"Зейдель сошёлся за {it + 1} итераций")
            return x_new
        x = x_new
    print("Достигнут максимум итераций")
    return x


# Пример для задания 5(a)
A = np.array([
    [22.52, -4.62, -1.41],
    [-5.10, -2.37, 4.58],
    [-4.68, -1.91, 3.85]
], dtype=float)
b = np.array([0.53, -78.58, 14.5], dtype=float)

sol_s = seidel_method(A, b, eps=1e-6)
print("Решение Зейделя:", np.round(sol_s, 4))