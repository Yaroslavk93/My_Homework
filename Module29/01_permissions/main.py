import functools
from collections.abc import Callable


def check_permission(user_name: str) -> Callable:
    user_permissions = ['admin']

    def permission(func: Callable) -> Callable:

        @functools.wraps(func)
        def wrapped():
            if user_name in user_permissions:
                func()
            else:
                try:
                    raise PermissionError('PermissionError')
                except PermissionError as error:
                    print(
                        f'{error}: У пользователя недостаточно прав, '
                        f'чтобы выполнить функцию {func.__name__}'
                    )
        return wrapped
    return permission


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()
