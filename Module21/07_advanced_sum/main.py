def sum_function(digit_list):
    result = 0
    for digit in digit_list:
        if isinstance(digit, (float, int)):
            result += digit
        else:
            result += sum_function(digit)

    return result



print(sum_function(([[1, 2, [3]], [1], 3])))
print(sum_function((1, 2, 3, 4, 5)))
