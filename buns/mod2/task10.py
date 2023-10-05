s = input()
word = ''
for i in range(len(s)):
    if s[i] == ' ':
        word += s[i-1]
word += s[-1]
print(word)