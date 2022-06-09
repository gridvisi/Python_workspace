'''
https://www.codewars.com/kata/58ca77b9c0d640ecd2000b1e/train/python

In this exercise, you will create a function that takes an integer, i. With it you must do the following:

Find all of its multiples up to and including 100,

Then take the digit sum of each multiple (eg. 45 -> 4 + 5 = 9),

And finally, get the total sum of each new digit sum.

Note: If the digit sum of a number is more than 9 (eg. 99 -> 9 + 9 = 18) then you do NOT have to break it down further until it reaches one digit.

Example (if i is 25):

Multiples of 25 up to 100 --> [25, 50, 75, 100]

Digit sum of each multiple --> [7, 5, 12, 1]

Sum of each new digit sum --> 25

If you can, try writing it in one line of code.
str(i)[0])+eval(str(i)[1]
Edit (3/17/2017): Added random tests
'''
i = 25
print(list(map(lambda x:eval(x),list(str(i)))))

def procedure(i):
    return sum([sum(list(map(lambda x:eval(x),list(str(i))))) for i in range(i,101,i)])
i = 25
print(procedure(i))

def procedure(i):
    sl = [i for i in range(i,101,i)]
    while all([len(str(i)) > 1 for i in sl]):
        sl = [sum([eval(i) for i in list(str(n))]) for n in sl]
    return sum(sl)
i = 25
print(procedure(i))

#1st
def procedure(n):
    return sum(int(d) for i in range(n, 101, n) for d in str(i))