ip = ['a', 'b', 'c', 'd', 'e']
# delete = 'd'
# op = ['a', 'b', 'c', 'e']


def list_del(arr, ind):
    del(arr[ind])
    return arr


print(list_del(ip, 3))
