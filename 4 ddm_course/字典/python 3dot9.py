'''
https://medium.com/better-programming/dictionary-merging-and-updating-in-python-3-9-4ac67c667ce
'''
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d2a = {'a': 10, 'c': 3, 'd': 4}
# unpacking
d3 = {**d1, **d2a}
# d3 is {'a': 10, 'b': 2, 'c': 3, 'd': 4}
# Not right
print(d3)
d3 = {**d2a, **d1}
# d3 is {'a': 1, 'c': 3, 'd': 4, 'b': 2}
# Good
print(d3)

d3 = dict(d1, **d2)
# d3 is {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# Good, it's what we want
d3 = dict(d1, **d2a)
# d3 is {'a': 10, 'b': 2, 'c': 3, 'd': 4}
# Not right, 'a' value got replaced

# use the merging operator |
d3 = d1 | d2
# d3 is now {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# good
d3 = d1 | d2a
# d3 is now {'a': 10, 'b': 2, 'c': 3, 'd': 4}
# not good