import random


class Parent:

    def __init__(self, p_name, p_age, p_c_list):
        self.p_name = p_name
        self.p_age = p_age
        self.p_c_list = p_c_list

    def __str__(self):
        p_info = '\n'.join(str(i) for i in self.p_c_list)
        return f'Имя и возраст родителя: {self.p_name} {self.p_age} года/лет\n'\
                f'Список детей:\n{p_info}'

    def cond(self, children):
        for i_children in self.p_c_list:
            if i_children is children:
                i_children.c_cond = True

    def hungry(self, children):
        for i_children in self.p_c_list:
            if i_children is children:
                i_children.c_hungry = True


class Children:

    def __init__(self, c_name, c_age, c_cond, c_hungry):
        self.c_name = c_name
        self.c_age = c_age
        self.c_cond = c_cond
        self.c_hungry = c_hungry

    def __str__(self):
        return f'{self.c_name} {self.c_age} года/лет ' + \
               ('Спокоен ' if self.c_cond else 'Раздражён ') + \
               ('Сыт ' if self.c_hungry else 'Голоден ')


def initialization():
    aaa = (True, False)
    parent_name = input('Введите имя, возраст и количество детей родителя: ').split()
    child_name = [input('Введите имя и возраст ребёнка: ').split() for _ in range(int(parent_name[2]))]
    child_list = [
        Children(i_child[0], i_child[1], random.choice(aaa), random.choice(aaa))
        for i_child in child_name
    ]
    parent_info = Parent(parent_name[0], int(parent_name[1]), child_list)

    return child_list, parent_info


child, parent = initialization()
while True:
    action = int(input(
        '\n1. Сообщить информацию о себе\n'
        '2. Успокоить ребёнка\n'
        '3. Покормить ребёнка\n'
        '0. Выйти из программы\n'
        'Выберите действие: '
    ))

    if action == 1:
        print(parent)
    elif action == 2:
        for i in child:
            parent.cond(i)
    elif action == 3:
        for i in child:
            parent.hungry(i)
    elif action == 0:
        print('Вы завершили программу.')
        break
    else:
        print('Такой команды нет.')
