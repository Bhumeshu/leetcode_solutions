ip = ['a', 'b', 'c', 'd', 'e']
# delete = 'e'
# op = ['a', 'b', 'c', 'e']


def demo_pop(arr, ind):
    return arr, arr.pop(ind)


print(demo_pop(ip, 2))
