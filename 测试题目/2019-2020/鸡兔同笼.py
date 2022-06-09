__author__ = 'Administrator'

# 鸡和兔共有15只，假如40只脚都是兔子的脚，兔子有20只；
# 如都是鸡的脚，鸡有10只。兔的数量不会超过20，兔子为x个

for x in range(1,21):
    y = 15 - x
    if 4*x + 2*y == 40:
        print('兔子有%s只，鸡有%s只'%(x, y))