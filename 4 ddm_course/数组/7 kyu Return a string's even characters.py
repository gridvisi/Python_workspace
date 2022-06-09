'''
https://www.codewars.com/kata/566044325f8fddc1c000002c/train/python
Write a function that returns a sequence (index begins with 1) of all the even characters from a string. If the string is smaller than two characters or longer than 100 characters, the function should return "invalid string".
For example:
"abcdefghijklm" --> ["b", "d", "f", "h", "j", "l"]
"a"             --> "invalid string"

@test.describe('Example Tests')
def example_tests():
    test.assert_equals(even_chars("a"), "invalid string")
    test.assert_equals(even_chars("abcdefghijklm"), ["b", "d", "f", "h", "j", "l"])
'''

def even_chars(st):
    ans = [e for i,e in enumerate(st) if i%2 == 1]
    return ans if 2 < len(ans) < 100 else "invalid string"
st = "aBc_e9g*i-k$m"
print(even_chars(st))

'''
Time: 837ms Passed: 106 Failed: 0
Test Results:
 Fixed Tests
 Basic Test Cases (3 of 3 Assertions)
 Edge Cases (3 of 3 Assertions)
Completed in 0.10ms
 Random Tests
 Random Test Cases (100 of 100 Assertions)
Completed in 4.02ms
You have passed all of the tests! :)
'''