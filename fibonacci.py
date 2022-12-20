def fibonacci(n):
    if n == 1:
        return int(0)
    if n == 2:
        return int(1)
    return fibonacci(n-2) + fibonacci(n-1)


print(fibonacci(19))
