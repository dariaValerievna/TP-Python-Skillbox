import time
def validate_args(func):
    def wrapper(*args):
        if len(args) < 1:
            return "Not enough arguments"
        elif len(args) > 1:
            return "Too many arguments"
        elif not isinstance(args[0], int):
            return "Wrong types"
        elif args[0] < 0:
            return "Negative argument"
        else:
            return func(*args)
    return wrapper

def memoize(func):
    cache = {}
    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]
    return wrapper

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Время выполнения функции {func.__name__}: {end_time - start_time} секунд")
        return result
    return wrapper

@validate_args
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input('Введите аргумент: '))

fib_without_memoize = timer(fibonacci)
print(f'Фибоначчи без memoize с аргументом {n}: ', fib_without_memoize(n))

fibonacci = memoize(fibonacci)
fib_with_memoize = timer(fibonacci)
print(f'Фибоначчи с memoize и аргументом {n}: ', fib_with_memoize(n))