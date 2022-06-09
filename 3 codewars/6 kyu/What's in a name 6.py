def name_in_str(str, name):
    str = str.lower()
    name = name.lower()
    str = list(str)
    name = list(name)
    sum = 0
    start = 0
    for i in range(0,len(name)):
        for j in range(start,len(str)):
            if name[i] == str[j]:
                sum += 1
                str[j] = ''
                try:
                    if i + 1 == len(name):
                        return True
                    else:
                        start = str.index(name[i+1])
                except ValueError:
                    return False
            break
    if sum == len(name):
        return True
    else:
        return False
print(name_in_str("crohe rris", "chris"))
'''
Across the rivers
 c      h  ri   s
'''