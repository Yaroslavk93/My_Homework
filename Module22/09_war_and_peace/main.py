import zipfile
def unzip(text_file):
    file_zip = zipfile.ZipFile(text_file, 'r')
    for string in file_zip.namelist():
        file_zip.extract(string)
    file_zip.close()


def alpha_dict(file_name):
    result_dict = dict()
    if file_name.endswith('.zip'):
        unzip(file_name)
        file_name = ''.join((file_name[:-3], 'txt'))
    text = open(file_name, 'r', encoding='utf-8')
    for i_line in text:
        for letter in i_line:
            if letter.isalpha():
                if letter not in result_dict:
                    result_dict[letter] = 0
                result_dict[letter] += 1
    text.close()

    return result_dict

def print_result(result):
    print('*{:-^23}*'.format('*'))
    print('|{: ^11}|{: ^11}|'.format('буква', 'частота'))
    print('*{:-^23}*'.format('*'))
    for key, value in result.items():
        print('|{: ^11}|{: ^11}|'.format(key, value))
        print('*{:-^23}*'.format('-'))

def sorted_result(my_result):
    value_sort = sorted(set(my_result.values()), reverse=True)
    sorted_dict = {
        key: my_result[key]
        for i in value_sort
        for key in my_result.keys()
        if my_result[key] == i
    }

    return sorted_dict

file_name = 'voyna-i-mir.zip'
result = alpha_dict(file_name)
result = sorted_result(result)
print_result(result)