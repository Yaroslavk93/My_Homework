import re


phone_book = ['9999999999', '999999-999', '99999x9999']
count = 0

for number in phone_book:
    count += 1
    print(f'{count}й номер: ', end='')
    if re.findall(r'8|9\d{9}', number):
        print('всё в порядке')
    else:
        print('не подходит')
