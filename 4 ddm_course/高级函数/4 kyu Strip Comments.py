'''

Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas
The code would be called like so:

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
ALGORITHMSSTRINGS
'''

def solution(string,markers):
    parts = string.split('\n')
    for s in markers:
        parts = [v.split(s)[0].rstrip() for v in parts]
    return '\n'.join(parts)

def solution(string,markers):
    string = list(string)
    output = []
    remove_mode = False
    for i in range(len(string)):
        if string[i] in markers and string[i] != chr(92):
            remove_mode = True
            continue
        elif string[i] == ' ' and string[i+1] in markers and i+1 != len(string):
            continue
        elif string[i] == '\n':
            remove_mode = False
            output.append('\n')
        elif not remove_mode:
            output.append(string[i])
    output = ''.join(output)
    return output