def factor(n):
    total = 1
    while n >= 1:
        _sum = n * (n - 1)
        n = n-2
        total = total * _sum
    return total


print(factor(4))



