def has_match(t1, t2):
    assert type(t1) in [tuple] and type(t2) in [tuple], "invalid input"
    for x, y in zip(t1, t2):
        print(x, y)
        if x == y:
            return True
    return False


print(has_match({1, 2, 3}, ('a', 'b', 3)))
