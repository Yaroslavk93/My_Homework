class Info:

    def __init__(self, arg: tuple, kwarg: dict) -> None:
        self.arg = arg
        self.kwarg = kwarg

    def __repr__(self) -> repr:
        if not self.kwarg and self.arg:
            return f'({repr(self.arg[0])})'
        elif not self.arg and self.kwarg:
            result = ''
            for key, value in self.kwarg.items():
                result += f'{key} = {value}, '
            return f'({result})'
        else:
            result = ''
            for key, value in self.kwarg.items():
                result = f'({repr(self.arg[0])}, {key} = {value})'
            return result

def debug(func):
    def wrapped(*args, **kwargs):
        info = Info(args, kwargs)
        print(f'Вызывается {func.__name__}{info.__repr__()}')
        my_func = func(*args, **kwargs)
        print(
            f'"{func.__name__}" вернула значение '
            f'"{my_func}"\n{my_func}\n'
        )
        return func
    return wrapped


@debug
def greeting(name, age=None):
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растёшь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)


greeting("Том")
greeting("Миша", age=100)
greeting(name="Катя", age=16)
