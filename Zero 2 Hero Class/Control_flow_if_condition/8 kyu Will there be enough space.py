'''
https://www.codewars.com/kata/5875b200d520904a04000003/train/python
bottle neck = 瓶颈 @gridvisi.com
test.describe('Example Tests')
test.assert_equals(enough(10, 5, 5), 0)
test.assert_equals(enough(100, 60, 50), 10)
test.assert_equals(enough(20, 5, 5), 0)
'''
print(max(10,9),min(10,9))
#define:定义
# + - // *
#1 ？ 1 = 1
x,y = 1,2
def jiafa(x,y): #jiafa is add
    return x + y
print('jiafa:',jiafa(x,y))

def add(x,y): #jiafa is add
    return x + y
print('add:',add(x,y))

cap, on, wait = 100, 60, 50
def enough(cap, on, wait):
    # judge on + wait more or less than cap?
    # 条件判断 conditional statement
    # if then else elif
    # more:> ,less : <
    # cap = Capacity

    if cap >= on + wait:
        return 0
    else:
        return on + wait - cap

#1st solution
def enough(cap, on, wait):
    return max(0, wait - (cap - on))

#修改题意，返回上车的人数,如何一行代码实现
def enough_go(cap, on, wait):
    return cap - on if cap - on <= wait else wait

def enough_go(cap, on, wait):
    return min(cap - on,wait)
cap, on, wait = 100, 40, 50
print(enough_go(cap, on, wait))