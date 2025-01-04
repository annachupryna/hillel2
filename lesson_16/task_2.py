# Завдання 2
# Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру.
# Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично вірні для
# них методи для площі та периметру. Властивості по типу “довжина сторони” й т.д. повинні бути приватними,
# та ініціалізуватись через конструктор. Створіть Декілька різних об’єктів фігур, та у циклі порахуйте
# та виведіть в консоль площу та периметр кожної.

from abc import ABC, abstractmethod


class Figure(ABC):

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def get_name(self):
        pass


class Square(Figure):

    def __init__(self, side):
        self.side = side

    def get_area(self):
        area = self.side ** 2
        return area

    def get_perimeter(self):
        perimeter = self.side * 4
        return perimeter

    @staticmethod
    def get_name():
        return 'Square'


class Rectangle(ABC):

    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def get_area(self):
        area = self.side_a * self.side_b
        return area

    def get_perimeter(self):
        perimeter = (self.side_b + self.side_a) * 2
        return perimeter

    @staticmethod
    def get_name():
        return 'Rectangle'


class Triangle(ABC):

    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def get_perimeter(self):
        perimeter = (self.side_a + self.side_b + self.side_c) / 2
        return perimeter

    def get_area(self):
        half_perimeter = (self.side_a + self.side_b + self.side_c) / 2
        area = pow(half_perimeter * ((half_perimeter - self.side_a)
                                     * (half_perimeter - self.side_b)
                                     * (half_perimeter - self.side_c)), 0.5)
        return area

    @staticmethod
    def get_name():
        return 'Triangle'


all_figures = [Square(5), Rectangle(2, 3), Triangle(2, 3, 4)]
for figure in all_figures:
    print(f'Perimeter of {figure.get_name()} is {figure.get_perimeter()}')
    print(f'Area of {figure.get_name()} is {figure.get_area()}')
