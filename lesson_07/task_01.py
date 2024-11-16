"""This is a file for homework 6."""


# task 1
# Задача - надрукувати табличку множення на задане число, але
# лише до максимального значення для добутку - 25.
# Код майже готовий, треба знайти помилки та випраавити\доповнити.


def multiplication_table(number):
    """
    Print the multiplication table until the result exceeds 25.

    Args:
        number (int): The number to be multiplied.

    Returns:
        None.
    """
    multiplier = 1
    outcome = 0
    while outcome <= 25:
        outcome = number * multiplier
        if outcome > 25:
            print('Stop action. Next operation is greater than 25')
            break
        print(f'{number} * {multiplier} = {outcome}')
        multiplier += 1


multiplication_table(3)


# task 2
# Написати функцію, яка обчислює суму двох чисел.


def sum_numbers(first_number, second_number):
    """
    Sum given numbers.

    Args:
        first_number (int): The first number to sum.
        second_number (int): The second number to sum.

    Returns:
        int: the sum of first and second numbers.
    """
    return first_number + second_number


example = sum_numbers(1, 1)
print(example)


# task 3
# Написати функцію, яка розрахує середнє арифметичне списку чисел.

def calculate_mean(numbers):
    """
    Calculate mean value of numbers.

    Args:
        numbers (list): The list of numbers.

    Returns:
        int: the result of sum division to amount.
    """
    return sum(numbers) / len(numbers)


res = calculate_mean([1, 2, 3, 4, 5, 6])
print(res)


# task 4
# Написати функцію, яка приймає рядок та повертає його у зворотному порядку.

def return_reverse(line):
    """
    Return reversed line.

    Args:
        line (str): The given string.

    Returns:
        str: the reversed line.
    """
    return line[::-1]


sam = return_reverse('qwerty')
print(sam)


# task 5
# Написати функцію, яка приймає список
# слів та повертає найдовше слово у списку.

def return_longest_word(words):
    """
    Return longest word of array.

    Args:
        words (list): The given list of words.

    Returns:
        str: the longest word.
    """
    return max(words, key=len)


a = return_longest_word(['a', 'ssdd', 'd', 'ff'])
print(a)


# task 6
# Написати функцію, яка приймає два рядки та повертає індекс
# першого входження другого рядка у перший рядок, якщо другий
# рядок є підрядком першого рядка, та -1, якщо другий рядок
# не є підрядком першого рядка.


def find_substring(val1, val2):
    """
    Determine if val2 is a substring of val1.

    Args:
        val1 (str): The string to be searched.
        val2 (str): The substring to search for.

    Returns:
        int: The starting index of the substring if found, otherwise -1.
    """
    if val2 in val1:
        return val1.index(val2)
    else:
        return -1


str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))  # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))  # поверне -1


# Оберіть будь-які 4 таски з попередніх домашніх робіт та
# перетворіть їх у 4 функції, що отримують значення та повертають результат.
# task 7
# Порахувати кількість унікальних символів в строці.
# Якщо їх більше 10 - вивести в консоль
# True, інакше - False. Строку отримати за допомогою функції input()

def unique_symbols(some_str):
    """
    Define unique symbols.

    Args:
        some_str (str): The given string of chars.

    Returns:
        bool: true if count unique symbols exceed 10.
    """
    unique = set(some_str)
    return len(unique) > 10


a = unique_symbols('bvfhhtjghrstuy')
print(a)


# task 8
# Напишіть цикл, який буде вимагати від користувача ввести слово,
# в якому є літера "h" (враховуються як великі так і маленькі).
# Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".


def h_present():
    """
    Define if letter 'h' is present.

    Args:
        None.

    Returns:
        None.
    """
    while True:
        user_input = input("Введіть слово: ")
        if user_input.lower().count('h') >= 1:
            return print("В слові є літера 'h'.")
        else:
            print("Ви не ввели літеру 'h' в слові.")


h_present()


# task 9
# Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6',
# 7, 8, 'Python', 9, 0, 'Lorem Ipsum']. Напишіть код, який свормує
# новий list (наприклад lst2), який містить лише змінні типу стрінг,
# які присутні в lst1. Данні в лісті можуть бути будь якими.


def string_only(*elements):
    """
    Return array of strings.

    Args:
        elements (list): The given list of values.

    Returns:
        lst (list): list of strings from initial array.
    """
    lst = []
    for element in elements:
        if type(element) is str:
            lst.append(element)
    return lst


a = string_only([True, 1])
print(a)


# task 10
# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті.

def even_sum(numbers):
    """
    Calculate sum of even numbers.

    Args:
        numbers (list): The given list of values.

    Returns:
        all_sum (int): sum of even numbers.
    """
    all_sum = 0
    for number in numbers:
        if number % 2 == 0:
            all_sum += number
    return all_sum


numbers1 = even_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 34, 51, 23, 81])
print(numbers1)
