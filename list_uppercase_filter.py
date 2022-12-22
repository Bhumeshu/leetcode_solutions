ip = ['SAM', 'b', 'C', 'disk']


def check_uppercase(arr):
    for i in arr:
        if not str.isupper(i):
            return False
    return True


print(check_uppercase(ip))


def filter_uppercase(arr):
    new_arr = []
    for i in arr:
        if str.isupper(i):
            new_arr.append(i)
    return new_arr


print(filter_uppercase(ip))
