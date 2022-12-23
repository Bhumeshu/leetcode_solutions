def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise ValueError


print(reverse_lookup({'a': 1, 'b': 2, 'c': 3, 'sam': 'alpha'}, 'alpha'))
