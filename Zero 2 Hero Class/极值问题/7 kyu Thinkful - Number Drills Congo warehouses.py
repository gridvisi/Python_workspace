'''
https://www.codewars.com/kata/5862e7c63f8628a126000e18/train/python
你的公司，刚果披萨，是第二大的在线冷冻披萨零售商。你拥有许多国际仓库，用来存储你
的冷冻披萨，你需要计算出每个地点可以存储多少箱披萨。

存储容器进行了标准化：所有的披萨都适合放在一个立方体的板条箱内，边长16英寸。板条
箱超级坚硬，所以你可以把它们堆得越高越好。

写一个函数box_capacity()，计算出在给定的仓库中可以存放多少个周转箱。这个函数
应该接受三个参数：你的仓库的长、宽、高（以英尺为单位），并且应该返回一个整数，代
表你在这个空间里可以存储的箱子数量。

例如：一个长32英尺、宽64英尺、高16英尺的仓库可以存放13824个箱子，因为你可以横
放24个箱子，深48个箱子，高12个箱子，所以box_capacity(32, 64, 16)应该返回
13824。

test.assert_equals(box_capacity(32, 64, 16), 13824)
test.assert_equals(box_capacity(20, 20, 20), 3375)
test.assert_equals(box_capacity(80, 40, 20), 27000)

inch 是英寸的意思，也被简称为 in. 使用。通常用符号 ‘ (单引号)表示。
foot (feet)，也被简称为 ft 使用，是英尺的意思。通常用符号 ” (双引号)表示。
1ft=12in
1in=2.54cm

英尺——在英语国家中，古代和现代各种以人脚长度为依据的长度计量单位。一般为
25—34厘米。在许多其他西方语言中，脚和计量用的尺都用同一个词表示，虽然它
所代表的长度各个地方、各个时期有所不同。例如德语言中的fuss，挪威和丹麦语
中的fod等。
'''
# box_side = 16 inch =
# foot = 12 inch
def box_capacity(length, width, height):
    maxn = [n*12//16 for n in (length, width, height)]
    return maxn[0]*maxn[1]*maxn[2]
length, width, height = 80, 40, 20
print(box_capacity(length, width, height))


#其他写法
from functools import reduce

def box_capacity(length, width, height):
    FEET_TO_INCH = 12
    CRATE_SIZE = 16
    crates = (
        int(FEET_TO_INCH * dimension / CRATE_SIZE) \
        for dimension in (length, width, height)
    )
    return reduce(lambda x, y: x * y, crates)

from functools import reduce
BOX_DIM = 16
def box_capacity(*dims):
    return reduce(int.__mul__, (d*12//BOX_DIM for d in dims))

def box_capacity(x, y, z):
  return int(x*0.75)*int(y*0.75)*int(z*0.75)
