s = input()
#Вводим строку и удаляем из нее все ненужные знаки и пробелы
s = s.replace('-', '').replace(')', '').replace('(', '').replace(' ', '')
print(s)