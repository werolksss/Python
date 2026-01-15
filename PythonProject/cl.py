# класс student представляет студента университета
# атрибуты: имя, возраст, курс, средний балл, id студенческого билета

class Student:
    def __init__(self, name, age, course, gpa, student_id):

        # инициализация студента с проверкой корректности данных
        self.name = name
        self.age = age

        # проверка корректности курса (1-5)
        if 1 <= course <= 5:
            self.course = course
        else:
            self.course = 1
            print(f"Ошибка: курс {course} некорректен. установлен курс 1.")

        # проверка корректности gpa (0-5)
        if 0 <= gpa <= 5:
            self.gpa = gpa
        else:
            self.gpa = 0
            print(f"Ошибка: GPA {gpa} некорректен. установлен GPA 0.")

        self.student_id = student_id

    def increase_course(self):

        # увеличивает курс студента на 1, если текущий курс меньше 5
        if self.course < 5:
            self.course += 1
            print(f"{self.name}: курс увеличен до {self.course}")
        else:
            print(f"{self.name}: уже на максимальном курсе (5)")

    def update_gpa(self, new_gpa):

        # обновляет средний балл студента с проверкой корректности (0-5)
        if 0 <= new_gpa <= 5:
            self.gpa = new_gpa
            print(f"{self.name}: GPA обновлен до {new_gpa}")
        else:
            print(f"Ошибка: GPA должен быть от 0 до 5")

    def __str__(self):

        # возвращает строковое представление студента
        return f"Студент {self.name}, курс {self.course}, GPA {self.gpa}, ID {self.student_id}"

# класс book представляет книгу в библиотеке
# атрибуты: название, автор, год издания, isbn, количество страниц, статус доступности

class Book:
    def __init__(self, title, author, year, isbn, pages):

        # инициализация книги с проверкой корректности данных
        self.title = title
        self.author = author

        # проверка корректности года издания
        if year > 0:
            self.year = year
        else:
            self.year = 2024
            print(f"Ошибка: год {year} некорректен. установлен 2024.")

        self.isbn = isbn

        # проверка корректности количества страниц
        if pages > 0:
            self.pages = pages
        else:
            self.pages = 1
            print(f"Ошибка: количество страниц {pages} некорректно. установлено 1.")

        self.available = True

    def borrow_book(self):

        # отмечает книгу как взятую, если она доступна
        if self.available:
            self.available = False
            print(f'Книга "{self.title}" взята')
        else:
            print(f'Книга "{self.title}" уже взята')

    def return_book(self):

        # отмечает книгу как возвращенную, если она была взята
        if not self.available:
            self.available = True
            print(f'Книга "{self.title}" возвращена')
        else:
            print(f'Книга "{self.title}" уже доступна')

    def __str__(self):

        # возвращает строковое представление книги
        status = "доступна" if self.available else "взята"
        return f'Книга "{self.title}", автор {self.author}, {status}'

# класс product представляет товар в магазине
# атрибуты: название, цена, категория, количество, артикул

class Product:
    def __init__(self, name, price, category, quantity, sku):

        # инициализация товара с проверкой корректности данных
        self.name = name

        # проверка корректности цены
        if price > 0:
            self.price = price
        else:
            self.price = 0
            print(f"Ошибка: цена {price} некорректна. установлена 0.")

        self.category = category

        # проверка корректности количества
        if quantity >= 0:
            self.quantity = quantity
        else:
            self.quantity = 0
            print(f"Ошибка: количество {quantity} некорректно. установлено 0.")

        self.sku = sku

    def sell(self, amount):

        # продает указанное количество товара, если его достаточно
        if amount > 0:
            if self.quantity >= amount:
                self.quantity -= amount
                print(f"Продано {amount} шт. товара '{self.name}'")
            else:
                print(f"Недостаточно товара. осталось: {self.quantity}")
        else:
            print(f"Ошибка: количество для продажи должно быть положительным")

    def restock(self, amount):

        # пополняет запас товара на указанное количество
        if amount > 0:
            self.quantity += amount
            print(f"Товар '{self.name}' пополнен на {amount} шт.")
        else:
            print(f"Ошибка: количество для пополнения должно быть положительным")

    def __str__(self):

        # возвращает строковое представление товара
        return f"Товар {self.name}, цена {self.price}, остаток {self.quantity}"

# создание объектов
student1 = Student("Иван Петров", 19, 1, 4.2, "ST001")
student2 = Student("Мария Сидорова", 20, 2, 4.7, "ST002")

book1 = Book("Преступление и наказание", "Фёдор Достоевский", 1866, "978-5-17-090879-1", 608)
book2 = Book("Мастер и Маргарита", "Михаил Булгаков", 1967, "978-5-389-06204-3", 480)

product1 = Product("Ноутбук", 75000.0, "Электроника", 10, "NB-001")
product2 = Product("Кофеварка", 12000.0, "Бытовая техника", 5, "CF-002")

# тестирование
print("Тестирование Student")
print(student1)
student1.increase_course()
student1.update_gpa(4.5)
student1.update_gpa(6.0)  # некорректный gpa
print(student1)

print("\nТестирование Book")
print(book1)
book1.borrow_book()
book1.borrow_book()  # попытка взять уже взятую книгу
book1.return_book()
book1.return_book()  # попытка вернуть уже доступную книгу
print(book1)

print("\nТестирование Product")
print(product1)
product1.sell(3)
product1.sell(10)  # попытка продать больше, чем есть
product1.restock(5)
product1.sell(-2)  # некорректное количество
print(product1)