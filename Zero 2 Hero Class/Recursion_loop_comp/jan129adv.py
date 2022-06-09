__author__ = 'Administrator'
'''
Starting with a number, the following is called the Collatz rule:

If the number is odd, multiply by 3 and add 1.
If the number is even, divide by 2.
The Collatz conjecture suggests that when you keep doing this, you will always reach 1 eventually.

For example, if you start with 7, you reach 1 in 16 steps:
However, 7 is not the only number that requires 16 steps. What is the total number of positive integers which require
exactly 16 steps to reach 1 for the first time?

Note: This problem is intended to have a coding solution.

7 -> 22  ->  11  -> 34  -> 17  ->   52   -> 26  ->  13  ->   40  ->  20  ->  10  ->   5    ->  16  ->    8  ->   4   ->  2   -> 1
'''


def collatzDistance(r, n=1):
    if r == 0:
        return 1
    else:
        if n > 4 and n % 6 == 4:
            return collatzDistance(r-1,2*n) + collatzDistance(r-1,(n-1)//3)
        else:
            return collatzDistance(r-1,2*n)

print(collatzDistance(10))

# 非递归，循环实现效率，时间有优势

collatzNumbers = [[1]]

def backCollatz():
      l = []
      for n in collatzNumbers[-1]:
        l.append(n*2)
        g = ((n-1)/3.0)
        if g % 2 == 1 and not g == 1:
          l.append(int(g))
      collatzNumbers.append(l)
      print(collatzNumbers)
      # print a

for i in range(3):
    backCollatz()

print (len(collatzNumbers[-1]))