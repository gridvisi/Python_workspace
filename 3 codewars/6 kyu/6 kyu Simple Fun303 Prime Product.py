'''
https://www.codewars.com/kata/simple-fun-number-303-prime-product/train/python
Example
For n = 1, the output should be 0.
1 can not split into two primes
For n = 4, the output should be 4.
4 can split into two primes 2 and 2. 2 x 2 = 4
For n = 20, the output should be 91.
20 can split into two primes 7 and 13 or 3 and 17. The maximum product is 7 x 13 = 91
Test.assert_equals(prime_product(1),0)
Test.assert_equals(prime_product(3),0)
Test.assert_equals(prime_product(4),4)
Test.assert_equals(prime_product(5),6)
Test.assert_equals(prime_product(6),9)
Test.assert_equals(prime_product(7),10)
Test.assert_equals(prime_product(8),15)
Test.assert_equals(prime_product(9),14)
Test.assert_equals(prime_product(10),25)
Test.assert_equals(prime_product(11),0)
Test.assert_equals(prime_product(12),35)
Test.assert_equals(prime_product(20),91)
Test.assert_equals(prime_product(100),2491)
'''
import math
def is_Prime(x):
    mp = math.sqrt(x)  # match point
    if x == 0 or x == 1:
        return False
    else:
        for i in range(2,int(mp)+1): # why mp + 1?
            if x % i == 0:
                return False
        return True
print(is_Prime(9))

# better solution with n//2
def prime_product(n):
    larger,i,mx = 0,0,[]
    for i in range(n//2,n):
        if is_Prime(i) == False or is_Prime(n-i) == False:
            pass
        else:
            re = i * (n-i)
            #print(re)
            if re > larger:
                larger = re
                #return re
            print(larger)
            #print(mx,larger, i, n - i)
            print(larger, i, n - i)
    print(larger, i, n - i)  # be careful,what happen with i?
    return larger

# the best solution

def prime_product(n):
    larger,i,mx = 0,0,[]
    for i in range(n//2,n):
        if is_Prime(i) == True and is_Prime(n-i) == True:
            print(i,n-i)
            return i * (n-i)
    return 0
print(prime_product(7))

def isPrime(n):
    return n==2 or n>2 and n&1 and all(n%p for p in range(3,int(n**.5+1),2))

def prime_product(n):
    return next( (x*(n-x) for x in range(n>>1,1,-1) if isPrime(x) and isPrime(n-x)), 0)


'''
# pave the way to success!!!

def prime_product(n):
    larger,i,mx = 0,0,[]
    for i in range(n):
        if is_Prime(i) == True and is_Prime(n-i) == True:
            re = i * (n-i)
            #print(re)
            if re > larger:
                larger = re
                #return re
        mx.append(larger)
            #print(mx,larger, i, n - i)
        print(mx, larger, i, n - i)
        #print(mx[1], larger, i, n - i)
        #return max(mx)
    return 0
print(prime_product(20))
'''
