from happy_farm import PotatoPatch, Gardener


patch = PotatoPatch(int(input('Введите количество грядок: ')))
mr_gardener = Gardener(input('Введите имя садовника: '), patch)
while True:
    mr_gardener.garden_work()

