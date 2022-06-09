__author__ = 'Administrator'
small = []
for i in range(1,100):
    for j in range(1,100):
        for k in range(1,100):
            if i*j*k == 10*(i + j + k):
                s = i*j + j*k + i*k
                small.append(s)

                print(i,j,k,min(small))


'''
AUTOBIOGRAPHICAL NUMBERS
An autobiographical number is a number  such that the first digit of  counts how many zeroes are in  the second
digit counts how many ones are in  and so on.
Again, our first goal will be to focus on the question: What is the autobiographical number with 10 digits?
As this problem can be difficult to answer outright, it's broken into parts. First, what is the sum of the 10 digits?
'''

import random
autobiographical = []

for i in range(10):
    digit = random.randint(1,9)
    autobiographical.append(digit)
print(autobiographical )

list()

x = 99399
print(len('234'))
print(len(str(x)))