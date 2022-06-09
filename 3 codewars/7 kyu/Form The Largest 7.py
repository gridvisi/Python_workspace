def max_number(n):
    n = sorted(list(str(n)),reverse=True)
    num = 0
    for i in n:
        num += int(i)
        num *= 10
    return int(num / 10)
print(max_number(192837465))