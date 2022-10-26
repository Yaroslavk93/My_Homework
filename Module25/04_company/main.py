class Person:

    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def __str__(self):
        return f'Фамилия и имя сотрудника: ' \
               f'{self.__surname} {self.__name}. ' \
               f'Возраст: {self.__age}'


class Employee(Person):
    def salary(self):
        pass

    def info_person(self):
        return f'{super().__str__()} {self.salary()}\n'


class Manager(Employee):
    def salary(self):
        return f'\nЗарплата: {13000} рублей'

class Agent(Employee):
    sales = 500000
    def salary(self):
        return f'\nЗарплата: {5000 + round(0.05 * self.sales)} рублей'

class Worker(Employee):
    hours = 183
    def salary(self):
        return f'\nЗарплата: {100 * self.hours} рублей\n'


manager = Manager('Василий', 'Петров', 33)
agent = Agent('Анастасия', 'Смирнова', 29)
worker = Worker('Денис', 'Иванов', 45)

print(manager.info_person())
print(agent.info_person())
print(worker.info_person())
