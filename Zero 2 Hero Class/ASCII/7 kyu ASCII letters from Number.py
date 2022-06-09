'''
https://www.codewars.com/kata/589ebcb9926baae92e000001/train/python

You have to create a function that converts integer given as string into ASCII uppercase letters.

All ASCII characters have their numerical order in table.

For example,

from ASCII table, character of number 65 is "A".
Numbers will be next to each other, So you have to split given number to two
digit long integers.

For example,

'658776' to [65, 87, 76] and then turn it into 'AWL'.
Good Luck!

Test.assert_equals(convert("65"),"A")
Test.assert_equals(convert("656667"),"ABC")
Test.assert_equals(convert("676584"),"CAT")
Test.assert_equals(convert("73327673756932858080698267658369"),"I LIKE UPPERCASE")
'''
print(chr(65))

def convert(number):
    return ''.join([chr(eval(number[i:i+2])) for i in range(0,len(number),2)])
#''.join(map(chr(eval()),number[0:len(number):2]))
#
number = "676584"
print(number[0:len(number):2])
print(convert(number))

def convert(number):
    ans = ''
    for i in range(0,len(number),2):
        ans += chr(eval(number[i:i+2]))# number[i:i+2]
    return ans


#1st
def convert(number):
    return ''.join(chr(int(number[a:a + 2])) for a in range(0, len(number), 2))