'''
https://www.codewars.com/kata/shortest-word/solutions/python
Simple, given a string of words, return the length of the shortest word(s).
String will never be empty and you do not need to account for different data types.
test.assert_equals(find_short("bitcoin take over the world maybe who knows perhaps"), 3)
test.assert_equals(find_short("turns out random test cases are easier than writing out basic ones"), 3)
test.assert_equals(find_short("lets talk about javascript the best language"), 3)
test.assert_equals(find_short("i want to travel the world writing code one day"), 1)
test.assert_equals(find_short("Lets all go on holiday somewhere very cold"), 2)
FUNDAMENTALS
'''
def find_short(s):
    return min(len(x) for x in s.split())

def find_short(s):
    if not s:
        return ''
    s= list(s)
    output = []
    num = []
    temp = ""
    for i in range(len(s)):
        if not s[i] == ' ':
            temp += s[i]
        else:
            output.append(temp)
            temp = ""
    output.append(temp)
    for i in range(len(output)):
        num.append(len(output[i]))
    return min(num)