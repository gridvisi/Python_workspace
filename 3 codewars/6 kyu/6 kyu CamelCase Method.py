'''
https://www.codewars.com/kata/camelcase-method/solutions/python
Write simple .camelCase method (camel_case function in PHP, CamelCase in C# or camelCase in Java) for strings. All words must have their first letter capitalized without spaces.
For instance:
camelcase("hello case") => HelloCase
camelcase("camel case word") => CamelCaseWord
Don't forget to rate this kata! Thanks :)

ALGORITHMSFUNDAMENTALSSTRINGS
'''

def camel_case(string):
    return string.title().replace(" ", "")

def camel_case(string):
    string = list(string)
    if len(string) == 0:
        return ""
    if string[0] == ' ':
        string[0] = ''
        string[1] = chr(ord(string[1]) - 32)
    else:
        string[0] = chr(ord(string[0]) - 32)
    if string[-1] == ' ':
        string[-1] = ''
    for i in range(len(string)):
        if string[i] == ' ':
            string[i] = ''
            string[i+1] = chr(ord(string[i+1])-32)
    string = ''.join(string)
    return string