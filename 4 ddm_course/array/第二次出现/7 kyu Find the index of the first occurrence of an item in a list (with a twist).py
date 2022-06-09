'''
https://www.codewars.com/kata/585ba66ce08bae791b00011b/train/python

Write a function index_finder/index-finder that returns the index of the first occurrence of an item (x) in the list (lst), but ignoring the first item in the list. The item will always occur at least once after the first item in the list. For example:

lst = ['a','b','c'], x = 'b' >>> returns 1 ('b' occurs first at position 1)

lst = ['b','b','b'], x = 'b' >>> returns 1 ('b' occurs first at position 1 if you ignore index 0)

lst = ['b','c','b','a'], x = 'b' >>> returns 2 ('b' occurs first at position 2 if you ignore index 0)

lst = [0,2,'a','5',0,1,0], x = 0 >>> returns 4 (0 occurs first at position 4 if you ignore index 0)
'''

def index_finder(lst, x):

    return [i for i,e in enumerate(lst) if e == x][1]
lst = [0,2,'a','5',0,1,0]
x = 0
print(index_finder(lst, x))

def index_finder(l,x):
    return l.index(x,1)

'''
def index_finder(lst, x):
    cunt = 0
    #while cunt <= 2:
    for i,c in enumerate(lst):
        if c != x and cunt <= 2:
            pass
        elif c == x and cunt <= 2:
            cunt += 1
            idx = i
    return idx

'''

ages = ['11','13','11','10','13','11']
print(ages.index('11'))
print(ages.index('11',0))
print(ages.index('11',1))
print(ages.index('11',2))
print(ages.index('11',3))

#index(variable,start_index)