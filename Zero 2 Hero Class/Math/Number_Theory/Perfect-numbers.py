'''
“Perfect numbers” are equal to the sum of their “proper” divisors.
For example, 6 = 3 + 2 + 1, and 28 = 14 + 7 + 4 + 2 + 1.
More than 2,000 years after Euclid presented the basics about
these numbers, mathematicians still find them mysterious.

"完全数 "等于它们的 "正数 "除数之和。例如，6=3+2+1，28=14+7+4+2+1。
在欧几里德提出关于这些数字的基础知识2000多年后，数学家仍然觉得它们很神秘。
'''
import math
def Isperfect_num(x):
    factor = []
    for i in range(1,int(x**0.5)+1):
        if x%i == 0:
            factor.append(i)
            factor.append(x//i)
    if sum(factor) - x == x:
        return f"{x} is perfect number",factor
    return False
x = 28
print([x for x in range(1,10000) if Isperfect_num(x)])