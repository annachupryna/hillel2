"""
This is a file for Homework 1.

In order for flake8 to ignore some checks, setup.cfg was created.
"""

# task 01 - Fix the syntax errors
print('Hello', end='')
print('world!')

# task 02 - Fix the syntax errors
first_string = 'Hello'
second_string = 'world'
print('{0}+{1}!'.format(first_string, second_string))  # noqa: WPS421

# task 03 - Insert the missing variable into the print function
for letter in 'Hello world!':
    print(letter)

# task 04 - Make the number of bananas always four times the number of apples
apples_count = 2
bananas_count = 4 * apples_count

# task 05 - Fix variable names
side_one = 1
side_two = 2
side_three = 3
side_four = 4

# task 06 - Calculate and display the perimeter of the figure from task 05
perimeter = side_one + side_two + side_three + side_four
print(perimeter)

# The following tasks are translated from the book "Mathematics,
# 2nd Grade" to Python:

# task 07 - Count the number of trees planted in the garden
# There were 4 apple trees planted.
# Pear trees are 5 more than apple trees, and plum trees are 2 less.
apple_trees = 4
pear_trees = apple_trees + 5
plum_trees = apple_trees - 2
total_trees = apple_trees + pear_trees + plum_trees
print(total_trees)

# task 08 - Calculate the temperature at the evening
# In the morning, the temperature was 5 degrees above zero.
# It dropped by 10 after lunch and rose by 4 in the evening.
initial_temperature = 0
temperature_morning = initial_temperature + 5
temperature_afternoon = temperature_morning - 10
temperature_evening = temperature_afternoon + 4
print(temperature_evening)

# task 09 - Calculate the number of children in the theater club today
# There are 24 boys and half as many girls in the club.
# 1 boy and 2 girls are absent today.
boys_count = 24
girls_count = boys_count / 2
boys_present = boys_count - 1
girls_present = girls_count - 2
total_kids_present = boys_present + girls_present
print(int(total_kids_present))

# task 10 - Calculate the total cost of three books
# The first book costs 8 UAH, the second is 2 UAH more,
# and the third is half the price of the first and second together.
first_book_price = 8
second_book_price = first_book_price + 2
third_book_price = (first_book_price + second_book_price) / 2
total_book_price = first_book_price + second_book_price + third_book_price
print(total_book_price)
