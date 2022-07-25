# В текстовом файле удалить все слова, которые содержат хотя бы одну цифру.
# В файле содержится, например:
# Мама сшила м0не штаны и7з бере9зовой кор45ы 893. -> Мама сшила штаны.

import os

path = os.path.join('folder', 'file4hm.txt')

with open(path, 'w') as writer:
    writer.write('Мама сшила м0не штаны и7з бере9зовой кор45ы 893.')

correct_list = []

with open(path, 'r') as reader:
    text = reader.readline()
    print(f'Original text: {text}')
    str_list = [str(x) for x in text.split(' ')]
    for i in range(len(str_list)):
        is_digit = False
        for char in str_list[i]:
            if char.isdigit():
                is_digit = True
        if is_digit == False:
            correct_list.append(str_list[i])

with open(path, 'a') as append:
    append.write(f'\n{" ".join(correct_list)}.')

with open(path, 'r') as reader:
    correct_text = reader.readline()
    correct_text = reader.readline()
    print(f'Correct text: {correct_text}')
