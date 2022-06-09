'''
https://www.codewars.com/kata/5aee86c5783bb432cd000018/train/python
@test.describe('Example Tests')
def example_tests():
    test.assert_equals(hydrate("1 beer"), "1 glass of water")
    test.assert_equals(hydrate("1 shot, 5 beers, 2 shots, 1 glass of wine, 1 beer"), "10 glasses of water")
'''
x = '1'
print(isinstance(x, str))
print()

drink_string = "1 shot, 5 beers, 2 shots, 1 glass of wine, 1 beer"
d = drink_string.split(',')
num = [n.split(' ') for n in d]
print(d)
print(num)

n_filt = [i for i in drink_string if not i.isalpha() or not ' ']

print(n_filt)

import string

print(string.ascii_letters)


def hydrate(drink_string):
    '''
    #n_filt = [i for i in drink_string if not i.isalpha()]
    str_filt = [i for i in drink_string if i not in string.ascii_letters+' ,']
    return str(sum([int(i) for i in str_filt]))
    '''
    return sum([int(i) for i in drink_string if '0' <= i <= '9'])

print('2' > '1')

print('ddm','1' + '2')
print('ddm2',1 + 2)

# sum([int(i) for i in n_filt if i != ' '])
print(hydrate(drink_string))
