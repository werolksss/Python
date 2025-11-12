# Исправленный buggy_code.py
def calculate_discount(price, age, is_student):
    """
    Расчет скидки на товар
    """
    discount = 0

    # Скидка по возрасту - добавлены граничные значения
    if age < 18:
        discount += 10
    elif age >= 60:  #изменено на >= 60
        discount += 15

    # Скидка для студентов
    if is_student == True:
        discount += 5

    # Максимальная скидка не более 25%
    if discount > 25:
        discount = 25

    final_price = price - (price * discount / 100)
    return final_price


def validate_password(password):
    """
    Проверка надежности пароля
    """
    if len(password) < 6:
        return "Слишком короткий"

    has_upper = False
    has_lower = False
    has_digit = False

    for char in password:
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True
        if char.isdigit():
            has_digit = True

    # добавлена явная проверка has_lower
    if has_upper and has_lower and has_digit:
        return "Надежный"
    else:
        return "Ненадежный"


def get_temperature_status(temp):
    """
    Определение статуса температуры
    """
    #исправлены границы диапазонов
    if temp <= 0:
        return "Лед"
    elif temp < 10:  # было < 10, оставляем
        return "Холодно"
    elif temp < 20:  # было < 20, оставляем
        return "Прохладно"
    elif temp < 30:  #было < 30, оставляем
        return "Тепло"
    else:
        return "Жарко"