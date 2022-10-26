print('Введите координаты монетки:')
X = float(input('X: '))
Y = float(input('Y: '))
r = float(input('Введите радиус: '))

if abs(X) > r or abs(Y) > r:
    print('Монетки в области нет')
else:
    print('Монетка где-то рядом')