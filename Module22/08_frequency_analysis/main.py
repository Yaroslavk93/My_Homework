import os
text = 'Mama myla ramu.'
text_file = open(os.path.abspath(os.path.join('text.txt')), 'w')
text_file.write(text)

my_dict = dict()
for letter in text.lower():
    if letter in my_dict or not letter.isalpha():
        pass
    else:
        my_dict[letter] = text.lower().count(letter)


sorted_dict = dict()
for index in reversed(sorted(set(my_dict.values()))):
    for key in sorted(my_dict.keys()):
        if my_dict[key] == index:
            sorted_dict[key] = my_dict[key]

text_file.close()


analysis_file = open(os.path.abspath(os.path.join('analysis.txt')), 'w')
for key, value in sorted_dict.items():
    analysis_file.write(f'{key}: {str(round((value / sum(my_dict.values())), 3))}\n')
analysis_file.close()
