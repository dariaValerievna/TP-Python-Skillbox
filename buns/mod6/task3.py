def armstrong_numbers():
    for number in range(10, 1000000):
        power = len(str(number))
        armstrong_sum = sum([int(digit) ** power for digit in str(number)])
        if armstrong_sum == number:
            yield number

armstrong_generator = armstrong_numbers()
def get_armstrong_numbers():
    return next(armstrong_generator)

for i in range(8):
    print(get_armstrong_numbers(), end=' ')

