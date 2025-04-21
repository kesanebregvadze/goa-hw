def points(games):
    num =0
    for i in games:
        x1 = int(i[0])
        x2 = int(i[2])
        if x1 > x2:
            num += 3
        elif x1 == x2:
            num += 1
    return num