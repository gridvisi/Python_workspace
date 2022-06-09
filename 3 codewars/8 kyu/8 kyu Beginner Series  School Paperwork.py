'''
Your classmates asked you to copy some paperwork for them.
You know that there are 'n' classmates and the paperwork has 'm' pages.
Your task is to calculate how many blank pages do you need.
Example:
paperwork(5, 5) == 25
'''
def paperwork(n, m):
    if n > 0 and m > 0:return n*m
    else:0

def paperwork(n, m):
    return n * m if n > 0 and m > 0 else 0
n, m = 5,-5
s = paperwork(n, m)
print(paperwork(n, m))
print(f"{n}")