def find_short(s):
    if not s:
        return ''
    s= list(s)
    output = []
    num = []
    temp = ""
    for i in range(len(s)):
        if not s[i] == ' ':
            temp += s[i]
        else:
            output.append(temp)
            temp = ""
    output.append(temp)
    for i in range(len(output)):
        num.append(len(output[i]))
    return min(num)
print(find_short("Ripple Monero Monero Lisk"))