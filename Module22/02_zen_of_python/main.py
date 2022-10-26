zen_file = open('zen.txt', 'r')

zen_list = reversed([string for string in zen_file])
for i in zen_list:
    print(i, end='')

zen_file.close()