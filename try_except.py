def try_except(fpath):
    try:
        fin = open(fpath, 'r')
        for line in fin:
            print(line)
        fin.close()
        return "operation completed"
    except Exception as e:
        return e


print(try_except('readfile.txt'))
