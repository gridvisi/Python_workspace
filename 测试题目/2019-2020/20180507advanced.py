__author__ = 'Administrator'
'''
Math.sin(x)      x 的正玄值。返回值在 -1.0 到 1.0 之间；
Math.cos(x)    x 的余弦值。返回的是 -1.0 到 1.0 之间的数；
这两个函数中的X 都是指的“弧度”而非“角度”，弧度的计算公式为： 2*PI/360*角度；
30° 角度 的弧度 = 2*PI/360*30


如何得到圆上每个点的坐标？解决思路：根据三角形的正玄、余弦来得值；
假设一个圆的圆心坐标是(a,b)，半径为r，
则圆上每个点的X坐标=a + Math.sin(2*Math.PI / 360) * r ；Y坐标=b + Math.cos(2*Math.PI / 360) * r ；
如何求时钟的秒针转动一圈的轨迹？
假设秒针的初始值（起点）为12点钟方向，圆心的坐标为（a,b)。
解决思路：一分钟为60秒，一个圆为360°，所以平均每秒的转动角度为 360°/60 = 6°；

for(var times=0; times<60; times++) {
      var hudu = (2*Math.PI / 360) * 6 * times;
       var X = a + Math.sin(hudu) * r;
       var Y = b - Math.cos(hudu) * r    //  注意此处是“-”号，因为我们要得到的Y是相对于（0,0）而言的。


三个相同的硬币的中心形成了上面绿色的角度。
什么角度最大化蓝色凸包的面积？
注意：你可以想象凸包的周长是围绕着三个硬币的橡皮筋。

参考：http://blog.csdn.net/nov_csdn/article/details/52959346
aa = [1,2,3,4,5]
aa.index(max(aa))
如果aa是numpy数组：
aa = numpy.array([1,2,3,4,5])
先把aa转换为List，再求索引：
bb = aa.tolist()
bb.index(max(bb))
circle = math.pi*(i*1/360*math.pi)
    rectangle = 2*math.cos(i*1/360*math.pi)
    total = triangle + rectangle - circle

'''
# x =? 3sinax/2 + cosx/2 + = max?
import math

y = []
for i in range(61):
    triangle = 2*math.sin(i*1/360*math.pi) * math.cos(i*1/360*math.pi)

    y.append(triangle)
ymax = y.index(max(y))
print(ymax,max(y),y)
print((math.pi)*2/6)
print(math.sin(math.pi*1/6))
print(math.sin(math.radians(60)))