# https://www.codewars.com/kata/598f76a44f613e0e0b000026/train/python
'''

test.describe("Example test cases")

exampleTests = (
("12.4", 16),
("h3ll0w0rld", 3),
("2 + 3 = ", 5),
("Our company made approximately 1 million in gross revenue last quarter.", 1),
("The Great Depression lasted from 1929 to 1939.", 3868),
("Dogs are our best friends.", 0),
("C4t5 are 4m4z1ng.", 18),
("The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog", 3635)
)

for testString, correctAnswer in exampleTests:
    test.assert_equals(sum_of_integers_in_string(testString), correctAnswer)

Your task in this kata is to implement a function that calculates
the sum of the integers inside a string.
For example, in the string
"The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog",
the sum of the integers is 3635.
'''

#1st
def sum_of_integers_in_string(s):
    return sum(map(int, ''.join(c if c.isdigit() else ' ' for c in s).split()))

#2nd
import re
def sum_of_integers_in_string(s):
    return sum(int(x) for x in re.findall(r"(\d+)", s))

import string
def sum_of_integers_in_string(s):
    #sl = [i for i in s if i not in string.ascii_letters]
    #sl = [i if not i.isalpha() else " " for i in s]
    sl = [i if i.isnumeric() else " " for i in s]
    ans = 0
    for n in ''.join(sl).split(" "):
        if n != '':
            ans += eval(n)
    return int(ans)
s= "The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog"
s = "12.4"
print(sum_of_integers_in_string(s))

#print(eval('034'))
#print(int('034'))
#SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers

#while try
def sum_of_integers_in_string(s):
    i,j = 0,1
    num = 0
    while j<len(s)-1:
        if s[i] not in "123456789":
            i += 1
            j = i+1

        elif s[i] in "123456789" and s[j] in "0123456789":
            j += 1

        elif s[i] in "123456789" and s[j] not in "0123456789":
            num += eval(s[i:j])
            i = j+1
            j = i+1

    return num
s = 'e01t34'
print(sum_of_integers_in_string(s))