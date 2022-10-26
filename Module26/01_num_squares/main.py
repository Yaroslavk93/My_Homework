class Iteration:

    def __init__(self, num):
        self.__num = num
        self.__counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__counter < self.__num:
            self.__counter += 1
            return self.__counter ** 2
        else:
            raise StopIteration('Ошибка: "Вы превысили допустимое значение!"')


N = int(input('Введите целое число: '))

# Класс - итератор
itr_class = Iteration(N)
print('\nКласс - итератор:', end=' ')
for i_num in itr_class:
    print(i_num, end=' ')


# Функция - генератор
def generator(my_num):
    for gen_num in range(1, N + 1):
        yield gen_num ** 2


gen_func = generator(N)
print('\n\nФункция - генератор:', end=' ')
for value in gen_func:
    print(value, end=' ')

# Генераторное выражение
print('\n\nГенераторное выражение:', end=' ')
gen_expression = (num ** 2 for num in range(1, N + 1))
for number in gen_expression:
    print(number, end=' ')
