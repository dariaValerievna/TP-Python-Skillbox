s, i = input(), input()
counter = 0
for c in range(len(s)):
    if s[c] == i:
        counter += 1
    else:
        break
print(counter)
    
