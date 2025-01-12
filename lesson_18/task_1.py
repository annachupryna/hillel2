# Генератори:
# Напишіть генератор, який повертає послідовність парних чисел від 0 до N.
import logging


class EvenIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration

        while self.current <= self.n:
            if self.current % 2 == 0:
                result = self.current
                self.current += 1
                return result
            self.current += 1

        raise StopIteration


even_numbers = EvenIterator(10)
for num in even_numbers:
    print(num)


# Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.

class FibonaciGenerator:

    def __init__(self, n):
        self.n = n
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.a > self.n:
            raise StopIteration

        while self.a < self.n:
            result = self.a
            self.a, self.b = self.b, self.a + self.b
            return result


fib_nums = FibonaciGenerator(10)
for num in fib_nums:
    print(num)


# Ітератори:
# Реалізуйте ітератор для зворотного виведення елементів списку.

class ReverseIterator:
    def __init__(self, array):
        self.array = array
        self.index = len(self.array) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        else:
            result = self.array[self.index]
            self.index -= 1
            return result


rev = ReverseIterator([1, 2, 3, 4, 5])
for i in rev:
    print(i)


# # Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.

class EvenNumIterator:
    def __init__(self, limit):
        self.limit = limit
        self.current_num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_num > self.limit:
            raise StopIteration
        else:
            result = self.current_num
            self.current_num += 2
            return result


even = EvenNumIterator(10)
for i in even:
    print(i)
    print('EvenNumIterator')


# Декоратори:
# Напишіть декоратор, який логує аргументи та результати викликаної функції.

def log_decorator(func):
    def wrapper(*args):
        result = func(*args)
        logging.info(print(f'Function {func.__name__} with arguments {args} executed with result: {result}'))
        return result

    return wrapper


# Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.
def exception_handle_decorator(func):
    def wrapper(*args):
        try:
            return func(*args)
        except Exception as e:
            print(f'An exception occured: {e}')

    return wrapper


@exception_handle_decorator
@log_decorator
def calculate_sum(num_list):
    result = sum(num_list)
    return result


print(calculate_sum([1, 8, 3]))
print(calculate_sum([1, '9', 3]))
