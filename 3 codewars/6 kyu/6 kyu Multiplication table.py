'''
https://www.codewars.com/kata/534d2f5b5371ecf8d2000a08/train/python
'''

def multiplication_table(size):
    res = []
    for j in range(1,size+1):
        res.append([i*j for i in range(1,size+1)])

    return res

size = 5
print(multiplication_table(size))

def multiplicationTable(size):
    return [[j*i for j in range(1, size+1)] for i in range(1, size+1)]