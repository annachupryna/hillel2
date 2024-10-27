"""This is a file for homework 6."""

# Task 1
user_input = input("Введіть текст: ")
unique_symbols = set(user_input)
if len(unique_symbols) > 10:
    print(True)
else:
    print(False)


# Task 2
while True:
    user_input = input("Введіть слово: ")
    if user_input.lower().count('h') >= 1:
        print("В слові є літера 'h'.")
        break
    else:
        print("Ви не ввели літеру 'h' в слові.")

# Task 3
lst1 = [
    '1',
    '2',
    3,
    True,
    'False',
    5,
    '6',
    7,
    8,
    'Python',
    9,
    0,
    'Lorem Ipsum',
]
lst2 = []
for element in lst1:
    if type(element) is str:
        lst2.append(element)

print(lst2)

# Task 4
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 34, 51, 23, 81]
all_sum = 0
for number in numbers:
    if number % 2 == 0:
        all_sum += number

print(all_sum)
