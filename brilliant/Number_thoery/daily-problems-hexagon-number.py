'''
Today's Challenge
The first several centered hexagonal numbers are

1, 7, 19, 37, 61 \ldots.
1,7,19,37,61….

What is the 12^\text{th}12
th centered hexagonal number?

今天的挑战

建议注册付费课程brilliant.org！舒适的交互体验，系统的课程体系，故事导入巧妙，
趣味和专业基础扎实。
由内到外看，逐渐变大的的六边形数字是

1, 7, 19, 37, 61

​中心的点为第1圈，向外直到第12圈的六边形包含多少个点？
'''

def hexagonal(n):
    total = 1
    for i in range(2,n+1):

    # 最内圈的六边形中心有一个点
    # 图中的三角型容易看出规律，分别向六个方向扩散
    # 六个向外扩展的方向的变化规律：
    # 第2圈共6个点，第2圈上每个点+1，即第3圈是6*(1+1=2)，
    # 第4圈比第3圈每个点+1，2+1 ...

        total += 6 * (i-1)
    return total
n = 12
print(hexagonal(n))

'''
Notice that the value of each consecutive pentagonal number increases by three more than the previous consecutive pair did. In other words, the difference between pentagonal numbers is 4, 7, 10, 13, etc.

In order to find the difference between the 99^\text{th}99 
th
  and 100^\text{th}100 
th
  pentagonal numbers, we use the fact that the difference will have increased by three 98 times, plus the original 4 that it increased between the first and second values:
98(3) + 4 = 298.
98(3)+4=298.
'''

def hexagonal(n):
    if n==1:return 1
    if n==2:return 6

    # 最内圈的六边形中心有一个点
    # 图中的三角型容易看出规律，分别向六个方向扩散
    # 六个向外扩展的方向的变化规律：
    # 第2圈共6个点，第2圈上每个点+1，即第3圈是6*(1+1=2)，
    # 第4圈比第3圈每个点+1，2+1 ...

    if n >= 3:return hexagonal(n-1)