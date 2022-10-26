def my_zip(num1, num2, num3):
    min_num = min(len(num1), len(num2), len(num3))
    my_list = [(num1[index], list(num2)[index], num3[index]) for index in range(min_num)]
    return my_list


a = [1, 2, 3, 4, 5]
b = {1: 's', 2: 'q', 3: 4}
x = (1, 2, 3, 4, 5)
print(my_zip(a, b, x))


