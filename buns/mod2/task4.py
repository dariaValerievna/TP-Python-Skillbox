a = int(input())
a_o = a
a_h = a

#Перевод в двоичную систему
binary = ''
while a>0:
    binary += str(a%2)
    a //= 2
    
#Перевод в восьмиричную систему
octal = ''
while a_o>0:
    octal += str(a_o%8)
    a_o //= 8

#Перевод в шестнадцатиричную систему 
hexadecimal = ''
while a_h>0:
    if a_h%16 == 10:
        hexadecimal += 'A'
    if a_h%16 == 11:
        hexadecimal += 'B'
    if a_h%16 == 12:
        hexadecimal += 'C'
    if a_h%16 == 13:
        hexadecimal += 'D'
    if a_h%16 == 14:
        hexadecimal += 'E'
    if a_h%16 == 15:
        hexadecimal += 'F'
    elif a_h%16 < 10:
        hexadecimal += str(a_h%16)
    a_h //= 16
    
    
print(binary[::-1], octal[::-1], hexadecimal[::-1], sep=', ')
