from typing import Callable
import functools


def singleton(cls: Callable) -> Callable:

    @functools.wraps(cls)
    def wrapped(*args, **kwargs):
        if not wrapped.instance:
            wrapped.instance = cls(*args, **kwargs)

    wrapped.instance = None
    return wrapped


@singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))

print(my_obj is my_another_obj)
