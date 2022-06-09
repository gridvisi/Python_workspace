def power_of_two(x):
    temp = 2
    i = 0
    while True:
        if temp**i == x:
            return True
        i += 1
    return False
print(power_of_two(10000000))