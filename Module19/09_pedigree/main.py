def place(human):
    if human not in family_tree:
        return 0
    else:
        return 1 + place(family_tree[human])

family_tree = dict()
for num in range(1, int(input('Введите количество человек: '))):
    child, parent = input(f'{num} пара: ').split()
    family_tree[child] = parent

position = dict()
for human in set(family_tree.keys()).union(set(family_tree.values())):
    position[human] = place(human)

print('\n«Высота» каждого члена семьи:')
for key, value in sorted(position.items()):
    print(key, value)

