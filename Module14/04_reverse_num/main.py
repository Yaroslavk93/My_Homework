def reverse(number):
  whole_part = int(number)
  summ_whole = 0
  while whole_part > 0:
    disig = whole_part % 10
    whole_part //= 10
    summ_whole *= 10
    summ_whole += disig
  return str(summ_whole)

def reverse2(number):
  fractional = ""
  for symbol in str(number):
    fractional += symbol
    if symbol == ".":
      fractional = ""
  fractional = reverse(fractional)
  return fractional


num1 = float(input('Введите первое число: '))
num2 = float(input('Введите второе число: '))

reverse_num1 = float(str(reverse(num1) + '.' + reverse2(num1)))
reverse_num2 = float(str(reverse(num2) + '.' + reverse2(num2)))
print('\nПервое число наоборот:', reverse_num1)
print('Введите второе число:', reverse_num2)

print('Сумма:', reverse_num1 + reverse_num2)