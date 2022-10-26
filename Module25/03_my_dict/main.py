# class MyDict:
#     """
#     MyDict - класс превращения None в 0
#     Attributes:
#          self.__zero = ключ словаря, возвращающий значение через get
#          set_zero - сеттер
#          get_zero - геттер
#     """
#
#     def __init__(self, zero):
#         self.__zero = zero
#
#     def set_zero(self):
#         if self.__zero is None:
#             self.__zero = 0
#
#     def get_zero(self):
#         return self.__zero
#
#
# my_dict = dict()
# my_key = input('Введите ключ словаря: ')
#
# get_zero = MyDict(my_dict.get(my_key))
# get_zero.set_zero()
# print(get_zero.get_zero())


class MyDict(dict):
    def get(self, key, default=0):
        return super().get(key, default)


my_dict = MyDict().get(input('Введите ключ словаря: '))
print(my_dict)
