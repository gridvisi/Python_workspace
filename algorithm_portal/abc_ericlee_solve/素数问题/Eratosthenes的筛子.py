
'''
Given a number n, print all primes smaller than or equal to n. It is also given that n is a small number.
Example:
Input : n =10
Output : 2 3 5 7
Input : n = 20
Output: 2 3 5 7 11 13 17 19
The sieve of Eratosthenes is one of the most efficient ways to find all primes smaller than n when n is smaller than 10 million or so


给定一个数n，打印出所有小于或等于n的素数。
例子：
输入：n =10
输出 : 2 3 5 7
输入 : n = 20
输出。2 3 5 7 11 13 17 19

同时给定n是小于1000万时，Eratosthenes的筛子是寻找所有小于n的素数的最有效方法之一！

以下是用埃拉托什恩的方法找到所有小于或等于给定整数n的素数的算法。
当算法结束时，列表中所有未被标记的数字都是质数。

用例子进行解释。
让我们举一个n=50的例子。所以我们需要打印所有小于或等于50的质数。
我们创建一个从2到50的所有数字的列表。
'''



# Python program to print all# primes smaller than or equal to
# n using Sieve of Eratosthenes
def SieveOfEratosthenes(n):
    # Create a boolean array
    # "prime[0..n]" and initialize
    # all entries it as true.
    # A value in prime[i] will
    # finally be false if i is
    # Not a prime, else true.
    ans = []
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
    # If prime[p] is not
    # changed, then it is a prime
        if (prime[p] == True):

            # Update all multiples of p
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1

    # Print all prime numbers
    #for p in range(2, n+1):
    #    if prime[p]:
    #        ans.append(p)
    return [i for i in range(2,n+1) if prime[i]]
# Driver codeif __name__ == '__main__':
n = 30
print("Following are the prime numbers smaller"),
print("than or equal to", n)
print('Eratosthenes:',SieveOfEratosthenes(n))


#2 math.sqrt()

def Isprime(x):
    return all([x%i!=0 for i in range(2,int(x**0.5 + 1))])

def filterPrime(n):
    ans = [x for x in range(2, n + 1) if Isprime(x)]
    #ans.append(2)
    return ans
print(filterPrime(n))


# compare time_usage

n  = 1000000
import time

start = time.time()
#print('Eratosthenes:',SieveOfEratosthenes(n))
SieveOfEratosthenes(n)
end = time.time()
time_used = end - start
print('Eratosthenes:',time_used)

#2 math.sqrt solution
start = time.time()
#print('mathSqrt:',filterPrime(n))
filterPrime(n)
end = time.time()
time_used_math = end - start
print('mathSqrt:',time_used_math)

# how fast?
print(time_used_math / time_used)
