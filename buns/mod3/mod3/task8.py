s = input() 
print(*[s[i] for i in range(len(s)) if s[i] not in '()- ,'], sep ='')