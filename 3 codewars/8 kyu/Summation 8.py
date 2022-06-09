def summation(num):
    for i in range(num-1,0,-1):
        num += i
    return num
print(summation(8))