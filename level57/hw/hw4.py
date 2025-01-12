def digitize(n):
    x  = str(n)
    result = []
    for x in x:
        result.append(int(x))
    return result[::-1]