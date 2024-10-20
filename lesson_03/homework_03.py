"""This is a file for Homework 3."""

# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала
# декілька фізичних ліній
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк

alice_in_wonderland = (
    "'Would you tell me, please, which way I ought to go from here?'\n"
    "'That depends a good deal on where you want to get to,' said the Cat.\n"
    "'I don't much care where ——' said Alice.\n"
    "'Then it doesn't matter which way you go,' said the Cat.\n"
    "'—— so long as I get somewhere,' Alice added as an explanation.\n"
    "'Oh, you're sure to do that,' said the Cat, 'if you only walk long enough.'"
)

print(alice_in_wonderland)

# task 04
# Площа Чорного моря становить 436 402 км2, а площа Азовського
# моря становить 37 800 км2. Яку площу займають Чорне та Азов-
# ське моря разом?

black_sea_area = 436_402
azov_sea_area = 37_800
common_area = black_sea_area + azov_sea_area
print(common_area)

# task 05
# Мережа супермаркетів має 3 склади, де всього розміщено
# 375 291 товар. На першому та другому складах перебуває
# 250 449 товарів. На другому та третьому – 222 950 товарів.
# Знайдіть кількість товарів, що розміщені на кожному складі.

all_goods = 375_291
first_second_warehouse = 250_449
second_third = 222_950
third_warehouse = all_goods - first_second_warehouse
second_warehouse = second_third - third_warehouse
first_warehouse = first_second_warehouse - second_warehouse

print(
    f'Goods on the first warehouse - {first_warehouse}.\n'
    f'Goods on the second warehouse - {second_warehouse}.\n'
    f'Goods on the third warehouse - {third_warehouse}.'
)

# task 06
# Михайло разом з батьками вирішили купити комп’ютер, ско-
# риставшись послугою «Оплата частинами». Відомо, що сплачу-
# вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
# вартість комп’ютера.

amount_of_payments = 18
monthly_payment = 1_179
computer_price = amount_of_payments * monthly_payment
print(f'Price of computer is {computer_price} hryvnias')

# task 07
# Знайди остачу від ділення чисел:
# a) 8019 : 8     d) 7248 : 6
# b) 9907 : 9     e) 7128 : 5
# c) 2789 : 5     f) 19224 : 9

sample_a = 8019 % 8
sample_b = 9907 % 9
sample_c = 2789 % 5
sample_d = 7248 % 6
sample_e = 7128 % 5
sample_f = 19224 % 9
print(
    f'The remainder of dividing for samples are:\n'
    f'a) 8019 : 8 = {sample_a}\n'
    f'b) 9907 : 9 = {sample_b}\n'
    f'c) 2789 : 5 = {sample_c}\n'
    f'd) 7248 : 6 = {sample_d}\n'
    f'e) 7128 : 5 = {sample_e}\n'
    f'f) 19224 : 9 = {sample_f}'
)

# task 08
# Іринка, готуючись до свого дня народження, склала список того,
# що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
# для даного її замовлення.
# Назва товару    Кількість   Ціна
# Піца велика     4           274 грн
# Піца середня    2           218 грн
# Сік             4           35 грн
# Торт            1           350 грн
# Вода            3           21 грн

big_pizza_price, big_pizza_amount = 274, 4
medium_pizza_price, medium_pizza_amount = 218, 2
juice_price, juice_amount = 35, 4
cake_price, cake_amount = 350, 1
water_price, water_amount = 21, 3

money_needed = (
    (big_pizza_amount * big_pizza_price)
    + (medium_pizza_amount * medium_pizza_price)
    + (juice_amount * juice_price)
    + (cake_amount * cake_price)
    + (water_amount * water_price)
)
print(f'Irynka needs {money_needed} hryvnias to buy all products for her birthday.')

# task 09
# Ігор займається фотографією. Він вирішив зібрати всі свої 232
# фотографії та вклеїти в альбом. На одній сторінці може бути
# розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
# Ігорю, щоб вклеїти всі фото?

all_photos = 232
photos_on_page = 8
pages_needed = all_photos / photos_on_page
print(f'Ihor needs {pages_needed} album pages for his photos.')

# task 10
# Родина зібралася в автомобільну подорож із Харкова в Буда-
# пешт. Відстань між цими містами становить 1600 км. Відомо,
# що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
# становить 48 літрів.
# 1) Скільки літрів бензину знадобиться для такої подорожі?
# 2) Скільки щонайменше разів родині необхідно заїхати на зап-
# равку під час цієї подорожі, кожного разу заправляючи пов-
# ний бак?

distance = 1600
fuel_consumption_per_hundred_km = 9
tank_capacity = 48
fuel_required_for_trip = (distance / 100) * fuel_consumption_per_hundred_km
gas_station_visits = fuel_required_for_trip / tank_capacity

print(
    f'{int(fuel_required_for_trip)} liters of fuel is required for family trip.\n'
    f'Minimum {int(gas_station_visits)} times it is required to refill the tank on gas station.'
)
