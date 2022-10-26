def counter(func):
    def wrapped(*args, **kwargs):
        wrapped.count += 1
        return func(*args, **kwargs)
    wrapped.count = 0
    return wrapped


@counter
def function():
    print('Посчитай функцию')


function()
function()
function()
print(function.count)
