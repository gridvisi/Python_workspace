def wave(str):
    str = list(str)
    output = []
    strlen = len(str)
    for i in range(0,strlen):
        if ord(str[i])>96 and ord(str[i])<123:
            str[i] = chr(ord(str[i])-32)
            output.append(''.join(str))
            str[i] = chr(ord(str[i])+32)
    return output
print(wave("hello"))
