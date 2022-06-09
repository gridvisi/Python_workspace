
'''
https://www.codewars.com/kata/5262119038c0985a5b00029f/train/python
'''
import math
def is_prime(num):
    if num == 1 or num < 1:return False
    elif num >= 2:
        for i in range(2,int(math.sqrt(num))+1):
            if num % i == 0:
                return False
    return True

check = [i for i in range(100)]
print([(num,is_prime(num)) for num in check])


import gmpy2

def is_prime(num):
  return gmpy2.is_prime(num) if num > 0 else False


'''
Time: 2548ms Passed: 519 Failed: 0
Test Results:
 Basic
 Basic tests (6 of 6 Assertions)
 Test prime (5 of 5 Assertions)
 Test not prime (8 of 8 Assertions)
Completed in 0.17ms
 Random tests
 Random tests (500 of 500 Assertions)
Completed in 1911.41ms
You have passed all of the tests! :)
'''