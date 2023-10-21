def count_letters(filename):

    letters_count_lower = {}
    letters_count_upper = {}

    with open(filename, 'r') as file:
        text = file.readline()

        for char in text:
            if char.isalpha():
                if char.islower():
                    if char in letters_count_lower:
                        letters_count_lower[char] += 1
                    else:
                        letters_count_lower[char] = 1
                else:
                    if char in letters_count_upper:
                        letters_count_upper[char] += 1
                    else:
                        letters_count_upper[char] = 1

    sorted_letters_count_lower = dict(sorted(letters_count_lower.items(), key=lambda item: item[1]))
    sorted_letters_count_upper = dict(sorted(letters_count_upper.items(), key=lambda item: item[1]))

    with open('result.txt', 'w') as file:
        file.write('Буквы низкого регистра: \n')
        file.write('')
        for letter, count in sorted_letters_count_lower.items():
            file.write(f'{letter}: {count}\n')

        file.write('Буквы верхнего регистра: \n')
        for letter, count in sorted_letters_count_upper.items():
            file.write(f'{letter}: {count}\n')


filename = input('Введите имя файла: ')
print(count_letters(filename))