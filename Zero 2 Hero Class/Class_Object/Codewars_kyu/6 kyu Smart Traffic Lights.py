# https://www.codewars.com/kata/58587905ed1b4dad6e0000c6/train/python
'''
故事
你的朋友鲍勃是一名出租车司机。在工作了一个月后，他在城市的交通灯中感到很
沮丧。他请你为一种新型的交通灯写一个程序。它的制作方式是让最拥堵的路段变
成绿色。

任务
给定2对数值，每对数值代表一条道路（道路上的车辆数量和道路名称），构造一个
对象，其turngreen方法返回方法调用时刻车流量最大的道路名称，并清除该道路
上的车辆。

当两条道路上的车辆都被清除后，或者如果两条道路上的车辆数量从一开始就相同，
则返回一个空值。

例子

'''
class SmartTrafficLight:
    def __init__(self, st1, st2):
        self.st =[]
        self.st.append(st1)
        self.st.append(st2)

    def turngreen(self):
        road1 =self.st[0][0]
        road2 =self.st[1][0]
        if road1 > road2:
            self.st[0][0 ] =0
            return self.st[0][1]
        elif road2 > road1:
            self.st[1][0 ] =0
            return self.st[1][1]
        else:
            return None


class SmartTrafficLight:
    def __init__(self, a, b):
        self.a = [] if a[0] == b[0] else sorted((a, b))

    def turngreen(self):
        if self.a:
            return self.a.pop()[1]