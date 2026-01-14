def min_refuels(distances, max_distance, total_distance):
    """
    distances - список расстояний между заправками
    max_distance - расстояние на полном баке
    total_distance - общее расстояние от петербурга до москвы
    """
    current_position = 0
    current_fuel = max_distance
    refuels = [0]  # начинаем с заправки в петербурге (индекс 0)
    refuel_count = 0

    # проверяем, можем ли сразу доехать до москвы
    if sum(distances) <= max_distance:
        return [0, len(distances)]  # заправляемся только в начале

    i = 0
    while i < len(distances):
        # проверяем, можем ли доехать до следующей заправки
        if distances[i] > current_fuel:
            # ищем самую дальнюю заправку, до которой можем доехать
            # в реальном алгоритме нужно пройти назад от текущей позиции
            # но в упрощенном варианте просто заправляемся на предыдущей
            if i > 0:
                refuels.append(i)
                refuel_count += 1
                current_fuel = max_distance
                continue
            else:
                return "невозможно доехать: расстояние до следующей заправки слишком велико"

        # едем до следующей заправки
        current_fuel -= distances[i]
        current_position += distances[i]
        i += 1

    # проверяем, доехали ли до москвы
    if current_position + current_fuel >= total_distance:
        return refuels
    else:
        return refuels + [len(distances)]  # добавляем заправку в москве


# пример использования:
distances = [40, 80, 60, 30, 50, 20, 40]  # расстояния между 8 заправками
max_distance = 100  # машина может проехать на полном баке
total_distance = sum(distances)  # 320 км

result = min_refuels(distances, max_distance, total_distance)
print("номера заправок для заправки:", result)
print("минимальное количество заправок:", len(result) - 1)  # не считая начальную