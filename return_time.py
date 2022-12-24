import time


def time_now():
    # return time.time()
    x = time.ctime()
    y = x.split()
    return y[3]


print(time_now())
