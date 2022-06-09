def match_arrays(v, r):
    sum = 0
    for i in v:
        for j in r:
            if i == j:
                sum += 1
    return sum
print(match_arrays([True,3,9,11,15],[True,3,11]))