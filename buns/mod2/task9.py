s = input()
counter_g = 0
counter_s = 0
for i in range(len(s)):
    if s[i] in 'аеёиоуыэю':
        counter_g += 1
    if s[i] in 'бвгджзйклмнпрстфхчцшщ':
        counter_s += 1
print(counter_g, counter_s)       
    
