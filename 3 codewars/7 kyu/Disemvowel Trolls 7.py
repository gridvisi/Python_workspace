
def disemvowel(string):
    strr = list(string)
    output = []
    for i in range(len(strr)):
        if strr[i] != 'i'and strr[i] != 'I':
            if strr[i] != 'o'and strr[i] != 'O':
                if strr[i] != 'e'and strr[i] != 'E':
                    if strr[i] != 'b' and strr[i] != 'B':
                        if strr[i] != 'u' and strr[i] != 'U':
                            if strr[i] != 'a' and strr[i] != 'A':
                                output.append(strr[i])
    output = ''.join(output)
    return output
print(disemvowel("This website is for losers LOL!"))