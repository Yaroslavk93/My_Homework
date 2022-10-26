import random


class Students:

    def __init__(self, full_name, group, performace):
        self.full_name = full_name
        self.group = group
        self.performace = performace
        self.mean = sum(performace) / len(performace)

    def sort_key(self):
        return self.mean

    def __str__(self):
        return f'Имя: {self.full_name},     № группы: {self.group},     Средний балл: {self.mean}'


class Sorted_list:

    def __init__(self, full_group):
        self.full_group = full_group

    def result(self):
        for i in self.full_group:
            print(i)


def pupil_info(names, surnames):
    name = f'{random.choice(names)} {random.choice(surnames)}'
    num_group = random.randint(1, 3)
    grades = [random.randint(3, 5) for _ in range(5)]
    return name, num_group, grades


names_tuple = ('Сидорова', 'Петрова', 'Иванов', 'Стрельцов', 'Пушкин', 'Самоварова', 'Романов')
surnames_tuple = ('И. А.', 'В. М.', 'Г. Ф.', 'С. А.', 'В. В.', 'А. А.', 'М. Н.')

students_list = [Students(*pupil_info(names_tuple, surnames_tuple)) for i in range(10)]
students_list.sort(key=lambda x: x.sort_key())

new_list = Sorted_list(students_list)
new_list.result()

