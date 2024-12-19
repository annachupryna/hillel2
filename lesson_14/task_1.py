# Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
# Створіть об'єкт цього класу, представляючи студента. Потім додайте метод до класу "Студент",
# який дозволяє змінювати середній бал студента.
# Виведіть інформацію про студента та змініть його середній бал.

class Student:
    def __init__(self, name, surname, age, average_rate):
        self.name = name
        self.surname = surname
        self.age = age
        self.average_rate = average_rate

    def change_average_rate(self, new_rate):
        self.average_rate = new_rate


student_1 = Student('Ivan', 'Ivanov', 20, 9)
student_1.change_average_rate(10)
print(student_1.average_rate)
