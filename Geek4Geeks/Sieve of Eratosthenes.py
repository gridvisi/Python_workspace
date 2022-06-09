'''

https://www.geeksforgeeks.org/sieve-of-eratosthenes/


Given a number n, print all primes smaller than or equal to n.
It is also given that n is a small number.

Example:

Input : n =10
Output : 2 3 5 7

Input : n = 20
Output: 2 3 5 7 11 13 17 19

The sieve of Eratosthenes is one of the most efficient ways to
find all primes smaller than n when n is smaller than 10 million or
so (Ref Wiki).
'''


# Python program to print all
# primes smaller than or equal to
# n using Sieve of Eratosthenes


def SieveOfEratosthenes(n):
    # Create a boolean array
    # "prime[0..n]" and initialize
    #  all entries it as true.
    # A value in prime[i] will
    # finally be false if i is
    # Not a prime, else true.
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):

        # If prime[p] is not
        # changed, then it is a prime
        if (prime[p] == True):

            # Update all multiples of p
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    # Print all prime numbers
    for p in range(2, n + 1):
        if prime[p]:
            print(p)


# Driver code
if __name__ == '__main__':
    n = 30
    print("Following are the prime numbers smaller")
    print("than or equal to", n)
    print(SieveOfEratosthenes(n))

'''
Output
Following are the prime numbers smaller  than or equal to 30
2 3 5 7 11 13 17 19 23 29 
Time complexity : O(n*log(log(n))) 
'''