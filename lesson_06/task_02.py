"""This is a file for homework 6."""

# Task 2
# Напишіть цикл, який буде вимагати від користувача ввести слово,
# в якому є літера "h" (враховуються як великі так і маленькі).
# Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".
while True:
    user_input = input("Введіть слово: ")
    if user_input.lower().count('h') >= 1:
        print("В слові є літера 'h'.")
        break
    else:
        print("Ви не ввели літеру 'h' в слові.")
