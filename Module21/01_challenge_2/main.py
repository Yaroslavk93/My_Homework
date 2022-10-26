def function(new_num, result = 1):
    print(result)
    if result != new_num:
        function(new_num, result + 1)


num = int(input('Введите num: '))
result = function(num)