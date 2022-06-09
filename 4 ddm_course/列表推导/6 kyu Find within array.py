'''
1002,4kyiu = eric
You have unlocked a new privilege!
1000+ Honor: You now have 2x kata voting power!

https://www.codewars.com/kata/51f082ba7297b8f07f000001/train/python


    test.assert_equals(find_in_array([], true_if_even) , -1)
    test.assert_equals(find_in_array([1,3,5,6,7], true_if_even) , 3)
    test.assert_equals(find_in_array([2,4,6,8], true_if_even) , 0)
    test.assert_equals(find_in_array([2,4,6,8], never_true) , -1)
    test.assert_equals(find_in_array([13,5,3,1,4,5], true_if_value_equals_index) , 4)
    test.assert_equals(find_in_array(["one","two","three","four","five","six"], true_if_length_equals_index) , 4)
    test.assert_equals(find_in_array(["bc","af","d","e"], true_if_length_equals_index) , -1)
'''

true_if_even = lambda value, index: value % 2 == 0
true_if_length_equals_index = lambda value, index: len(value) == index

seq, predicate = ["one","two","three","four","five","six"], true_if_length_equals_index
seq, predicate = [1,3,5,6,7],true_if_even

def find_in_array(seq, predicate):
    re = list(map(predicate,seq,[i for i in range(len(seq))]))
    print(re)
    #res = filter(lambda x:x==True,map(predicate,seq,[i for i in range(len(seq))]))
    return re.index(True) if True in re else -1

print(find_in_array(seq, predicate))

#Top 1st
def find_in_array(seq, fn):
    return next((i for i, j in enumerate(seq) if fn(j, i)), -1)

print(next(i if i % 2==0 else -1 for i in [1,4,6,9]))
print(next(i for i in [7,4,1,4,6,8,9] if i % 2==0),-1)