itg = "6:52"


def calculate_time(it, x):
    ith = int(it.split(":")[0])
    itm = int(it.split(":")[1])
    if x < (60-itm):
        return f"{ith}:{itm+x}"
    if x >= (60 - itm):
        y = x - (60-itm)
        return f"{ith+int(x/60)}:{y%60}"


print(calculate_time(itg, 1))
