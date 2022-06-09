def points(games):
    a = b = point = 0
    str = ''
    for i in range(len(games)):
        str = games[i]
        str = list(str)
        if str[0] > str[2]:
            point += 3
        elif str[0] == str[2]:
            point += 1
        str = ''
    return point
print(points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']))