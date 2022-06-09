# https://www.codewars.com/kata/59e49b2afc3c494d5d00002a/train/python

'''
Sort the Vowels!
In this kata, we want to sort the vowels in a special format.

Task
Write a function which takes a input string s and return a string in the following way:


                  C|                          R|
                  |O                          n|
                  D|                          d|
   "CODEWARS" =>  |E       "Rnd Te5T"  =>      |
                  W|                          T|
                  |A                          |e
                  R|                          5|
                  S|                          T|

Notes:

List all the Vowels on the right side of |
List every character except Vowels on the left side of |
Return every character in its original case
Each line is seperated with \n
Invalid input ( undefined / null / integer ) should return an empty string

'''

def sort_vowels(s):
    if not s or isinstance(s,int)==True:
        return ''
    ans = ''
    for i in s:
        if i.lower() in 'aeiou':
            ans += '|'+i+'\n'
        else:
            ans += i+"|"+'\n'
    return ans[:-1]
s = 'Rnd Te5T'
print(sort_vowels(s))

#1st
def sort_vowels(s):
    try:
        return '\n'.join('|' + i  if i.lower() in 'aioue' else i + '|' for i in s)
    except:
        return ''