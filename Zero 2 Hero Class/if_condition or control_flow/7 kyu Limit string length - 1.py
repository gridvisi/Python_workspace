'''
https://www.codewars.com/kata/5208fc3cb613bc725f000142/train/python

@test.describe('Example Tests')
def example_tests():
    test.assert_equals(solution('Testing String',3), 'Tes...')
    test.assert_equals(solution('Testing String',8), 'Testing ...')
    test.assert_equals(solution('Test', 10), 'Test')
    test.assert_equals(solution('Test', 4), 'Test')

The function must return the truncated version of the given string up to the given
limit followed by "..." if the result is shorter than the original.
Return the same string if nothing was truncated.

Example:

solution('Testing String', 3) --> 'Tes...'
solution('Testing String', 8) --> 'Testing ...'
solution('Test', 8)           --> 'Test'
'''

def solution(st, limit):
    return st if len(st)<= limit else st[:limit] + "..."

st,limit = 'Testing String', 3
print(solution(st, limit))

#1st
def solution(st, limit):
    if len(st) <= limit:
        return st
    return st[:limit] + '...'