s = input()
x = [int(s[x]) for x in range (len(s))]
print('yes' if x.count(0)==x.count(1) else 'no')