def solve(s):
    s = list(s)
    words = ['a','e','i','o','u']
    numbers = []
    sum = 0
    for i in range(len(s)):
        if s[i] in words:
            s[i] = ''
    for i in range(len(s)):
        if not s[i] == '':
            sum += ord(s[i])-96
        if s[i] == '' and sum:
            numbers.append(sum)
            sum = 0
    numbers.append(sum)
    return sorted(numbers)[-1]
print(solve("zodiacs"))