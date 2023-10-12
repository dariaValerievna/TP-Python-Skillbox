s = input()
print(*[s[i-1] for i in range(len(s)) if s[i]==' '], s[-1], sep = '')