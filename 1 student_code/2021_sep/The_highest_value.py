
#找出一个数组中最大的一个数
#例如：arr = [17,10,9,4,8,5,10,15]
#输出：17，15
#说明：因为17和15是排最大的前两个数

#方法一：用for循环，打擂台的方式找到最大的
#先看第一个数是17，再看第二个数10，和17比较，
# 如果比17大就将最大的数改为第二个数，如果不是就保持17

'''
以下是一个如何在一串数值中找到最小的数值的代码。 一行代码有错误，导致整个代码无法和预期一样的运行。
那么是哪一行？
smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
        break
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)
'''

def highestValue(arr):
    biggest = float('+inf')  #biggest = float('-inf') 试试看结果有无变化？
    for n in arr:
        if n < biggest:
            biggest = n
    return biggest
arr = [-30,-100,-6,-100000000000000,] #17,10,9,4,8,5,10,15,20,

print(highestValue(arr))


#2 find error

smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 74, -15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
        break
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)