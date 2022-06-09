
china = (1400050000,960,'Peking')
warssaw = (1700000,517,'Poland')
seoul = (9776000,605.2,'South Korea')

from collections import namedtuple
City = namedtuple('City','population area country')
#实例
warsaw = City(1700000 ,517,'Poland')
print(warsaw.area,warsaw.country,warsaw.population)

seouls = City(9776000,605.2,'South Korea')
print(seouls.area,seouls.country,seouls.population)

chinese = City(1400050000,960,'Peking')
print(chinese.area,chinese.country,chinese.population)

# 坐标
coordinate = namedtuple('Coordinate', ['x', 'y'])
co = coordinate(10,20)
print (co.x,co.y)
print (co[0],co[1])
co = coordinate._make([100,200])
print (co.x,co.y)
co = co._replace(x = 30)
print (co.x,co.y)

