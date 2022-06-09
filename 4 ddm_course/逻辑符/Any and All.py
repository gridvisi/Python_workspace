'''
Python provides two unique built-in functions that allow us to check
if all elements in an iterable are True, and if any element is True.
These functions are aptly named all and any.
'''


#if student[s] == "python" and student[s] == english:

all_true = [True, True, 1, 'hello']
any_true = [0, False, True, '', []]
# all(all_true) == True
# any(all_true) == True
# all(any_true) == False
# any(any_true) == True

print(all_true,all(all_true),any(all_true),all(any_true),any(any_true))

our_list = [1, 2, 3]
a, b, c = our_list
print(a,b,c)