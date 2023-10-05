s = input()
phone_number = ''
#Вводим строку и удаляем из нее все ненужные знаки и пробелы
for i in range(len(s)):
    if s[i] not in '()- ,':
        phone_number += s[i]   
print(phone_number)