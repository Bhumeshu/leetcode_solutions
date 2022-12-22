ip = ['1', 'b', '9', 'd']


# op = ['A', 'B' , 'C', 'D']

def list_capitalize(ip_list):
    arr = []
    for i in ip_list:
        arr.append(str.upper(i))
    return arr


print(list_capitalize(ip))
