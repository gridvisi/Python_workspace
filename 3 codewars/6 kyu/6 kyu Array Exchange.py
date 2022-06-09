'''
https://www.codewars.com/kata/5353212e5ee40d4694001114/train/python
# before
my_list = ['a', 'b', 'c']
other_list = [1, 2, 3]

exchange_with(my_list, other_list)

# after
my_list == [3, 2, 1]
other_list == ['c', 'b', 'a']
'''
a = ['a', 'b', 'c']
b = [1, 2, 3]

a = ["1", "2", "3", "4", "5", "6", "7"]
b = ["a", "b", "c"]
def exchange_with(a, b):
    a,b = b[::-1],a[::-1]
    return a, b
print(exchange_with(a, b))
def exchange_with(a, b):
    a[:], b[:] = b[::-1], a[::-1]

def exchange_with(a, b):
    c = a.copy()
    a.clear()
    while b:
        a.append(b.pop())
    while c:
        b.append(c.pop())
print(exchange_with(a, b))