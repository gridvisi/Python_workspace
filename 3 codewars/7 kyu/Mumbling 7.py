def accum(s):
    s = s.lower()
    s = list(s)
    output = []
    for i in range(len(s)):
        for j in range(i+1):
            if j == 0 and s[i] >= 'a' and s[i] <= 'z':
                output.append(chr(ord(s[i])-32))
            else:
                output.append(s[i])
        output.append('-')
    output[-1] = ''
    return ''.join(output)
print(accum("ZpglnRxqenU"))