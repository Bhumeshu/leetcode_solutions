def invert_dict(d):
    inv = dict()
    for key in d:  # a,b,c
        val = d[key]  # d[a], val = 1
        if val not in inv:  # 1 not in {}
            inv[val] = [key]  # inv[1] = ['a'], inv {1: 'a'}
        else:
            inv[val].append(key)
    return inv


print(invert_dict({'a': 1, 'b': 2, 'c': 3, 'd': 1}))
