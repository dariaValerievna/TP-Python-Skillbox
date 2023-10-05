s = input()
s = s.replace(' ', '')
flag = False

for i in range(1, len(s)):
    if s[i-1] == s[i]:
        flag = True
        
print(flag)
        