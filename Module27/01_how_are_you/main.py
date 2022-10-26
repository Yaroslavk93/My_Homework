def how_are_you(func):
    def wrapper():
        input('Как дела? ')
        print('А у меня не очень! Ладно, держи свою функцию.')
        func()
    return wrapper


@how_are_you
def test():
    print('<Тут что-то происходит...>')


test()
