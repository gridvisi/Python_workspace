def find_outlier(integers):
    temp = []
    for i in integers:
        if i % 10 == 0 or i % 10 == 2 or i % 10 == 4 or i % 10 == 6 or i % 10 == 8:
            temp.append(1)
        else:
            temp.append(0)
    if temp.count(1) == 1:
        return integers[temp.index(1)]
    elif temp.count(0) == 1:
        return integers[temp.index(0)]
print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))
'''
def find_outlier(int):
    odds = [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]
'''