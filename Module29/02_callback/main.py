from collections.abc import Callable
import functools


app = dict()
def callback(symbol: str) -> Callable:
    def function(func: Callable) -> Callable:
        app[symbol] = func

        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            result = func(*args, **kwargs)
            return result
        return wrapped
    return function


@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')
