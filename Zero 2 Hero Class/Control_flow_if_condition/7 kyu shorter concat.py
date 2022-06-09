'''
https://www.codewars.com/kata/54557d61126a00423b000a45/solutions/python

test.assert_equals(shorter_reverse_longer("first", "abcde"),"abcdetsrifabcde");
test.assert_equals(shorter_reverse_longer("hello", "bau"),"bauollehbau");
test.assert_equals(shorter_reverse_longer("abcde", "fghi"),"fghiedcbafghi");

Given 2 strings, a and b, return a string of the form: shorter+reverse
(longer)+shorter.

In other words, the shortest string has to be put as prefix and as suffix
of the reverse of the longest.

Strings a and b may be empty, but not null (In C# strings may also be null.
Treat them as if they are empty.).
If a and b have the same length treat a as the longer producing b+reverse(a)+b
'''


def shorter_reverse_longer(a,b):
    if len(b) > len(a):
        a,b = b,a
    return b + a[::-1] + b