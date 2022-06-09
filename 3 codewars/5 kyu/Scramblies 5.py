def scramble(s1, s2):
    sum1 = sum2 = 0
    s1 = list(s1)
    s2 = list(s2)
    for i in range(len(s2)-1):
        if s2[i] in s1:
            sum1 += 1
        else:
            return False
    for i in range(len(s1)-1):
        if s1[i] in s2:
            sum2 += 1
        else:
            return False
    return True
print(scramble('katas', 'steak'))
