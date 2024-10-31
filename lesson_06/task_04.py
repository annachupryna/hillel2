"""This is a file for homework 6."""

# Task 4
# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 34, 51, 23, 81]
all_sum = 0
for number in numbers:
    if number % 2 == 0:
        all_sum += number

print(all_sum)
