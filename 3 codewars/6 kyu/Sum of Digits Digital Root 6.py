def digital_root(n):
    n = list(str(n))
    summ = 0
    for i in range(len(n)):
        summ += int(n[i])
    return summ


print(digital_root(456))