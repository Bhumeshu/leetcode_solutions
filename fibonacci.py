def fibonacci(n):
    assert n != 0, "invalid"
    # if n == 0:
    #     raise Exception
    if n == 1:
        return int(0)
    if n == 2:
        return int(1)
    # input("Are you sure? please hit enter to proceed")
    return fibonacci(n-2) + fibonacci(n-1)


print(fibonacci(5))
