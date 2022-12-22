ip = ['a', 'c', 'e', 'g', 'k']
letter = 'i'
# op = [a,c,e,g,i,k]


def list_append(x, y):
    x.append(y)
    return x


print(list_append(ip, letter))
