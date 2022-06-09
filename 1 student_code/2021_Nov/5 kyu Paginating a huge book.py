'''
https://www.codewars.com/kata/55905b7597175ffc1a00005a/train/python
'''


def page_digits(pages):
    total,p = 0,str(pages)
    for i,e in enumerate(p):
        total += (pages+1 - 10**(len(str(pages))-1)) * (len(str(pages)))
        pages = 10**(len(str(pages))-1)-1
    return total
pages = 100
print(page_digits(pages))



#1st
def page_digits(pages):
    total = 0
    start = 0
    tens = 10
    while pages > start:
        total += pages - start
        start = tens - 1
        tens *= 10
    return total

print([i for i in range(20)])
print([i for i in range(10,20)])