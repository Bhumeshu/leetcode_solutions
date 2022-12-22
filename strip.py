ip = ["sam is dead", "helo hello", "alphabeta          "]


def check_strip(arr):
    res = []
    for i in arr:
        res.append(str.strip(i))
    return res


print(check_strip(ip))
