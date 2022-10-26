print(list(filter(lambda x: all(map(lambda y: x % y != 0, range(2, int(x ** 0.5) + 1))), range(2, 1001))))


prime_list = []
for x in range(2, 1001):
    for y in range(2, x):
        if x % y == 0:
            break
    else:
        prime_list.append(x)

print(prime_list)
