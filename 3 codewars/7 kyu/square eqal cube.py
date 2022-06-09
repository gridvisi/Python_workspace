__author__ = 'Administrator'
'''
import math
for i in range (100):
    temp = math.sqrt((i**3) + ((i+1)**3) + ((i+2)**3))
    #print(temp)

    if temp - int(temp) == 0:
        print('result:',int(temp))
'''
# n**5-1 is prime
import math
def is_prime_v2(n):
    if n == 0 or n == 1:
        return False

    max_divisor = math.floor(math.sqrt(n))
    for d in range(2,1+max_divisor):
        if n % d == 0:
            return False
    return True
print(is_prime_v2(27))

for j in range(1,1000):
    #print(i,i**5-1)
    if is_prime_v2( j ** 5 - 1) == True:
        print(j,j ** 5 - 1)
'''
import math
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
        return True
print(isPrime(27))


'''