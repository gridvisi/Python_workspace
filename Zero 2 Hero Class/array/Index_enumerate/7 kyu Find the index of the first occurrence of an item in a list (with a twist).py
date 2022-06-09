'''
https://www.codewars.com/kata/585ba66ce08bae791b00011b/train/python
test.describe("Example Tests")

tests = [ [[['a','b','c'], 'b'],1], [[['b','b','b'], 'b'],1], [[['b','c','b','a'], 'b'],2], [[[0,2,'a','5',0,1,0],0],4]]

for inp, exp in tests:
    test.assert_equals(index_finder(*inp), exp, message="Input: {}".format(inp))
'''

def index_finder(l,x):
    return l.index(x,1)