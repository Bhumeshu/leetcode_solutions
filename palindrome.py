def palindrome_check(word):
    count = 0
    # for i in range(int(len(word)/2)):
    #     count += 1
    #     if word[i] != word[-i-1]:
    #         return False, count
    # return True, count
    a = list(word)
    b = list(word)
    print(b)
    b.reverse()
    print(b)
    if a == b:
        return True
    else:
        return False


d = "9424927"
print(palindrome_check(d))
