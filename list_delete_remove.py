ip = ['a', 'b', 'c', 'd', 'e']
to_remove = 'a'
# op   = ['b', 'c', 'd', 'e']


def list_remove(arr, ele):
    arr.remove(ele)
    return arr


print(list_remove(ip, to_remove))
