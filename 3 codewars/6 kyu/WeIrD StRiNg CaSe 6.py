def to_weird_case(string):
    string = string.lower()
    string = string.split(' ')
    for i in range(0,len(string)):
        temp = list(string[i])
        for j in range(0,len(temp)):
            if not j % 2:
                temp[j] = chr(ord(temp[j])-32)
        if not i == len(string)-1:
            string[i] = ''.join(temp) + ' '
        else:
            string[i] = ''.join(temp)
    return ''.join(string)



print(to_weird_case('This is a test'))