"""Створіть клас геометричної фігури "Ромб". Клас повинен мати наступні атрибути:

сторона_а (довжина сторони a).
кут_а (кут між сторонами a і b).
кут_б (суміжний з кутом кут_а).
Необхідно реалізувати наступні вимоги:

Значення сторони сторона_а повинно бути більше 0.
Кути кут_а та кут_б повинні задовольняти умову: кут_а + кут_б = 180
Протилежні кути ромба завжди рівні, тому при заданому значенні кут_а, значення кут_б обчислюється автоматично.
Для встановлення значень атрибутів використовуйте метод __setattr__.
"""


class Rhombus:
    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a
        self._angle_b = self.calculate_angle_b()  # роблю кут б умовно недостпуним для змін

    def calculate_angle_b(self):
        angle_b = 180 - self.angle_a
        return angle_b

    def __setattr__(self, key, value):
        if key == 'side_a':
            if value <= 0:
                raise AttributeError(f'Value for {key} should be 0 < but entered {value}.')
            super().__setattr__(key, value)
        elif key == 'angle_a':
            if not 0 < value < 180:
                raise AttributeError(f'Value for {key} should be 0 < but entered {value}.')
            super().__setattr__(key, value)
        else:
            super().__setattr__(key, value)

    @property
    def angle_b(self):  # геттер для кута б, при виклику проперті кута б буде спрацьовувати ця функція
        return self._angle_b


my_romb = Rhombus(3, 66)
print(my_romb.side_a, my_romb.angle_a, my_romb.angle_b)
