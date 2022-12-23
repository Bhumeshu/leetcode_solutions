def readfile(file_path, extras):
    out = open(file_path, 'w')
    out.write(extras)
    out.close()
    return out


txt = "\noh my"
print(readfile("readfile.txt", txt))
