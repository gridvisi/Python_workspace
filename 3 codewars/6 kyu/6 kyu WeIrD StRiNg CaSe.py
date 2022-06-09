'''
https://www.codewars.com/kata/weird-string-case/train/python

Write a function toWeirdCase (weirdcase in Ruby) that accepts a string, and returns the same
string with all even indexed characters in each word upper cased, and all odd indexed characters
in each word lower cased. The indexing just explained is zero based, so the zero-ith index is
even, therefore that character should be upper cased.

The passed in string will only consist of alphabetical characters and spaces(' '). Spaces
will only be present if there are multiple words. Words will be separated by a single space(' ').

Examples:
to_weird_case('String'); # => returns 'StRiNg'
to_weird_case('Weird string case') # => returns 'WeIrD StRiNg CaSe'

test.it('should return the correct value for a single word')
test.assert_equals(to_weird_case('This'), 'ThIs')
test.assert_equals(to_weird_case('is'), 'Is')

test.it('should return the correct value for multiple words')
test.assert_equals(to_weird_case('This is a test'), 'ThIs Is A TeSt')
ALGORITHMSUTILITIESSTRINGS
'''


def to_weird_case_word(string):
    return "".join(c.upper() if i % 2 == 0 else c for i, c in enumerate(string.lower()))

def to_weird_case(string):
    return " ".join(to_weird_case_word(str) for str in string.split())

def to_weird_case(string):
    recase = lambda s: "".join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(s)])
    return " ".join([recase(word) for word in string.split(" ")])

def to_weird_case(string):
    string = string.lower()
    string = string.split(' ')
    for i in range(0,len(string)):
        temp = list(string[i])
        for j in range(0,len(temp)):
            if not j % 2:
                temp[j] = chr(ord(temp[j])-32)
        if not i == len(string)-1:
            string[i] = ''.join(temp) + ' '
        else:
            string[i] = ''.join(temp)
    return ''.join(string)