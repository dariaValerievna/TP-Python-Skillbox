s = input()
s = s.replace(' ', '')
flag = True

for i in range(1, len(s)):
    if s[i-1] == s[i]:
        flag = False
        
print(flag)
        