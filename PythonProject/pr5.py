import math


def triangle_type_by_sides(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 0, "Ошибка: все стороны должны быть положительными числами"

    if a + b <= c or a + c <= b or b + c <= a:
        return 0, "Ошибка: не выполняется неравенство треугольника"

    if a == b == c:
        return 3, "Равносторонний треугольник"
    elif a == b or a == c or b == c:
        return 2, "Равнобедренный треугольник"
    else:
        return 1, "Разносторонний треугольник"


def triangle_type_by_angles(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 0, "Ошибка: все стороны должны быть положительными числами"

    if a + b <= c or a + c <= b or b + c <= a:
        return 0, "Ошибка: не выполняется неравенство треугольника"

    sides = sorted([a, b, c])
    a_sq = sides[0] ** 2
    b_sq = sides[1] ** 2
    c_sq = sides[2] ** 2

    if a_sq + b_sq > c_sq:
        return 1, "Остроугольный треугольник"
    elif a_sq + b_sq < c_sq:
        return 2, "Тупоугольный треугольник"
    else:
        return 3, "Прямоугольный треугольник"


def calculate_area(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 0, "Ошибка: невозможно вычислить площадь"

    if a + b <= c or a + c <= b or b + c <= a:
        return 0, "Ошибка: невозможно вычислить площадь"

    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return area, f"Площадь треугольника: {area:.2f}"


def main():
    print("Определение типа треугольника")
    print("Введите длины сторон треугольника:")

    a = float(input("Сторона A: "))
    b = float(input("Сторона B: "))
    c = float(input("Сторона C: "))

    type_sides, message_sides = triangle_type_by_sides(a, b, c)
    print(f"Тип по сторонам: {message_sides}")

    type_angles, message_angles = triangle_type_by_angles(a, b, c)
    print(f"Тип по углам: {message_angles}")

    area, message_area = calculate_area(a, b, c)
    print(message_area)


if __name__ == "__main__":
    main()