def palindrome_check(word):
    for i in range(int(len(word)/2)):
        if word[i] != word[-i-1]:
            return False
    return True


d = "wowa"
print(palindrome_check(d))
