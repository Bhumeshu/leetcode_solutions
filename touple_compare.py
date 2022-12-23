def sort_by_length(words):
    t = []
    for word in words:  # word = sam
        t.append((len(word), word))
        print(t)
    t.sort(reverse=True)
    print(t)
    res = []
    for length, word in t:
        res.append(word)
    return res


print(sort_by_length(["sam", "is", "alive"]))
