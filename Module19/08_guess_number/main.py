max_digit = set(range(1, int(input('Введите максимальное число: ')) + 1))
numbers = max_digit

while True:
    num_dict = input('Нужное число есть среди вот этих чисел: ').capitalize()
    if num_dict == 'Помогите!':
        break
    num_dict = {int(num) for num in num_dict.split()}
    Artem = input('Ответ Артёма: ').capitalize()
    if Artem == 'Да':
        numbers &= num_dict
    else:
        numbers &= max_digit - num_dict

print('Артём мог загадать следующие числа:', ' '.join([str(i) for i in sorted(numbers)]))