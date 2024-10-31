"""This is a file for homework 6."""

# Task 1
# Порахувати кількість унікальних символів в строці.
# Якщо їх більше 10 - вивести в консоль
# True, інакше - False. Строку отримати за допомогою функції input()

user_input = input("Введіть текст: ")
unique_symbols = set(user_input)
if len(unique_symbols) > 10:
    print(True)
else:
    print(False)
