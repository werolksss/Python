def max_meetings(meetings, min_break=0):
    """
    meetings - список кортежей (начало, конец)
    min_break - минимальный перерыв между заседаниями
    """
    # сортируем по времени окончания
    sorted_meetings = sorted(meetings, key=lambda x: x[1])

    selected = []
    last_end = -float('inf')

    for meeting in sorted_meetings:
        start, end = meeting

        # проверяем, можно ли посетить это заседание
        if start >= last_end + min_break:
            selected.append(meeting)
            last_end = end

    return selected


# пример использования:
meetings = [
    (9, 10),  # заседание 1: 9:00-10:00
    (10, 12),  # заседание 2: 10:00-12:00
    (11, 13),  # заседание 3: 11:00-13:00
    (14, 16),  # заседание 4: 14:00-16:00
    (15, 17),  # заседание 5: 15:00-17:00
    (16, 18)  # заседание 6: 16:00-18:00
]

min_break = 0.5  # 30 минут перерыва между заседаниями

result = max_meetings(meetings, min_break)
print("максимальное количество заседаний:", len(result))
print("расписание заседаний:")
for i, (start, end) in enumerate(result, 1):
    print(f"{i}. {start}:00 - {end}:00")