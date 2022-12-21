def counter(word, x):
    _count = 0
    for i in word:
        if i == x:
            _count = _count + 1
    return _count


print(counter("however", 'e'))

