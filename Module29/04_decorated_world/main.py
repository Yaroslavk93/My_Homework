from typing import Callable
import functools


def decorator_with_args_for_any_decorator(dec_in_dec: Callable) -> Callable:
    def variables(*args, **kwargs) -> Callable:
        def wrapped(func: Callable) -> Callable:
            return dec_in_dec(func, *args, **kwargs)
        return wrapped
    return variables


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs) -> Callable:

    @functools.wraps(func)
    def wrapped(*transfer_args, **transfer_kwargs) -> Callable:
        print(f'Переданные арги и кварги в декоратор: {args} {kwargs}')
        return func(*transfer_args, **transfer_kwargs)
    return wrapped

@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)
