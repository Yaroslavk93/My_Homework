from typing import List


letters: List[str] = ['a', 'b', 'c', 'd', 'e']
numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]

my_zip: List[tuple] = list(map(lambda str_x, int_y: (str_x, int_y), letters, numbers))
print(my_zip)
