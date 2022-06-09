'''
https://www.codewars.com/kata/584d2c19766c2b2f6a00004f/train/python
'''
#1st
def func_or(a, b):
    return not (bool(a) == bool(b) == False)

def func_xor(a, b):
    return not (bool(a) == bool(b))

#2nd
def func_or(a,b):
    return bool(a) | bool(b)

def func_xor(a,b):
    return bool(a) ^ bool(b)

#4th
def func_or(*a):
    return any(a)

def func_xor(*a):
    return any(a) and not all(a)



print(1 ^ 1)
print(1 | 1)

print(1 ^ 0)
print(1 | 0)

print(0 ^ 0)
print(0 | 0)

print(None == 0)

print(-4 or 6)
print(4 ^ 6)
print(-4 | 6)
print(2 or 3)
print(2 and 3)


def func_or(a,b):
    #your code here - do no be lame and do not use built-in code!
    return a or (b >= 1 if type(b) != list else len(b))

def func_xor(a,b):
    #your code here - remember to consider truthy and falsey value as in JS
    return a | (b>=1 if type(b) != list else len(b))

