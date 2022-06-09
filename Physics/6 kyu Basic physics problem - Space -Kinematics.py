'''
https://www.codewars.com/kata/58dc420210d162048a000085/train/python

两个运动物体A和B在同一轨道上运动（可以是任何物体：两颗行星，两颗卫星，两艘飞船，两架飞碟，
或者蜘蛛人与蝙蝠侠，如果你喜欢的话）。如果两个物体从同一个点开始运动，而且轨道是圆的，
写一个函数，给出两个物体再次相遇的时间，给定物体A和B需要经过一个完整的轨道的时间，分别是Ta和Tb，
以及轨道半径r.由于不可能有负时间，Ta和Tb的符号，是物体运动方向的指示：顺时针为正，逆时针为负。

函数将返回一个字符串，给出时间，以两个小数点为单位。Ta和Tb将具有相同的测量单位，所以你不应该在解决方案中期待它。

提示：使用角速度 "w "而不是经典的 "u"。

test.describe("Basic Tests")
test.it("It should works for basic tests")
test.assert_equals(meeting_time(12, 15, 5), "60.00")
test.assert_equals(meeting_time(12, -15, 6), "6.67")

'''
import math
def meeting_time(Ta, Tb, r):
    #再次相遇的描述是较快的转过的角度恰好多较慢的一个整圆360度
    if Ta != 0 and Tb != 0:
        Va = math.pi * r / Ta
        Vb = math.pi * r / Tb
        Vgap = abs(Va - Vb)  #sorted([Va,Vb])
        if Vgap == 0:return "0.00"
        return '%.2f'% round(math.pi * r / Vgap,3)
    return '%.2f'% round(math.pi * r / max(Ta,Tb),3) if max(Ta,Tb) != 0 else "0.00"
Ta, Tb, r = 12, 15, 5   # "60.00"
Ta, Tb, r = 12, -15, 6
Ta, Tb, r = 12, 12, 6
Ta, Tb, r = -15, 12, 5
print(meeting_time(Ta, Tb, r))


#1st
def meeting_time(Ta, Tb, r):
    if Ta == 0:
        return "{:.2f}".format(abs(Tb))
    elif Tb == 0:
        return "{:.2f}".format(abs(Ta))
    else:
        return "{:.2f}".format(abs(Ta * Tb / (Tb - Ta)))

'''
import math
def meeting_time(Ta, Tb, r):
    #再次相遇的描述是较快的转过的角度恰好多较慢的一个整圆360度
    if not Ta and not Tb: 
        Va = math.pi * r / Ta
        Vb = math.pi * r / Tb
        Vgap = abs(Va - Vb)  #sorted([Va,Vb])
        if not Vgap:return float("inf")
        return round(math.pi * r / Vgap,2)
    return round(math.pi * r / max(Ta,Tb))
'''