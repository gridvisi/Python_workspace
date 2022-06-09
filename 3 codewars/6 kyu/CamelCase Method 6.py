def camel_case(string):
    string = list(string)
    if len(string) == 0:
        return ""
    if string[0] == ' ':
        string[0] = ''
        string[1] = chr(ord(string[1]) - 32)
    else:
        string[0] = chr(ord(string[0]) - 32)
    if string[-1] == ' ':
        string[-1] = ''
    for i in range(len(string)):
        if string[i] == ' ':
            string[i] = ''
            string[i+1] = chr(ord(string[i+1])-32)
    string = ''.join(string)
    return string


print(camel_case(" camel case word"))