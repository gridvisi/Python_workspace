
'''
ADT Stack:
    Stack(self)     # 创建空栈
    is_empty(self)  # 判断栈是否为空
    push(self, elem)    # 将元素elem加入栈
    pop(self)       # 删除栈中最后加入的元素并将其返回
    top(self)           # 取得栈中最后压入的元素，不删除
'''
#定义一个异常类
class StackUnderflow(ValueError): # 栈下溢(空栈访问)
    pass

#Python 的 list 是线性表的一种实现，在此使用 list 作为栈元素存储区，整体实现如下：
class SStack:
    def __init__(self):
        self._elems = [] # 使用list存储栈元素

    def is_empty(self):
        return self._elems == []

    def push(self, elem):
        self._elems.append(elem)

    def pop(self):
        if self._elems == []:
            raise StackUnderflow("in SStack.pop()")
        return self._elems.pop()

    def top(self):
        if self._elems == []:
            raise StackUnderflow("in SStack.top()")
        return self._elems[-1]

# 简单的书写测试用例
if __name__ == '__main__':
    s = SStack()
    assert s.is_empty() is True
    try:
        s.pop()
    except StackUnderflow:
        print("StackUnderflow")
    s.push(123)
    assert s.is_empty() is not True
    assert s.pop() == 123

'''
简单应用：括号匹配问题
给定一个字符串，其中的字符只包含三种括号：花括号{ }、中括号[ ]、圆括号( )，即它仅由( ) [ ] { }这六个字符组成。
设计算法，判断该字符串是否有效，即字符串中括号是否匹配。括号匹配要求括号必须以正确的顺序配对，如{ [ ] ( ) }或[ ( { } [ ] ) ]等为正确的格式，而[ ( ] )或{ [ ( ) }或( { } ] )均为不正确的格式。

完整的括号匹配算法流程如下：

从前向后扫描字符串，遇到无关字符则跳过；
遇到左括号 x，就把 x 压栈；
遇到右括号 y:
如果发现栈顶元素x和该括号y匹配，则栈顶元素出栈，继续判断下一个字符；
如果栈顶元素x和该括号y不匹配，字符串不匹配；
如果栈为空，字符串不匹配；
扫描完成后，如果栈恰好为空，则字符串匹配，否则，字符串不匹配。
代码如下：

作者：AndZONE
链接：https://www.jianshu.com/p/d0919c5b9bb7
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

def check_parens(text):
    stack = SStack()
    left_parens = "([{"
    right_parens = ")]}"
    parens = {")":"(", "]":"[", "}":"{"}
    for i in text:
        if i in left_parens:
            stack.push(i)
        elif i in right_parens:
            if stack.is_empty():
                return False
            if parens[i] != stack.pop():
                return False
    if stack.is_empty():
        return True
    return False

if __name__ == '__main__':
    assert check_parens("[{1232}]") is True
    assert check_parens("[{[}]") is False
    assert check_parens("[{123444]}]") is False
    assert check_parens("][{}]") is False

'''
栈与函数调用经典问题之简单背包问题
递归实现如下：

'''
# 简单背包问题
def knap_rec(weight, wlist, n):
    if weight == 0:
        return True
    if weight < 0 or (weight > 0 and n < 1):
        return False
    if knap_rec(weight - wlist[n-1], wlist, n-1):
        return True
    if knap_rec(weight, wlist, n-1):
        return True
    else:
        return False

assert knap_rec(100, [90, 40, 20, 10, 50], 4) is True


# 可利用回溯法的设计思想来解决背包问题。
# 首先将 n 件物品排成一列，依次选取；若装入某件物品后，背包内物品的总质量不超过背包最大装载质量时，则装入（进栈）；
# 否则放弃这件物品的选择，选择下一件物品试探，直至装入的物品总和正好是背包的最大转载质量为止。这时我们称背包装满。
# 若装入若干物品的背包没有满，而且又无其他物品可以选入背包，说明已装入背包的物品中有不合格者，需从背包中取出最后装入的物品（退栈）
# 然后在未装入的物品中挑选，重复此过程，直至装满背包（有解），或无物品可选（无解）为止。

def knapstack(weight, wlist):
    n = len(wlist)  # 可选的物品数量
    stack = SStack()  # 创建一个栈
    k = 0  # 当前所选择的物品游标
    while stack.is_empty() is not True or k < n:  # 栈不为空或者k<n
        while weight > 0 and k < n:  # 还有剩余空间并且有物品可装
            if weight >= wlist[k]:  # 剩余空间大于等于当前物品重量
                print(wlist[k])
                stack.push(k)  # 把物品装备背包
                weight -= wlist[k]  # 背包空间减少
            k += 1  # 继续向后找
        if weight == 0:  # 找到解
            print(stack._elems)
            # return True
        # 回退过程
        k = stack.pop()  # 把最后一个物品拿出来
        print(wlist[k])
        weight += wlist[k]  # 背包总容量加上w[k]
        print(weight)
        k += 1  # 装入下一个物品