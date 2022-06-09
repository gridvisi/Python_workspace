# https://www.geeksforgeeks.org/power-set/

'''
Difficulty Level : Medium
Last Updated : 29 May, 2021
Power Set Power set P(S) of a set S is the set of all
subsets of S. For example S = {a, b, c} then P(s) = {{}, {a}, {b}, {c}, {a,b}, {a, c}, {b, c}, {a, b, c}}.
If S has n elements in it then P(s)
will have 2^n elements


Recommended: Please solve it on “PRACTICE” first,
before moving on to the solution.
Algorithm:

Input: Set[], set_size
1. Get the size of power set
    powet_set_size = pow(2, set_size)
2  Loop for counter from 0 to pow_set_size
     (a) Loop for i = 0 to set_size
          (i) If ith bit in counter is set
               Print ith element from set for this subset
     (b) Print separator for subsets i.e., newline
Example:


Set  = [a,b,c]
power_set_size = pow(2, 3) = 8
Run for binary counter = 000 to 111

Value of Counter            Subset
    000                    -> Empty set
    001                    -> a
    010                    -> b
    011                    -> ab
    100                    -> c
    101                    -> ac
    110                    -> bc
    111                    -> abc
Method 1:
'''

# python3 program for power set

import math
def printPowerSet(set, set_size):
    # set_size of power set of a set
    # with set_size n is (2**n -1)
    pow_set_size = (int)(math.pow(2, set_size))
    counter = 0
    j = 0

    # Run from counter 000..0 to 111..1
    for counter in range(0, pow_set_size):
        for j in range(0, set_size):

            # Check if jth bit in the
            # counter is set If set then
            # print jth element from set
            if ((counter & (1 << j)) > 0):
                print(set[j], end="")
        print("")


# Driver program to test printPowerSet
set = ['a', 'b', 'c']
printPowerSet(set, 3)

# This code is contributed by mits.

'''
Time Complexity: O(n2^n)
Method 2: 
This method is specific to the python programming language. 
We can iterate a loop over 0 to the length of the set to obtain 
and generate all possible combinations of that string with the iterable length. 

The program below will give the implementation of the above idea. 

时间复杂度。O(n2^n)
方法二。
这种方法是python编程语言所特有的。我们可以在0到集合的长度上进行循环迭代，获得并生成该字符串与可迭
代长度的所有可能组合。下面的程序将给出上述想法的实现。
'''
#Python program to find powerset
from itertools import combinations
def print_powerset(string):
    for i in range(0,len(string)+1):
        for element in combinations(string,i):
            print(''.join(element))
string=['a','b','c']
print_powerset(string)