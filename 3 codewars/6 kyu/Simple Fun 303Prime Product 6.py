def prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def prime_product(n):
    if n == 0 or n == 1 or n == 2 or n == 3:
        return 0
    else:
        over = n - 1
        start = 1
        for i in range(n,0,-1):
            if prime(over) and prime(start):
                return start * over
            elif not prime(over):
                over -= 1
            elif not prime(start):
                start += 1
            else:
                over -= 1
                start += 1
print(prime_product(4))
