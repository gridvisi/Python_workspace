'''
https://www.codewars.com/kata/55f2b110f61eb01779000053/train/python

get_sum(1, 0) == 1   // 1 + 0 = 1
get_sum(1, 2) == 3   // 1 + 2 = 3
get_sum(0, 1) == 1   // 0 + 1 = 1
get_sum(1, 1) == 1   // 1 Since both are same
get_sum(-1, 0) == -1 // -1 + 0 = -1
get_sum(-1, 2) == 2  // -1 + 0 + 1 + 2 = 2
'''

def get_sum(a,b):
    a,b = min(a,b),max(a,b)
    return sum([i for i in range(a,b+1)])
#print(get_sum(a,b))

def get_sum(a,b):
    return sum((min(a,b), max(a,b)+1))
a,b = 1, 0
print(get_sum(a,b))

def get_sum(a, b):
    return (a + b) * (abs(a - b) + 1) // 2