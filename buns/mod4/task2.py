def fast_power(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return fast_power(a**2, n/2)
    else:
        return a * fast_power(a, n-1)

a = int(input())
n = int(input())
print(fast_power(a, n))
