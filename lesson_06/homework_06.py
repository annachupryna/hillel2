"""FINISHED This is a file for homework 6."""

# Task 1
user_input = input("Введіть рядок: ")
unique_symbols = set(user_input)
unique_count = len(unique_symbols)
if unique_count > 10:
    print(True)
else:
    print(False)

# Task 2
while True:
    word = input("Введіть слово з літерою 'h': ")
    if 'h' in word.lower():
        break

# Task 3
lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
str_list = []

for item in lst1:
    if type(item) == str:
        str_list.append(item)

print(str_list)

# Task 4
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers_sum = 0
for number in numbers:
    if number % 2 == 0:
        even_numbers_sum += number

print(even_numbers_sum)
