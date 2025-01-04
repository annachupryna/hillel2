# Завдання 1
#
# Створіть клас Employee, який має атрибути name та salary.
# Далі створіть два класи, Manager та Developer, які успадковуються від Employee.
# Клас Manager повинен мати додатковий атрибут department, а клас Developer - атрибут programming_language.
# Тепер створіть клас TeamLead, який успадковується як від Manager,
# так і від Developer. Цей клас представляє керівника з команди розробників.
# Клас TeamLead повинен мати всі атрибути як Manager (ім'я, зарплата, відділ),
# а також атрибут team_size, який вказує на кількість розробників у команді, якою керує керівник.

# Напишіть тест, який перевіряє наявність атрибутів з Manager та Developer у класі TeamLead

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Manager(Employee):

    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)
        self.department = department


class Developer(Employee):

    def __init__(self, name, salary, programming_language):
        Employee.__init__(self, name, salary)
        self.programming_language = programming_language


class TeamLead(Manager, Developer):

    def __init__(self, name, salary, department, programming_language, team_size):
        Employee.__init__(self, name, salary)
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
        self.team_size = team_size


employee_1 = Employee('Ivan', 2000)
print(employee_1.name, employee_1.salary)
manager_1 = Manager('Oleh', 2500, 'sales')
print(manager_1.name, manager_1.salary, manager_1.department)
developer_1 = Developer('Inna', 2000, 'java')
print(developer_1.name, developer_1.salary, developer_1.programming_language)
team_lead_1 = TeamLead('Olena', 2700, 'qa', 'python', 7)
