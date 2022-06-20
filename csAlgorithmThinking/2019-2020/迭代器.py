'''
https://www.jianshu.com/p/104cec085611
'''
from collections import namedtuple
Student = namedtuple('Student', ['name','age','sex','email'])  # 定义类
s = Student('jim',16, 'male', 'aa@aa.com')  # 赋值就跟创建一个对象类似
s.name  # 获取元素
isinstance(s, tuple)

class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    def getWeather(self, city):
        r = requests.get(u'http://wthrcdn.etouch.cn/weather_mini?city=' + city)
        data = r.json()['data']['forecast'][0]
        return '%s: %s, %s' % (city, data['low'], data['high'])

    def next(self):
        if self.index == len(self.cities):
            raise StopIteration

        city = self.cities[self.index]
        self.index += 1
        return self.getWeather(city)


class WeatherIterable(Iterable):
    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)
