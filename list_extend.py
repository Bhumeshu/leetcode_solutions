from typing import List

ip1: list[int] = [1, 2, 3, 4]
ip2 = [5, 6, 7, 8]
op = [1, 2, 3, 4, 5, 6, 7, 8]
def list_extend(x, y):
    x.extend(y)
    return x


print(list_extend(ip1, ip2))