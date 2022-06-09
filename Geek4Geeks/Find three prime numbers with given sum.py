'''
https://www.geeksforgeeks.org/find-three-prime-numbers-with-given-sum/

Given an integer N, the task is to find three prime numbers
X, Y, and Z such that the sum of these three numbers is equal
to N i.e. X + Y + Z = N.

Examples:

Input: N = 20
Output: 2 5 13

Input: N = 34
Output: 2 3 29

使用埃拉托塞尼斯筛子生成素数
从第一个质数开始。
从生成的列表中抽取另一个数字。
用第一个数字和第二个数字减去原始数字，得到第三个数字。
检查第三个数字是否是一个质数。
如果第三个数字是一个质数，则输出这三个数字。
否则，重复第二个数字的过程，进而重复第一个数字的过程
如果答案不存在，则打印-1。
'''

# Python3 implementation of the approach
from math import sqrt

MAX = 100001

# The vector primes holds
# the prime numbers
primes = []


# Function to generate prime numbers
def initialize():
    # Initialize the array elements to 0s
    numbers = [0] * (MAX + 1)
    n = MAX
    for i in range(2, int(sqrt(n)) + 1):
        if (not numbers[i]):
            for j in range(i * i, n + 1, i):
                # Set the non-primes to true
                numbers[j] = True

    # Fill the vector primes with prime
    # numbers which are marked as false
    # in the numbers array
    for i in range(2, n + 1):
        if (numbers[i] == False):
            primes.append(i)


# Function to print three prime numbers
# which sum up to the number N
def findNums(num):
    ans = False
    first = -1
    second = -1
    third = -1
    for i in range(num):

        # Take the first prime number
        first = primes[i]
        for j in range(num):

            # Take the second prime number
            second = primes[j]

            # Subtract the two prime numbers
            # from the N to obtain the third number
            third = num - first - second

            # If the third number is prime
            if (third in primes):
                ans = True
                break

        if (ans):
            break

    # Print the three prime numbers
    # if the solution exists
    if (ans):
        print(first, second, third)
    else:
        print(-1)


# Driver code
if __name__ == "__main__":
    n = 101

    # Function for generating prime numbers
    # using Sieve of Eratosthenes
    initialize()

    # Function to print the three prime
    # numbers whose sum is equal to N
    findNums(n)

# This code is contributed by AnkitRai01