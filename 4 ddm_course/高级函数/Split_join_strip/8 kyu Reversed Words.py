'''
https://www.codewars.com/kata/51c8991dee245d7ddf00000e/train/python

Complete the solution so that it reverses all of the words within the string passed in.

Example:

reverseWords("The greatest victory is that which requires no battle")
// should return "battle no requires which that is victory greatest The"
'''

#def splitself()

def reverseWords(s):
    #s = s.split()
    return ' '.join(s.split()[::-1])
s = "The greatest victory is that which requires no battle"
print(s.split())
print(reverseWords(s))

s = "The greatest victory is that which requires no battle"
print(s.split())

print(s.split(' ',3))