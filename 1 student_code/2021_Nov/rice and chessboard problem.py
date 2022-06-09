'''
https://www.codewars.com/kata/5b0d67c1cb35dfa10b0022c7/train/python

squares_needed(0) == 0
squares_needed(1) == 1
squares_needed(2) == 2
squares_needed(3) == 2
squares_needed(4) == 3

我想你们中的大多数人都熟悉关于大米（但我看到维基百科出于某种原因建议用小麦）问题的古老传说，
但我要为你们做一个简单的回顾：一个年轻人要求作为补偿，第一个方格只用1粒米，第二个方格用2粒米，
第三个方格用4粒米，第四个方格用8粒米，以此类推，总是比以前多一倍。

你的任务很简单（但不一定很容易）：给你一定数量的谷物，你需要返回到棋盘的哪个方格，以便至少得
到同样的数量。

像往常一样，举几个例子可能比我说的几千字要好得多。

squares_needed(0) == 0
squares_needed(1) == 1
squares_needed(2) == 2
squares_needed(3) == 2
squares_needed(4) == 3
输入总是有效的/合理的：即：非负数；不使用循环计算逐个平方（至少不直接计算）
而尝试更聪明的方法的额外cookie[提示：一些奇特的运算符]；转换数字的技巧也可能有效：
给我留下深刻印象

通过www.DeepL.com/Translator（免费版）翻译
'''
import math
def squares_needed(grains):
    # s   =    2**1 + 2**2 + 2**3 ... ... 2**n
    # s/2 = 1+ 2**1 + 2**2 + 2**3 ...2**(n-1)
    # s - s/2 = 2**n - 1 == s/2
    # 2*(grains - grains/2) = grains = 2**(n+1) - 2
    # grains + 2 = 2**(n+1)
    return math.ceil(math.log(grains+2,2))

#1st
squares_needed = int.bit_length

def squares_needed(grains):
    if grains < 1:
        return 0
    else:
        return 1 + squares_needed(grains // 2)

#2nd
def squares_needed(grains):
    return grains.bit_length()

#3rd
def squares_needed(grains):
    if grains < 1:
        return 0
    else:
        return 1 + squares_needed(grains // 2)

#4th
from math import log2, ceil
def squares_needed(grains):
    return grains and ceil(log2(grains+1))

#5th
def squares_needed( _ ):
    return len(bin(_)[2:]) if _ else 0

#6th
def squares_needed(grains):
    return next(i for i in range(99) if 1<<i > grains)

#7th
from math import log2
def squares_needed(grains):
    return int(log2(grains))+1 if grains else 0

def squares_needed(grains):
    return 0 if grains==0 else len(bin(grains)[2::])

#8th
def squares_needed(grains):
    if not grains: return grains
    squares = 1
    while 2**squares <= grains:
        squares += 1
    return squares


# 第四种 递推写法
def squares_needed(grains):
    square,n = 0,0
    while square < grains:
        square += 2**n
        n += 1
    return n


'''
前n格子的米粒总和 S = 2**n - 1 = 2 * 2**(n-1) - 1
S // 2 = (2 * 2**(n-1) - 1) // 2  = 

假设, 第grains颗米粒落在第n-1格子，
gains的数量落在前n-2格子米粒总和2**(n-1) - 1，与前n-1个格子总和2**n - 1之间
初始 0 态：2**(n-1) - 1 <=   grains  <= 2 * 2**(n-1) - 1
                   2**(n-1)      <=  grains+1      <= 2 * 2**(n-1) 

recur 1st： 2**(n-2)      <=   grains+1      <= 2 * 2**(n-2) 
recur 2nd：2**(n-3)      <=  (grains+1)/2   = 2**(n-3)
'''