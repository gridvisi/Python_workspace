def is_prime(num):
    cam = 0
    if num == 2:
        return True
    elif num > 2:
        for i in range(2,num):
            if num % i == 0:
                return False
        return True
    else:
        return False

print(is_prime(9))