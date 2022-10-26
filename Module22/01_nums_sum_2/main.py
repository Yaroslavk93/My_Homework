num_file = open('numbers.txt', 'r')

num_list = []
print('Содержимое файла numbers.txt')
for digit in num_file:
    print(digit)
    for i_num in digit:
        if i_num.isdigit():
            num_list.append(int(i_num))

num_file.close()


answer_file = open('answer.txt', 'w')
answer_file.write(str(sum(num_list)))
print(f'\nСодержимое файла answer.txt\n{str(sum(num_list))}')
answer_file.close()
