def TowerOfHanoi (n, x = 1, y = 3):
    if n == 1:
        print(f'Переложить диск {n} со стержня номер {x} на стержень номер {y}')
    else:
        TowerOfHanoi(n - 1, x, 6 - x - y)
        print(f'Переложить диск {n} со стержня номер {x} на стержень номер {y}')
        TowerOfHanoi(n - 1, 6 - x - y, y)



num = int(input('Введите количество дисков: '))
TowerOfHanoi(num)