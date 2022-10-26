# TODO здесь писать код
import os, functools, datetime
from typing import Callable, Any


def logging(func: Callable) -> Callable:
    """
    Декоратор, логирующий функцию
    :param func: my_func
    :return: Документация, запись ошибок в файл
    """
    @functools.wraps(func)
    def wrapped(*args, **kwargs) -> Any:
        print(func.__name__, func.__doc__)
        try:
            result = func(*args, **kwargs)
            return result

        except Exception as error:
            error_time = datetime.datetime.now()
            with open('function_errors.log', 'a', encoding='utf-8') as log_file:
                log_file.write(
                    f'Дата/время: {error_time}\t'
                    f'Имя функции: {func.__name__}\n'
                    f'Ошибка: {error}\n'
                )
    return wrapped


@logging
def find_alpha(file: Any) -> None:
    """
    Функция вызова ошибки, при обнаружении символа
    :param file: Файл с информацией о домашних заданиях к модулю 27
    :return: Возвращает информацию об ошибке
    """
    with open(file, 'r', encoding='utf-8') as alpha:
        for i_line in alpha.readlines():
            for j_sym in i_line:
                if j_sym.isalpha():
                    pass
                else:
                    raise Exception(f'{j_sym} не является буквой')


@logging
def find_digit(my_string: str) -> None:
    """
    Функция вызова ошибки, при обработке списка на наличие символов или букв
    :param my_string: Строка с элементами
    :return: Возвращает информацию об ошибке
    """

    for i_num in my_string:
        if i_num.isdigit():
            pass
        else:
            raise Exception(f'{i_num} не является цифрой')


README_file = os.path.abspath(os.path.join('../README.md'))
print(logging.__name__, logging.__doc__)
find_alpha(README_file)

digit_list = '1234bad5'
find_digit(digit_list)
