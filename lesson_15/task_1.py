"""Створіть клас геометричної фігури "Ромб". Клас повинен мати наступні атрибути:

сторона_а (довжина сторони a).
кут_а (кут між сторонами a і b).
кут_б (суміжний з кутом кут_а).
Необхідно реалізувати наступні вимоги:

Значення сторони сторона_а повинно бути більше 0.
Кути кут_а та кут_б повинні задовольняти умову: кут_а + кут_б = 180
Протилежні кути ромба завжди рівні, тому при заданому значенні кут_а, значення кут_б обчислюється автоматично.
Для встановлення значень атрибутів використовуйте метод __setattr__."""


class Rhombus:
    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a
        self.angle_b = self.calculate_side_b()

    def calculate_side_b(self):
        side_b = 180 - self.side_a
        return side_b

    def __setattr__(self, key, value):
        if key == 'side_a':
            if value <= 0:
                raise AttributeError(f'Value for {key} should be 0 < but entered {value}.')
            super().__setattr__(key, value)
        elif key == 'angle_a':
            if value <= 0:
                raise AttributeError(f'Value for {key} should be 0 < but entered {value}.')
            super().__setattr__(key, value)
        else:
            super().__setattr__(key, value)


my_romb = Rhombus(3, 3)

print(my_romb.side_a, my_romb.angle_a, my_romb.angle_b)
