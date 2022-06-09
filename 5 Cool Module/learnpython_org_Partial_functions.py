'''
https://www.learnpython.org/en/Partial_functions
'''

from functools import partial

def multiply(x,y):
        return x * y

# create a new function that multiplies by 2
dbl = partial(multiply,9)
print(dbl(4))


#Following is the exercise, function provided:
from functools import partial
def func(u,v,w,x):
    return u*4 + v*3 + w*2 + x
#Enter your code here to create and print with your partial
# function

from functools import partial
def func(u,v,w,x):
    return u*4 + v*3 + w*2 + x

p = partial(func,5,6,7)
print(p(10))  #hint x = 8