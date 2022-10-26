def symmetry(number):
    reverse_list = []
    for i_nums in range(len(number) - 1, -1, -1):
        reverse_list.append(number[i_nums])
    if number == reverse_list:
        return True
    else:
        return False

amt_num = int(input('Кол-во чисел: '))
num_list = []
for nums in range(amt_num):
    print('Число: ', end = '')
    digit = int(input())
    num_list.append(digit)
new_list = []
answer = []

for i_num in range(0, len(num_list)):
    for j_elem in range(i_num, len(num_list)):
        new_list.append(num_list[j_elem])
    if symmetry(new_list):
        for i_answer in range(0, i_num):
            answer.append(num_list[i_answer])
        answer.reverse()
        break
    new_list = []

print('\nПоследовательность:', num_list)
print('Нужно приписать чисел:', len(answer))
print('Сами числа:', answer)