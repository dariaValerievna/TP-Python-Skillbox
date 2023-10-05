s = input()
first_whitespace = s.find(' ')

a = int(s[0:first_whitespace])
b = int(s[first_whitespace:s.find(' ', first_whitespace+1)])
c = int(s[s.find(' ', first_whitespace+1)::])

if -1000<=a<=1000 and -1000<=b<=1000 and -1000<=c<=1000:
    total= a + b + c
    total -= max(a, b, c) + min(a, b, c)
    print(total)
else:
    print("Число выходит за пределы допустимого диапазона")