"""
Задание #1:
Создать класс "Компьютер" у которого должны быть следующие параметры:
 - Имя компьютера
 - Количество оперативной памяти
 - Мощность процессора (от 1 до 100)
"""


class Computer:

    def __init__(self, name: str, ram: int, processor_power: int):
        self.name = name
        self.ram = ram
        self.processor_power = processor_power

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def ram(self):
        return self._ram

    @ram.setter
    def ram(self, value: int):
        self._ram = value

    @property
    def processor_power(self):
        return self._processor_power

    @processor_power.setter
    def processor_power(self, value: int):
        if 0 < value < 100:
            self._processor_power = value
        else:
            raise ValueError("Мощность должна быть указана в диапазоне от 0 до 100!")


"""
Задание #2:
Реализуйте класс «Стадион». Необходимо хранить в
полях класса: название стадиона, дату открытия, страну,
город, вместимость. Реализуйте методы класса для ввода
данных, вывода данных, реализуйте доступ к отдельным
полям через методы класса.
"""


class Stadium:
    def __init__(self, name: str, date: str, country: str, city: str, capacity: int):
        self.name = name
        self.date = date
        self.country = country
        self.city = city
        self.capacity = capacity

    def __str__(self):
        return f"Название: {self.name}\n" \
               f"Дата открытия: {self.date}\n" \
               f"Страна: {self.country}\n" \
               f"Город: {self.city}\n" \
               f"Вместительность: {self.capacity}\n"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value: str):
        self._date = value

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, value: str):
        self._country = value

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value: str):
        self._city = value

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value: str):
        self._capacity = value


"""
Задание #3:
Создайте класс Device, который содержит информацию об устройстве.
С помощью механизма наследования, реализуйте класс
CoffeeMachine (содержит информацию о кофемашине),
класс Blender (содержит информацию о блендере), класс
MeatGrinder (содержит информацию о мясорубке).
Каждый из классов должен содержать необходимые
для работы методы.
"""


class Device:

    def name_of_device(self) -> str:
        pass

    def get_price_(self) -> float:
        pass


class CoffeeMachine(Device):

    def __init__(self, price: float, brand: str, model: str):
        self.price_of_coffee_machine = price
        self.brand_of_coffee_machine = brand
        self.model_of_coffee_machine = model

    def name_of_device(self) -> str:
        return "Кофемашина"

    @property
    def price_of_device(self) -> float:
        return self.price_of_coffee_machine

    @price_of_device.setter
    def price_of_device(self, value):
        if isinstance(value, float):
            self.price_of_coffee_machine = value
        else:
            raise ValueError('price_of_coffee_machine должен быть типом float')

    @property
    def brand_of_device(self) -> str:
        return self.brand_of_coffee_machine

    @brand_of_device.setter
    def brand_of_device(self, value):
        if isinstance(value, str):
            self.brand_of_coffee_machine = value
        else:
            raise ValueError('brand_of_coffee_machine должен быть типом str')

    @property
    def model_of_device(self) -> str:
        return self.model_of_coffee_machine

    @model_of_device.setter
    def model_of_device(self, value):
        if isinstance(value, str):
            self.model_of_coffee_machine = value
        else:
            raise ValueError('brand_of_coffee_machine должен быть типом str')


class Blender(Device):

    def __init__(self, price: float, brand: str, model: str):
        self.price_of_blender = price
        self.brand_of_blender = brand
        self.model_of_blender = model

    def name_of_device(self) -> str:
        return "Блендер"

    @property
    def price_of_device(self) -> float:
        return self.price_of_blender

    @price_of_device.setter
    def price_of_device(self, value):
        if isinstance(value, float):
            self.price_of_blender = value
        else:
            raise ValueError('price_of_blender должен быть типом float')

    @property
    def brand_of_device(self) -> str:
        return self.brand_of_blender

    @brand_of_device.setter
    def brand_of_device(self, value):
        if isinstance(value, str):
            self.brand_of_blender = value
        else:
            raise ValueError('brand_of_blender должен быть типом str')

    @property
    def model_of_device(self) -> str:
        return self.model_of_blender

    @model_of_device.setter
    def model_of_device(self, value):
        if isinstance(value, str):
            self.model_of_blender = value
        else:
            raise ValueError('model_of_blender должен быть типом str')


class MeatGrinder(Device):

    def __init__(self, price: float, brand: str, model: str):
        self.price_of_meat_grinder = price
        self.brand_of_meat_grinder = brand
        self.model_of_meat_grinder = model

    @property
    def price_of_device(self) -> float:
        return self.price_of_meat_grinder

    @price_of_device.setter
    def price_of_device(self, value):
        if isinstance(value, float):
            self.price_of_meat_grinder = value
        else:
            raise ValueError('price_of_meat_grinder должен быть типом float')

    @property
    def brand_of_device(self) -> str:
        return self.brand_of_meat_grinder

    @brand_of_device.setter
    def brand_of_device(self, value):
        if isinstance(value, str):
            self.brand_of_meat_grinder = value
        else:
            raise ValueError('brand_of_meat_grinder должен быть типом str')

    @property
    def model_of_device(self) -> str:
        return self.model_of_meat_grinder

    @model_of_device.setter
    def model_of_device(self, value):
        if isinstance(value, str):
            self.model_of_meat_grinder = value
        else:
            raise ValueError('model_of_meat_grinder должен быть типом str')


"""
Задание #4:
Реализуйте класс «Книга». Необходимо хранить в
полях класса: название книги, год выпуска, издателя,
жанр, автора, цену. Реализуйте методы класса для ввода
данных, вывода данных, реализуйте доступ к отдельным
полям через методы класса.
Реализуйте функцию для получения книг по всем параметрам класса.
"""


class Book:
    def __init__(self, name, year, publisher, genre, author, price):
        self.name = name
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value
        else:
            raise ValueError('name must be a string')

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if isinstance(value, int):
            self._year = value
        else:
            raise ValueError('year must be an integer')

    @property
    def publisher(self):
        return self._publisher

    @publisher.setter
    def publisher(self, value):
        if isinstance(value, str):
            self._publisher = value
        else:
            raise ValueError('publisher must be a string')

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, value):
        if isinstance(value, str):
            self._genre = value
        else:
            raise ValueError('genre must be a string')

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if isinstance(value, str):
            self._author = value.title()
        else:
            raise ValueError('author must be a string')

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if isinstance(value, float):
            self._price = value
        else:
            raise ValueError('price must be a float')

    def __str__(self):
        return f"Название - {self.name}\n" \
               f"Год - {self.year}\n" \
               f"Издатель - {self.publisher}\n" \
               f"Жанр - {self.genre}\n" \
               f"Автор - {self.author}\n" \
               f"Цена - {self.price}\n"


books_list = []


def filter_search_books():
    menu_filter = "1 - Фильтр по автору\n" \
                  "2 - Фильтр по названию\n" \
                  "3 - Фильтр по жанру\n" \
                  "4 - Фильтр по цене\n" \
                  "0 - Закрыть фильтр\n--> "
    while True:
        action = input(menu_filter)
        if action == "1":
            author = input("Введите автора: ")
            for i in range(0, len(books_list)):
                if author in books_list[i].author:
                    print(str(books_list[i]))
            continue
        elif action == "2":
            title = input("Введите заголовок: ")
            for i in range(0, len(books_list)):
                if title in books_list[i].name:
                    print(str(books_list[i]))
            continue
        elif action == "3":
            description = input("Введите жанр: ")
            for i in range(0, len(books_list)):
                if description in books_list[i].genre:
                    print(str(books_list[i]))
            continue
        elif action == "4":
            while True:
                try:
                    price_from = float(input("Введите цену от: "))
                except ValueError:
                    print('Нужно ввести число')
                    continue
                try:
                    price_up_to = float(input("Введите цену до: "))
                except ValueError:
                    print('Нужно ввести число')
                    continue
                for i in range(0, len(books_list)):
                    if price_from < books_list[i].price < price_up_to:
                        print(str(books_list[i]))
                break
        elif action == "0":
            break


if __name__ == '__main__':
    book_1 = Book("1984", 1948, "Кто-то", "Антиутопия", "Джордж Оруэлл", 100.0)
    books_list.append(book_1)
    filter_search_books()

"""
Задание #5:
Создайте класс Circle (окружность). Для данного
класса реализуйте ряд перегруженных операторов:
    - Проверка на равенство радиусов двух окружностей
    (операция = =);
    - Сравнения длин двух окружностей (операции >, <,
    <=,>=);
    - Пропорциональное изменение размеров окружности,
    путем изменения ее радиуса (операции + - += -=).
"""


class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.circle_len = 2 * 3.14 * radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.circle_len < other.circle_len

    def __gt__(self, other):
        return self.circle_len > other.circle_len

    def __le__(self, other):
        return self.circle_len <= other.circle_len

    def __ge__(self, other):
        return self.circle_len >= other.circle_len

    def __pos__(self, value: float):
        return self.radius + value

    def __neg__(self, value: float):
        return self.radius - value


"""
Задание #6:
Создайте базовый класс Shape для рисования плоских
фигур.
Определите методы:
    - Show() — вывод на экран информации о фигуре;
    - Save() — сохранение фигуры в файл;
    - Load() — считывание фигуры из файла.
Определите производные классы:
    - Square — квадрат, который характеризуется координатами левого верхнего угла и длиной стороны;
    - Rectangle — прямоугольник с заданными координатами верхнего левого угла и размерами;
    - Circle — окружность с заданными координатами центра и радиусом;
    - Ellipse — эллипс с заданными координатами верхнего угла описанного вокруг него прямоугольника со сторонами, 
    параллельными осям координат, и размерами этого прямоугольника.
Создайте список фигур, сохраните фигуры в файл,
загрузите в другой список и отобразите информацию о
каждой из фигур.
"""


class Shape:
    def __init__(self):
        self.figure = None

    def show(self):
        pass

    def save(self):
        pass

    @staticmethod
    def load():
        with open('file.txt', 'r') as f:
            f.read()


class Square(Shape):
    def __init__(self, x, y, length):
        super(Square, self).__init__()
        self.figure = "Квадрат"
        self.x = x
        self.y = y
        self.length = length

    def show(self):
        print(f"{self.figure}\n"
              f"Левый верхний угол: ({self.x}, {self.y})\n"
              f"Длина стороны: {self.length}\n")

    def save(self):
        with open('file.txt', 'a') as f:
            f.write(f"{self.figure}\n"
                    f"Левый верхний угол: ({self.x}, {self.y})\n"
                    f"Длина стороны: {self.length}\n\n")


class Rectangle(Shape):
    def __init__(self, x, y, length_a, length_b):
        super(Rectangle, self).__init__()
        self.figure = "Прямоугольник"
        self.x = x
        self.y = y
        self.length_a = length_a
        self.length_b = length_b

    def show(self):
        print(f"{self.figure}\n"
              f"Левый верхний угол: ({self.x}, {self.y})\n"
              f"Длины сторон: {self.length_a}, {self.length_b}\n")

    def save(self):
        with open('file.txt', 'a') as f:
            f.write(f"{self.figure}\n"
                    f"Левый верхний угол: ({self.x}, {self.y})\n"
                    f"Длины сторон: {self.length_a}, {self.length_b}\n\n")


class Circles(Shape):
    def __init__(self, x, y, radius):
        super(Circles, self).__init__()
        self.figure = "Круг"
        self.x = x
        self.y = y
        self.radius = radius

    def show(self):
        print(f"{self.figure}\n"
              f"Координаты центра: ({self.x}, {self.y})\n"
              f"Радиус: {self.radius}\n")

    def save(self):
        with open('file.txt', 'a') as f:
            f.write(f"{self.figure}\n"
                    f"Координаты центра: ({self.x}, {self.y})\n"
                    f"Радиус: {self.radius}\n\n")


class Ellipse(Shape):
    def __init__(self, x, y, length_a, length_b):
        super(Ellipse, self).__init__()
        self.figure = "Эллипс"
        self.x = x
        self.y = y
        self.length_a = length_a
        self.length_b = length_b

    def show(self):
        print(f"{self.figure}\n"
              f"Левый верхний угол: ({self.x}, {self.y})\n"
              f"Длины сторон: {self.length_a}, {self.length_b}\n")

    def save(self):
        with open('file.txt', 'a') as f:
            f.write(f"{self.figure}\n"
                    f"Левый верхний угол: ({self.x}, {self.y})\n"
                    f"Длины сторон: {self.length_a}, {self.length_b}\n\n")
