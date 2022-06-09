'''
https://www.codewars.com/kata/57e35f1bc763b8ccce000038/train/python
Between 8 - 20 characters
Contains only the following characters (and at least one character from each category):
uppercase letters,
lowercase letters,
digits,
special characters from !@#$%^&*?
test.describe('Basic Tests')
test.assert_equals(check_password(""), "not valid")
test.assert_equals(check_password("password"), "not valid")
test.assert_equals(check_password("P1@p"), "not valid")
test.assert_equals(check_password("P1@pP1@p"), "valid")
test.assert_equals(check_password("P1@pP1@pP1@pP1@pP1@pP1@p"), "not valid")
test.assert_equals(check_password("Paaaaaa222!!!"), "valid")

'''
import string
s = "Paaaaaa222!!!"
import string
def check_password(s):
    valid_1,valid_2,valid_3,valid_4 = 0,0,0,0
    for e in s:
        if e in string.ascii_lowercase:
            valid_1 = 1
        if e in string.ascii_uppercase:
            valid_2 = 1
        if e in string.digits:
            valid_4 = 1
        if e in "!@#$%^&*?":
            valid_3 = 1
    return "not valid" if valid_1*valid_2*valid_3*valid_4 == 0 else "valid"

#1st
import re
def check_password(s):
    if re.search('^(?=.*?[a-z])(?=.*?[A-Z])(?=.*?\d)(?=.*?[!@#$%^&*?])[a-zA-Z\d!@#$%^&*?]{8,20}$', s) :
        return 'valid'
    else:
        return 'not valid'

#2nd
import re

PATTERN = re.compile(
'^'                   # begin string
'(?=.*?[A-Z])'        # at least one uppercase letter
'(?=.*?[a-z])'        # at least one lowercase letter
'(?=.*?\d)'           # at least one digit
'(?=.*?[!@#$%^&*?])'  # at least one special character
'[A-Za-z\d!@#$%^&*?]' # only the given characters
'{8,20}'              # between 8 and 20 characters long
'$'                   # end string
)

def check_password(s):
    return "valid" if PATTERN.match(s) else "not valid"

#4nd
def check_password(s):
    c1 = 8 <= len(s) <=20
    c2 = any([i.isupper() for i in s])
    c3 = any([i.islower() for i in s])
    c4 = any([i.isdigit() for i in s])
    c5 = any([i for i in s if i in '!@#$%^&*?'])
    c6 = not any([i for i in s if i not in '!@#$%^&*?' and not i.isupper() and not i.islower() and not i.isdigit()])
    return 'valid' if c1 and c2 and c3 and c4 and c5 and c6 else 'not valid'