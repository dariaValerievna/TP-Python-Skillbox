with open('количество сделанных шагов.txt', 'r') as file:
    n = file.readline()

n = int(n)
x, y = 0, 0
step = 0

while step != n:
    if x == y and x >= 0:
        while x != -y - 1 and step != n:
            step += 1
            x -= 1
    elif x == -y:
        while x != y and x > 0 and step != n:
            step += 1
            y += 1

    elif x == y and x < 0:
        while x != -y and step != n:
            step += 1
            x += 1

    else:
        while x != y and x < 0 and step!= n:
            step += 1
            y -= 1

with open('количество сделанных шагов.txt', 'a') as file:
    file.write('\n' + str(x) + ' ' + str(y))


