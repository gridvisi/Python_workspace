def find_longest(string):
    temp = ''
    biggest = 0
    string = list(string)
    string.append(' ')
    output = []
    for i in range(len(string)):
        if not string[i] == ' ':
            temp += string[i]
        if string[i] == ' ':
            output.append(temp)
            temp = ''
    for i in range(len(output)):
        if len(output[i]) > biggest:
            biggest = len(output[i])
    return biggest
print(find_longest("The quick white fox jumped around the massive dog"))