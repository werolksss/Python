import numpy as np
def gauss_elimination(A, b):
    n = len(A)
    # Создаем расширенную матрицу
    Ab = np.hstack([A.astype(float), b.astype(float).reshape(-1, 1)])
    # Прямой ход
    for i in range(n):
        # Поиск ведущего элемента
        max_row = np.argmax(np.abs(Ab[i:, i])) + i
        Ab[[i, max_row]] = Ab[[max_row, i]]

        # Нормализация строки
        Ab[i] = Ab[i] / Ab[i, i]

        # Исключение
        for j in range(i + 1, n):
            Ab[j] = Ab[j] - Ab[j, i] * Ab[i]

    # Обратный ход
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = Ab[i, -1] - np.dot(Ab[i, i + 1:n], x[i + 1:n])

    return x

def gauss_determinant(A):

    n = len(A)
    det = 1.0
    A_copy = A.astype(float).copy()

    for i in range(n):
        # Поиск ведущего элемента
        max_row = np.argmax(np.abs(A_copy[i:, i])) + i
        if max_row != i:
            A_copy[[i, max_row]] = A_copy[[max_row, i]]
            det *= -1  # Смена знака при перестановке

        if abs(A_copy[i, i]) < 1e-10:
            return 0

        det *= A_copy[i, i]

        for j in range(i + 1, n):
            factor = A_copy[j, i] / A_copy[i, i]
            A_copy[j] -= factor * A_copy[i]

    return det

def gauss_inverse(A):

    n = len(A)
    # Создаем расширенную матрицу [A|I]
    I = np.eye(n)
    AI = np.hstack([A.astype(float), I])

    # Прямой ход
    for i in range(n):
        # Поиск ведущего элемента
        max_row = np.argmax(np.abs(AI[i:, i])) + i
        AI[[i, max_row]] = AI[[max_row, i]]

        # Нормализация
        pivot = AI[i, i]
        AI[i] = AI[i] / pivot

        # Исключение
        for j in range(n):
            if j != i:
                factor = AI[j, i]
                AI[j] -= factor * AI[i]

    # Обратная матрица - правая часть
    return AI[:, n:]

if __name__ == "__main__":
    A1 = np.array([
        [5.38, -0.33, -0.24, 0.49, -0.89],
        [2.81, -0.69, -0.13, -0.55, 0.19],
        [7.60, 0.78, 0.59, -0.98, 0.72],
        [-8.44, -5.53, -4.87, 4.96, 3.61],
        [-0.61, 4.63, 4.10, -1.72, 3.71]
    ])

    b1 = np.array([4.27, -5.77, 7.70, 8.85, -6.77])

    print("Решение системы 6а:")
    solution = gauss_elimination(A1, b1)
    print(f"x = {solution}")

    residual = np.dot(A1, solution) - b1
    print(f"Невязка: {residual}")
    print(f"Максимальная невязка: {np.max(np.abs(residual))}")