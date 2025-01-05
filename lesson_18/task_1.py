# Генератори:
# Напишіть генератор, який повертає послідовність парних чисел від 0 до N.
import logging


def generate_even(m):
    for num in range(m):
        if num % 2 == 0:
            yield num


sample = generate_even(10)
for val in sample:
    print(val)


# Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


for num in fibonacci_generator():
    if num > 100:
        break
    print(num)


# Ітератори:
# Реалізуйте ітератор для зворотного виведення елементів списку.
def list_reverse(data):
    reversed_list = data[::-1]
    print(reversed_list)
    return reversed_list


list_reverse([1, 2, 3])


# # Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.
def return_even(num):
    current_num = 0
    while current_num < num:
        if current_num % 2 == 0:
            yield current_num
        current_num += 1


for even_num in return_even(10):
    print(even_num)


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
