def stray(s):
    word2 = []
    for i in s:
        if i in word2:
            word2.remove(i)
        elif i not in word2:
            word2.append(i)
    return word2[0]
    