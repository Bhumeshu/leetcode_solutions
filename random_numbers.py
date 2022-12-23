from random import random


def random_number(x):
    rn = []
    for i in range(x):
        x = random()
        rn.append(x)
    return rn


print(random_number(10))
