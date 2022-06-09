'''
https://www.codewars.com/kata/5ff50f64c0afc50008861bf0/train/python

Simple kata, simple rules: your function should accept the inputs 4 and 7. If 4 is entered,
the function should return 7. If 7 is entered, the function should return 4.
Anything else entered as input should return a false-y value such as False, 0, [], "".

There's only one catch, your function cannot include if statements (or the eval function
due to the fact that you can get around the if requirement using it).

There are some very simple ways of answering this problem, but I encourage you to try
and be as creative as possible.

Good Luck!

est Results:
No Cheating
Should prevent 'if' and 'eval' from being used anywhere in the code
Your code isn't allowed to use 'if'!
Test Passed
Completed in 0.08ms
Completed in 0.10ms
Tests for 4 and 7
n = 4 should return 7
n = 7 should return 4
Completed in 0.03ms
False-y Tests
Random ints
n = 64 should be False-y
'''
solution = lambda n: {4: 7, 7: 4}.get(n, False)
def solution(n):

    try:
        return {4: 7, 7: 4}[n]
    except KeyError:
        return False


n = 4
print(solution(n))

def solution(n):
    return 4 if n == 7 else 7


#1st
solution = {4:7, 7:4}.get

#2nd
def solution(n):
    return n == 4 and 7 or n == 7 and 4



def solution(n):
    return n in [4, 7] and [4, 7][n == 4]