s = input()
even_num = 0
odd_num = 0
for i in range(len(s)):
    if i%2 == 0:
        even_num += int(s[i])
    if i%2 != 0:
        odd_num += int(s[i])
if (even_num + odd_num*3)%10 == 0:
    print('yes')
else:
    print('no')