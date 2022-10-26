import time


def sleep(func):
    def wrapped(timeout=3):
        while timeout != 0:
            print(f'Подождите {timeout} секунды(у)')
            time.sleep(1)
            timeout -= 1
        func()
    return wrapped


@ sleep
def my_program():
    print('\nСпасибо за ожидание!')


my_program()
