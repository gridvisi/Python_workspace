'''
https://www.codewars.com/kata/5a07e5b7ffe75fd049000051/train/python

#Just so you know, you can edit these to better test your
code

#Test cases
test.assert_equals(sorter(['Algebra', 'History', 'Geometry', 'English']), ['Algebra', 'English', 'Geometry', 'History'], 'Does not sort strings')
test.assert_equals(sorter(['Algebra', 'history', 'Geometry', 'english']), ['Algebra', 'english', 'Geometry', 'history'], 'Does not handle capitalization')
test.assert_equals(sorter(['Alg#bra', '$istory', 'Geom^try', '**english']), ['$istory', '**english', 'Alg#bra', 'Geom^try'], 'Does not handle symbols')
'''
print('s'.upper())
print('S'.casefold())
print('s'.isascii())
print(ord('s'))
def sorter(textbooks):
    return sorted(textbooks,key=lambda x:x.lower())

def sorter(textbooks):
    return sorted(textbooks,key=lambda x:ord(x.upper()[0]))
textbooks = ['Algebra', 'history', 'Geometry', 'english']
print(sorter(textbooks))


#1st
def sorter(textbooks):
    return sorted(textbooks,key=str.lower)

#2nd
def sorter(textbooks):
    return sorted(textbooks, key=str.casefold)