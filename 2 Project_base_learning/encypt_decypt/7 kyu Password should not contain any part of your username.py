'''
https://www.codewars.com/kata/5c511d8877c0070e2c195faf/train/python

You are writing a password validator for a website. You want to discourage users from
using their username as part of their password, or vice-versa, because it is insecure.
Since it is unreasonable to simply not allow them to have any letters in common,
you come up with this rule:

For any password and username pair, the length of the longest common substring should
be less than half the length of the shortest of the two.

In other words, you won't allow users to have half their password repeated in their
username, or half their username repeated in their password.

Write a function validate(username, password) which returns true if your rule is
followed, false otherwise.

Assume:

Both the username and the password may contain uppercase letters, lowercase letters,
numbers, spaces, and the following special/punctation characters: !@#$%^&*()_+{}:"<>?[];',.
The username and password will each be less than 100 characters.
FUNDAMENTALSREGULAR EXPRESSIONSDECLARATIVE PROGRAMMINGADVANCED LANGUAGE FEATURESSTRINGSVALIDATIONALGORITHMS


import codewars_test as test
# TODO Write tests
import solution # or from solution import example

# test.assert_equals(actual, expected, [optional] message)
@test.describe("Example")
def test_group():
    @test.it("test case")
    def test_case():
        test.assert_equals(validate("", ""), False)
        test.assert_equals(validate("username", "myname"), False)
        test.assert_equals(validate("sword", "password" ), False)
        test.assert_equals(validate("qwertyuiop", "asdfghjkl"), True)
        test.assert_equals(validate("MASH", "M*A*S*H"), True)
        test.assert_equals(validate("asdfghjkl", "lkjhgfdsa"), True)
'''
username, password = "MASH", "M*A*S*H"
username, password = "sword", "password"
username, password = "username", "myname"
s, t = sorted((username, password), key=len)
print(s,t)
print(sum(divmod(len(s), 2)))

import re
#print(re.findall(username,password))

def validate(username, password):
    #start = [i for i in username if i in password]
    #it = iter(password)
    common = ''
    #start = [e for e in it if e in username]
    start = [e for e in password if e in username]
    ans = [(x,y) for x,y in zip(username,password)]
    return ans,start
print(validate(username, password))

#Not suit very well solution
def validate(username, password):
    return password not in username and username not in password


#1st solution
def validate(username, password):
    s, t = sorted((username, password), key=len)
    h = sum(divmod(len(s), 2))
    return all(t[a:a + h] not in s for a in range(len(t) - h + 1))
# 50%的字符串不同！

import math
def validate(username, password):
    print(username, password)
    short_half = math.ceil(min(len(username), len(password)) / 2.0)
    maxIdx = len(username) - short_half

    for i in range(maxIdx + 1):
        substr = username[i: i + short_half]
        if substr in password: return False

    return True
'''
    for i in username:
        for j in password:
            if i == j:
                print(i,j)
                common = [username.index(i),password.index(j)]
                break
'''