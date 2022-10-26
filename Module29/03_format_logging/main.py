from datetime import datetime
import functools
from typing import Callable
import time


def data_time(cls, func, date_format):

    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        date = date_format
        for sym in date:
            if sym.isalpha():
                date = date.replace(sym, '%' + sym)

        print(
            f"- Запускается '{cls.__name__}.{func.__name__}'. "
            f"Дата и время запуска: {datetime.now().strftime(date)}"
        )
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(
            f"- Завершение '{cls.__name__}.{func.__name__}', "
            f"время работы = {round(end - start, 3)}s"
        )
        return result
    return wrapped


def log_methods(date_format: Callable) -> Callable:

    @functools.wraps(date_format)
    def decorator(cls):
        for i_method in dir(cls):
            if i_method.startswith('__') is False:
                cur_method = getattr(cls, i_method)
                decorated_method = data_time(cls, cur_method, date_format)
                setattr(cls, i_method, decorated_method)
        return cls
    return decorator


@log_methods("b d Y - H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()