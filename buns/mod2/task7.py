s = input()
count_0 = 0
count_1 = 0
for i in range(len(s)):
    if s[i] == '0':
        count_0 += 1
    if s[i] == '1':
        count_1 += 1
     
if count_0 == count_1:
    print('yes')
else:
    print('no')