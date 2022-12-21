def compare_string(str1, str2):
    if str1 == str2:
        return True
    if len(str1) < len(str2):
        if str1 in str2:
            return "str1 is subset of str2"
    if len(str1) > len(str2):
        if str2 in str1:
            return "str2 is subset of str1"


print(compare_string('apple', 'app'))
