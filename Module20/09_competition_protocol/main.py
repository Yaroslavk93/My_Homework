amount = int(input('Сколько записей вносится в протокол? '))
print('Записи (результат и имя):')

record = dict()
for num in range(amount):
    check = input(f'{num + 1} запись: ').split()
    if check[1] in record.keys():
        if int(check[0]) > record[check[1]]:
            element = record.pop(check[1])
            record[check[1]] = int(check[0])
    else:
        record[check[1]] = int(check[0])


sort_score = sorted(record.values(), reverse=True)

results = dict()
for score in sort_score:
    for champion in record:
        if score == record[champion]:
            results[champion] = record[champion]

print('\nИтоги соревнований:')
count = 0
for key, value in results.items():
    count += 1
    print(f'{count} место: {key} ({value})')
    if count == 3:
        break
