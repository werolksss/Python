# часть 1:
class Human:
    # 2 статические поля
    default_name = "Иван"
    default_age = 30

    # статический метод default_info()
    @staticmethod
    def default_info():
        print(f"default_name: {Human.default_name}")
        print(f"default_age: {Human.default_age}")

    # конструктор __init__()
    def __init__(self, name=default_name, age=default_age):
        # Публичные свойства
        self.name = name
        self.age = age
        # Приватные свойства
        self.__money = 0
        self.__house = None

    # метод info()
    def info(self):
        print(f"Имя: {self.name}")
        print(f"Возраст: {self.age}")
        print(f"Дом: {self.__house}")
        print(f"Деньги: {self.__money}")

    # метод earn_money()
    def earn_money(self, amount):
        self.__money += amount
        print(f"Заработано {amount}. Теперь денег: {self.__money}")

    # приватный метод __make_deal()
    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house
        print(f"Куплен дом за {price}. Осталось денег: {self.__money}")

    # метод buy_house()
    def buy_house(self, house, discount):
        final_price = house.final_price(discount)
        if self.__money >= final_price:
            self.__make_deal(house, final_price)
        else:
            print(f"Недостаточно денег! Нужно {final_price}, а есть {self.__money}")

# часть 2
class House:
    # конструктор __init__()
    def __init__(self, area, price):
        self._area = area
        self._price = price

    # метод final_price()
    def final_price(self, discount):
        return self._price * (1 - discount / 100)

# часть 3
class SmallHouse(House):
    # переопределение __init__()
    def __init__(self, price):
        # Создаем объект с площадью 40 m²
        super().__init__(area=40, price=price)

# часть 4
# вызов справочного метода default_info() для класса Human
print("1. Статическая информация:")
Human.default_info()
print()

# создание объекта класса Human
person = Human("Анна", 25)
print("2. Создан объект Human")
print()

# вывод справочной информации о созданном объекте
print("3. Информация о человеке:")
person.info()
print()

# создание объекта класса SmallHouse
small_house = SmallHouse(price=50000)
print("4. Создан объект SmallHouse")
print()

# попытка купить созданный дом
print("5. Попытка купить дом (скидка 10%):")
person.buy_house(small_house, discount=10)
print()

# поправление финансового положения объекта
print("6. Заработок денег:")
person.earn_money(60000)
print()

# снова попытка купить дом
print("7. Вторая попытка купить дом (скидка 10%):")
person.buy_house(small_house, discount=10)
print()

# просмотр состояния объекта класса Human
print("8. Финальное состояние:")
person.info()