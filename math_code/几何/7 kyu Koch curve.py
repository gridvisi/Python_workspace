'''
https://www.codewars.com/kata/5c5abf56052d1c0001b22ce5/train/python

科赫曲线是一种简单的几何分形。
这个分形的构造如下：将一条线段分成三个相等的部分。在中间部分的基础上，插入两个相同的段，彼此成60度角。
这个过程在每次迭代时都会重复：每一段都会被四段取代。你必须写一个程序，当从起点到终点画一条线时，
取数字n并返回一个旋转角度的数组。旋转角度是逆时针方向的正值。
test.describe("Koch curve")

test.it("Should handle basic cases")
test.assert_equals(koch_curve(0), [])
test.assert_equals(koch_curve(1), [60, -120, 60])
'''

def koch_curve(n):
    if n == 0:return []
    elif n == 1:return [60, -120, 60]
    return 4 * koch_curve(n-1)
n = 3
print(koch_curve(n))

ans = koch_curve(n)
print(ans.count(-120))

#1st solution
def koch_curve(n):
    if not n: return []
    deep = koch_curve(n-1)
    return [*deep, 60, *deep, -120, *deep, 60, *deep]
n = 3
print(koch_curve(n))

def koch_curve(n):
    l = []
    for i in range(1, n + 1):
        l = l + [60] + l + [-120] + l + [60] + l
    return l