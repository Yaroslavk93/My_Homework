students_1 = list(range(160, 177, 2))
students_2 = list(range(162, 181, 3))
students_1.extend(students_2)

for i in range(len(students_1) - 1):
 for j in range(len(students_1) - i - 1):
   if students_1[j] > students_1[j + 1]:
     students_1[j], students_1[j + 1] = students_1[j + 1], students_1[j]

print('Отсортированный список учеников: ',students_1)