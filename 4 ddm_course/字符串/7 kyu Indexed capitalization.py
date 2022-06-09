'''
https://www.codewars.com/kata/59cfc09a86a6fdf6df0000f1/train/python


'''

#3rd solution by ericlee
def capitalize(s,ind):
    return ''.join([e.upper() if i in ind else e for i,e in enumerate(s)])

s,ind = "codewarriors",[5]
print(capitalize(s,ind))


#1st solution
def capitalize(s,ind):
    ind = set(ind)
    return ''.join(c.upper() if i in ind else c for i,c in enumerate(s))

#2nd solution
def capitalize(s, ind):
    result = list(s)
    for index in ind:
        try:
            result[index] = result[index].upper()
        except IndexError:
            break  # assumes the indexes are sorted
    return ''.join(result)

