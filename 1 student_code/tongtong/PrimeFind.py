import math


def prime(f):
    for d in range(2, f):
        if f % d == 0:
            return False

        if d == f - 1:
            return True
output = filter(prime, range(2, 1001))
print(list(output))


#sliver  #枚举
def primeSliver(f):
    for d in range(2, int(math.sqrt(f))+1):
        if f % d == 0:
            return False
    return True


#