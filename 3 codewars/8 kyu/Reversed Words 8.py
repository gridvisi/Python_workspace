def reverseWords(str):
    str = str.split(' ')
    str = sorted(str,reverse=False)
    output = ""
    for i in str:
        output += i + ' '
    output = output[:-1]
    return output
print(reverseWords('kata editor'))