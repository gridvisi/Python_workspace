def multi_table(number):
    strr = ''
    output = ''
    for i in range(1,11):
        strr = strr + str(number)+" * "+str(i)+" = "+str(number*i)+r'\n'
    strr = list(strr)
    for i in range(len(strr)-2):
        output = strr[i] + output
    return output
print(multi_table(5))