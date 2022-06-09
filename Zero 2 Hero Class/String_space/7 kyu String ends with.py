# https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d/train/python
'''
test.assert_equals(solution('abcde', 'cde'), True)
test.assert_equals(solution('abcde', 'abc'), False)
test.assert_equals(solution('abcde', ''), True)
'''
def solution(string, ending):
    # your code here...
    return string[-len(ending):] == ending if len(ending)>0 else True
string, ending = 'abcde', 'cde'
print(solution(string, ending))

def solution(string, ending):
    return string.endswith(ending)

solution = str.endswith

def solution(string, ending):
    return ending in string[-len(ending):]

solution=str.endswith

def solution(a,b):
    return(a.endswith(b))

