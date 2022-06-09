'''
https://brilliant.org/problems/stacked-carts/

ADT Stack:
    Stack(self)     # 创建空栈
    is_empty(self)  # 判断栈是否为空
    push(self, elem)    # 将元素elem加入栈
    pop(self)       # 删除栈中最后加入的元素并将其返回
    top(self)           # 取得栈中最后压入的元素，不删除
'''

x = 3
print(bin(x),type(bin(x)))
print('0b'+x*2*'1')
print(int(x*2*'1'))

import queue


def oppu(x):
    re = []
    for i in range(int(x*2*'1',2)):
        if str(bin(i)).count('1') == x:
            s = (2*x - len(str(bin(i))[2:]))*'0'+ str(bin(i))[2:]
            re.append(s)
    return re
print(oppu(x))

# '0'-> push,'1'-> pop
i,re = 0,[]
ops = oppu(x)
while i < len(ops):
    #print(ops[i])
    left = [1, 2, 3]
    right = queue.deque()
    spur = []
    for op in ops[i]:

        if op == '0' and len(left) == 0:
            i += 1
        elif op == '0' and len(left) != 0:
            spur.append(left.pop())
            i += 1

        elif op == '1' and len(spur) == 0:
            i += 1
        elif op == '1' and len(spur) != 0:
            right.appendleft(spur.pop())
            re.append(right)
            #print(right,re)
            i += 1
print(left,right,spur,re)

def recur(x):
    if x == 1:return 1
    if x == 2:return 2
    if x >= 3:return 2 * recur(x-1) + 1

print(recur(3))
print(recur(16))


left = 16
result = 0

def count(spur, right,result=0):
    n = 3

    print(left)
    if right == n:  #all trains are on the right track
        return result
    elif right + spur < n: #there is at least one train available on the left track
        result += 1
        count(spur+1, right,result) #push a cart
    elif spur > 0: #if the spur is non-empty
        result += 1
        count(spur-1, right+1,result) #pop a cart

print(count(0,0,0))
print(result)
'''
# stack()
def revStrings(myStr):
    stack = Stack()
    for ch in myStr:
        stack.push(ch)
    revStr = ''
    while not stack.isEmpty():
        revStr += stack.pop()
    return revStr

print(revStrings("apple"))
'''