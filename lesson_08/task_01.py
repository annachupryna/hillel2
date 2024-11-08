"""This is a file for homework 8."""

# Створіть масив зі строками, які будуть складатися з чисел,
# які розділені комою. Наприклад: [”1,2,3,4”, ”1,2,3,4,50” ”qwerty1,2,3”]
# Для кожного елементу списку виведіть суму всіх чисел
# (створіть нову функцію для цього). Якщо є символи, що не є числами
# (”qwerty1,2,3” у прикладі), вам потрібно зловити
# вийняток і вивести “Не можу це зробити!”
# Використовуйте блок try\except, щоб уникнути інших символів,
# окрім чисел у списку.Для цього прикладу правильний вивід
# буде - 10, 60, “Не можу це зробити”

some_array1 = ['1,2,3,4', '1,2,3,4,50', 'ghg1,2,3']


def all_sum(rows):
    """
    Sum value of each string consisting of numbers.

    Args:
        rows (list): The list of strings to process.

    Returns:
        None.
    """
    try:
        for el in rows:
            outcome = sum([int(el) for el in el.split(',')])
            print(outcome)
    except Exception:
        print('Не можу це зробити')


all_sum(some_array1)
