nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

new_list = [number for index1 in nice_list for index2 in index1 for number in index2]
print('Ответ:', new_list)
