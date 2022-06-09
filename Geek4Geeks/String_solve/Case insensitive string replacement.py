'''
https://www.geeksforgeeks.org/python-case-insensitive-string-replacement/?ref=rp

Given a string of words. The task is to write a Python program to replace the given word irrespective of the case with the given string.

Examples:

Input : test_str = “gfg is BeSt”, repl = “good”, subs = “best”

Output : gfg is good

Explanation : BeSt is replaced by “good” ignoring cases.

Method #1 : Using re.IGNORECASE + re.escape() + re.sub()
In this, sub() of regex is used to perform task of replacement and IGNORECASE,
ignores the cases and performs case-insensitive replace.
'''

# Python3 code to demonstrate working of
# Case insensitive Replace
# Using re.IGNORECASE + re.escape() + re.sub()
import re

# initializing string
test_str = "gfg is BeSt"

# printing original string
print("The original string is : " + str(test_str))

# initializing replace string
repl = "good"

# initializing substring to be replaced
subs = "best"

# re.IGNORECASE ignoring cases
# compilation step to escape the word for all cases
compiled = re.compile(re.escape(subs), re.IGNORECASE)
res = compiled.sub(repl, test_str)

# printing result
print("Replaced String : " + str(res))

'''
Method #2 : Using sub() + lambda + escape() 

Using particular ignore case regex also this problem can be solved. Rest, 
a lambda function is used to handle escape characters if present in the string. 
'''
# Python3 code to demonstrate working of
# Case insensitive Replace
# Using sub() + lambda + escape()
import re

# initializing string
test_str = "gfg is BeSt"

# printing original string
print("The original string is : " + str(test_str))

# initializing replace string
repl = "good"

# initializing substring to be replaced
subs = "best"

# regex used for ignoring cases
res = re.sub('(?i)' + re.escape(subs), lambda m: repl, test_str)

# printing result
print("Replaced String : " + str(res))


