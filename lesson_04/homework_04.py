"""This is a file for Homework 4."""

# task 01 == Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
# треба замінити кінець абзацу на пробіл .replace("\n", " ")

adventures_of_tom_sayer = """
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while the late steamer "Big Missouri" worked .... 
and sweated in the sun, the retired artist sat on a barrel in the .... 
shade close by, dangled his legs, munched his apple, and planned 
the slaughter of more innocents. There was no lack of material; 
boys happened along every little while; they came to jeer, but .... 
remained to whitewash. .... By the time Ben was fagged out, Tom had 
traded the next chance to Billy Fisher for a kite, in good repair; 
and when he played out, Johnny Miller bought in for a dead rat and 
a string to swing it with—and so on, and so on, hour after hour. 
And when the middle of the afternoon came, from being a poor poverty,
stricken boy in the .... morning, Tom was literally rolling in wealth.
"""

# task 01
# Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
# треба замінити кінець абзацу на пробіл .replace("\n", " ")
adventures_of_tom_sayer = adventures_of_tom_sayer.replace('\n', ' ')
print(adventures_of_tom_sayer)

# task 02 == Замініть .... на пробіл
adventures_of_tom_sayer = adventures_of_tom_sayer.replace('....', ' ')
print(adventures_of_tom_sayer)

# task 03 == Зробіть так, щоб у тексті було не більше одного
# пробілу між словами.
adventures_of_tom_sayer = adventures_of_tom_sayer.split()
separator = ' '
adventures_of_tom_sayer = separator.join(adventures_of_tom_sayer)
print(adventures_of_tom_sayer)

# task 04 == Виведіть, скількі разів у тексті зустрічається літера "h".
count_h = adventures_of_tom_sayer.count("h")
print(f'Count of the letter "h" in text: {count_h}.')

# task 05 == Виведіть, скільки слів у тексті починається з Великої літери?
capital_letters_count = 0
for word in adventures_of_tom_sayer:
    if word.istitle():
        capital_letters_count += 1

print(capital_letters_count)

# task 06 == Виведіть позицію, на якій слово Tom зустрічається вдруге.
first_occurrence = adventures_of_tom_sayer.find('Tom')
second_occurrence = adventures_of_tom_sayer.find('Tom', first_occurrence+1)
print(second_occurrence)

# task 07 == Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
# Збережіть результат у змінній adwentures_of_tom_sawer_sentences
adventures_of_tom_sayer_sentences = adventures_of_tom_sayer.split('. ')

# task 08 == Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
# Перетворіть рядок у нижній регістр.
sentence_number = 0
for sentence in adventures_of_tom_sayer_sentences:
    sentence_number += 1
    if sentence_number == 4:
        print(sentence)

# task 09 == Перевірте чи починається якесь речення з "By the time".
count = 0
for sentence in adventures_of_tom_sayer_sentences:
    count += 1
    if sentence.startswith('By the time'):
        print(f'Sentence number {count} starts with "By the time"')
    else:
        print(f'Sentence number {count} does not start with "By the time"')

# task 10 == Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.

# First solution
last_sentence = adventures_of_tom_sayer_sentences[-1]
last_sentence_only_letters = last_sentence.replace(' ', '').replace(',', '').replace('.', '')
letters_count = 0
for letter in last_sentence_only_letters:
    letters_count += 1
print(letters_count)

# Second solution
symbols_count = 0
for symbol in last_sentence:
    if symbol.isalpha():
        symbols_count += 1
print(symbols_count)
