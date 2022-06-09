def sum_factorial(ls):
    summ = 0
    temp = 1
    for i in range(0,len(ls)):
        for j in range(ls[i],0,-1):
            temp *= j
        summ += temp
        temp = 1
    return summ
print(sum_factorial([4,6]))