class LibraryItem:
    __last_id = 0

    def __init__(self, title, author, year):
        self._title = title
        self._author = author
        self._year = year
        LibraryItem.__last_id += 1
        self.__item_id = LibraryItem.__last_id
        self.__is_checked_out = False

    def get_title(self):
        return self._title

    def get_author(self):
        return self._author

    def get_year(self):
        return self._year

    def get_item_id(self):
        return self.__item_id

    def get_is_checked_out(self):
        return self.__is_checked_out

    def set_is_checked_out(self, value):
        if isinstance(value, bool):
            self.__is_checked_out = value
        else:
            raise ValueError("Должно быть True или False")

    def get_info(self):
        status = "выдан" if self.__is_checked_out else "доступен"
        return f"ID: {self.__item_id}, '{self._title}', {self._author}, {self._year}, {status}"


class Book(LibraryItem):
    def __init__(self, title, author, year, genre, page_count):
        super().__init__(title, author, year)
        self.genre = genre
        self.__page_count = page_count
        if page_count < 1:
            raise ValueError("Страниц не может быть меньше 1")

    def get_page_count(self):
        return self.__page_count

    def set_page_count(self, page_count):
        if page_count < 1:
            raise ValueError("Страниц не может быть меньше 1")
        self.__page_count = page_count

    def get_info(self):
        base = super().get_info()
        return f"{base}, Книга, {self.genre}, {self.__page_count} стр."


class Magazine(LibraryItem):
    def __init__(self, title, author, year, issue_number):
        super().__init__(title, author, year)
        self._issue_number = issue_number

    def get_magazine_info(self):
        return f"Журнал: '{self._title}', Выпуск №{self._issue_number}, {self._year}"

    def get_info(self):
        base = super().get_info()
        return f"{base}, Журнал, №{self._issue_number}"


class DVD(LibraryItem):
    VALID_RATINGS = {"G", "PG", "PG-13", "R", "NC-17"}

    def __init__(self, title, author, year, duration, rating):
        super().__init__(title, author, year)
        self.set_duration(duration)
        self.set_rating(rating)

    def get_duration(self):
        return self.__duration

    def get_rating(self):
        return self.__rating

    def set_duration(self, duration):
        if not (1 <= duration <= 300):
            raise ValueError("Продолжительность: 1-300 минут")
        self.__duration = duration

    def set_rating(self, rating):
        if rating not in self.VALID_RATINGS:
            raise ValueError(f"Рейтинг должен быть: {', '.join(self.VALID_RATINGS)}")
        self.__rating = rating

    def get_info(self):
        base = super().get_info()
        return f"{base}, DVD, {self.__duration} мин., {self.__rating}"


class Library:
    def __init__(self):
        self.__items = []

    def add_item(self, item):
        if isinstance(item, LibraryItem):
            self.__items.append(item)
            print(f"Добавлен: {item.get_title()}")
        else:
            raise TypeError("Только LibraryItem")

    def remove_item(self, item_id):
        for i, item in enumerate(self.__items):
            if item.get_item_id() == item_id:
                self.__items.pop(i)
                print(f"Удален ID {item_id}")
                return True
        print(f"ID {item_id} не найден")
        return False

    def find_items(self, search_term):
        search_term = search_term.lower()
        return [item for item in self.__items
                if search_term in item.get_title().lower()
                or search_term in item.get_author().lower()]

    def get_statistics(self):
        stats = {"Книги": 0, "Журналы": 0, "DVD": 0, "Всего": len(self.__items)}
        for item in self.__items:
            if isinstance(item, Book):
                stats["Книги"] += 1
            elif isinstance(item, Magazine):
                stats["Журналы"] += 1
            elif isinstance(item, DVD):
                stats["DVD"] += 1
        return stats

    def get_available_items(self):
        return [item for item in self.__items if not item.get_is_checked_out()]

    def display_all(self):
        print("\nВСЕ МАТЕРИАЛЫ")
        for item in self.__items:
            print(item.get_info())

    def display_stats(self):
        print("\nСТАТИСТИКА")
        for k, v in self.get_statistics().items():
            print(f"{k}: {v}")

    def display_available(self):
        print("\nДОСТУПНЫЕ")
        for item in self.get_available_items():
            print(item.get_info())


# Пример использования
if __name__ == "__main__":
    library = Library()

    # Создание материалов
    book1 = Book("Мастер и Маргарита", "Булгаков", 1967, "Роман", 480)
    magazine1 = Magazine("National Geographic", "NGS", 2023, 5)
    dvd1 = DVD("Король Лев", "Дисней", 1994, 88, "G")

    # Добавление в библиотеку
    library.add_item(book1)
    library.add_item(magazine1)
    library.add_item(dvd1)

    # Демонстрация
    library.display_all()
    library.display_stats()

    # Изменение статуса
    book1.set_is_checked_out(True)
    print("\nПосле выдачи книги:")
    library.display_available()

    # Поиск
    print("\nПоиск 'мастер':")
    for item in library.find_items("мастер"):
        print(f"  Найден: {item.get_title()}")