cols = 3; rows = 4
List = [ list(range(x, x + rows * (cols - 1) + 1, rows)) for x in range(1, rows + 1) ]

print(List)