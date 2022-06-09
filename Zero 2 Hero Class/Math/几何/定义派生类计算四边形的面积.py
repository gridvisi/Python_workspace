
'''模块说明  定义类计算三角形有关的方法
定义派生类计算四边形的算法'''
from matplotlib import pyplot as plt
import math
import numpy
import random
class Triangle(object):
    '''判断三角形的类型以及面积方法'''
    #定义三角形三边啊a,b,c,;
    def __init__(self,a,b,c):
        self.a=a; self.b=b; self.c=c
    #判断是否构成三角形的方法；
    def JDTriangle(self):
        if self.a+self.b>self.c and self.b+self.c>self.a and \
            self.c+self.a>self.b:
            return "能构成三角形"
        else:
            return "不能构成三角形"
    #判断三角形类型锐、钝、直、等腰三角形
    def TPTriangle(self):
        '''判断三角形类型锐、钝、直、等腰三角形'''
        if self.a**2+self.b**2==self.c**2 or self.b**2+self.c**2==self.a**2 or \
                self.c ** 2 + self.a ** 2 == self.b ** 2:
            return "直角三角形"
        elif self.a**2+self.b**2>self.c**2 and self.b**2+self.c**2>self.a**2 and \
                self.c ** 2 + self.a ** 2 > self.b ** 2:
            return "钝角三角形"
        elif self.a**2+self.b**2<self.c**2 and self.b**2+self.c**2<self.a**2 and \
                self.c ** 2 + self.a ** 2 < self.b ** 2:
            return "锐角三角形"
        elif self.a==self.b==self.c:
            return "等边三角形"
        elif self.a==self.b or self.b==self.c or self.c==self.a:
            return "等腰三角形"
    #求三角形面积
    def area_1(self):
        '''已知三边求三角形面积'''
        p=(self.a+self.b+self.c)/2
        S=numpy.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))
        # print("三角形面积为{:0.2f}".format(S))
        return S  #直接返回S 避免计算四边形是发生错误
    def area_2(a,b,α):
        '''已知三角形两边及夹角  需传入三个参数'''
        S=(a*b*math.sin(α*math.pi/180))/2
        # print( "三角形面积为{:0.2f}".format(S))
        return S
    def area_3(A,B,a):
        '''已知两角及其一角的对边   先输入有对边的角'''
        S=(a**2*numpy.sin((A+B)*numpy.pi/180)*numpy.sin(B*numpy.pi/180))/(2*numpy.sin(A*numpy.pi/180))
        return "三角形面积为{:0.2f}".format(S)

class Quadrilateral(Triangle):
    '''计算四边形面积方法'''
    def __init__(self,a,b,c,d):
        Triangle.__init__(self,a,b,c)  #调用基类构造函数
        self.d=d
    def areas_1(self):
        '''已知四边，调用三角形方法area_1求解'''
        if self.a*self.b*self.c *self.d>0 and self.a+self.b+self.c>self.d and \
                self.a+self.b+self.d>self.c and self.a+self.c+self.d>self.b and self.b+self.c+self.d>self.a:  # 判断是否构成四边形
            x_1=[self.a-self.b,self.a-self.c,self.a-self.d,self.b-self.c,self.b-self.d,self.c-self.d]  # 控制对角线范围     最大边之差 <x<最小边之和
            x_1=max(map(abs, x_1))
            x_2=[self.a+self.b,self.c+self.d,self.b+self.c,self.b+self.d,self.a+self.d,self.a+self.c]
            x_2=min(x_2)
            area=[]
            for i in range(0, 100000):  # 随机取对角线
                x=random.uniform(x_1, x_2)
                S1=Triangle(self.a,self.b,x)  #创建对象
                S2=Triangle(self.c,self.d,x)
                s=S1.area_1()+S2.area_1()
                area.append(s)
            maxS=max(area)
            minS=min(area)
        else:
            print("不能构成四边形")
        print("最大面积为{:0.4f}".format(maxS))
        print("最小面积为{:0.4f}".format(minS))
    def areas_2(self):
        if 2*max(self.a,self.b,self.c,self.d)<(self.a+self.b+self.c+self.d):  # 判断是否构成四边形
            x_1=[self.a-self.b,self.a-self.c,self.a-self.d,self.b-self.c,self.b-self.d,
                   self.c - self.d]  # 控制对角线范围     最大边之差 <x<最小边之和
            x_1 =max(map(abs, x_1))
            x_2 = [self.a+self.b,self.c+self.d,self.b+self.c,self.b+self.d,self.a+self.d,self.a+self.c]
            x_2 = min(x_2)
            n=int(input("请输入需要分割成多少个"))
            x = numpy.linspace(x_1, x_2, n)  # 构建对角线最大最小值之间的等差数列
            L = []
            for i in range(n):  # 进行搜索法
                p_1 = (self.a+self.b + x[i]) / 2
                p_2 = (self.c+self.d + x[i]) / 2
                y1 = math.sqrt(p_1 * (p_1 -self.a) * (p_1 - self.b) * (p_1 - x[i]))
                y2 = math.sqrt(p_2 * (p_2 - self.c) * (p_2 - self.d) * (p_2 - x[i]))
                y = y1 + y2  # 四边形面积
                L.append(y)  # 将所有四边形面积存储在列表list之中
        else:
            print("不能构成四边形")
        print("四边形的最大值为：{:0.4f}".format(max(L)))
        print("四边形的最小值为：{:0.4f}".format(min(L)))

    def areas_3(self):
        if 2 * max(self.a, self.b, self.c, self.d) < (self.a + self.b + self.c + self.d):  # 判断是否构成四边形
            n=numpy.linspace(0,math.pi,10000)
            S=[]
            for i in range(10000):
                α=n[i]
                x=math.sqrt((self.a**2+self.b**2)-2*self.a*self.b*math.cos(α))
                if self.c+self.d>x:
                    β=math.acos((self.c**2+self.d**2-x**2)/(2*self.c*self.d))
                    S1=Triangle.area_2(self.a,self.b,(α*180/math.pi))
                    S2=Triangle.area_2(self.c,self.d,(β*180/math.pi))
                    s=S1+S2
                    S.append(s)
                else:
                    continue

        else:
            print("不能构成四边形")
        print("四边形的最大值为：{:0.4f}".format(max(S)))
        print("四边形的最小值为：{:0.4f}".format(min(S)))
        # 支持中文标签
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
        plt.plot(n, S)
        plt.xlabel("对角线的取值")
        plt.ylabel("四边形面积变化")
        plt.title("原始数据分布")
        plt.show()

if __name__ == '__main__':
     P=Triangle(41,4,5)  #创建对象
     print(P.JDTriangle())
     print(Triangle.area_2(3,4,30))
     print(Triangle.area_3(45,45,1))
     p1=Quadrilateral(2,3,4,5)
     p1.areas_1()
     p1.areas_3()


#原文链接：https://blog.csdn.net/weixin_44659084/article/details/103141993