def is_prime(index):
    count = 0
    for num in range(2, index // 2 + 1):
        if index % num == 0:
            count += 1
    if count == 0 and index != 0 and index != 1:
        return True
    else:
        return False





crypto = [value for index, value in enumerate(input('Введите текст: ')) if is_prime(index)]

print('Ответ в консоли:', crypto)