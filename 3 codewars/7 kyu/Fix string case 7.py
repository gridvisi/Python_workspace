def solve(s):
    s = list(s)
    big = 0
    small = 0
    for i in s:
        if ord(i) > 64 and ord(i) < 91:
            big += 1
        if ord(i) > 96 and ord(i) < 123:
            small += 1
    if big > small:
        return ''.join(s).upper()
    elif small > big or small == big:
        return ''.join(s).lower()
print(solve("CODe"))