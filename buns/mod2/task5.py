i, n = input(), int(input())
s = 'abcdefghijklmnopqrstuvwxyz'
print(s[(s.find(i)+n)%26])