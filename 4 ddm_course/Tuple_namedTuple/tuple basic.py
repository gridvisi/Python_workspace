# 出生年月，身份证

lyc = [13,160]
lyc[0],lyc[1] = 14,172
print(lyc)

lyc = (13,160)
lyc[0] = 14
print(lyc)



'''
元组折包可以应用到任何可选代对象上,唯一的硬性要求是,被可迭代对
中的元素数量必须要跟接受这些元素的元组的空档数 致。除非我们用*
表示忽略多余的元素,在“川 来处理多余的元素”一节里,我会排到它
具体用法。 Python爱好若们很喜欢川元组拆色这个说法,但是可迭代元素
包这个表达也慢慢流行了起来,比如"PEP 3132 Extended Icrable Unpackin
(htp://www.pyhon.p/lev/ep/xp-3132)的标题就是这么用的。
'''
lax_coordinates = (33.9425, -118.408056)
s_latitude, longitude = lax_coordinates #元组拆包
print(s_latitude,longitude) #33.9425 -118.408056

lax_coordinates =(33.9425,-118.408056)
city, vear, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567')]
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

for country in traveler_ids:
    print(country)

metro_areas = [('Tokyo', 'Jp , 36.933, (35.689722, 139.691667)',
                '#0Delhi NCR', 'IN, 21.935, (28.613889, 77.208889)',
                'Mexico City', 'MX, 20.142, (19.433333, -99.1333)',
                'New York-Newark', 'US, 20.104, (40.808611, -74.020386)',
                'Sao Paulo', 'BR, 19.649, (-23. 547778, -46.635833)')]
m = metro_areas
#print(m[:15],m[:9],m[9]. format(', 'lat.', 'long.'))#fmtf:15} | (:9.4f] 1 (:9.4f)1
for name, cc, pop, Latitude, longitude in metro_areas: #0if longitude <= 0: #6print (fmt. format(name, latitude, longitude))
    print(name,cc,pop,(Latitude, longitude))
'''
0洛杉矶国际机场的经纬度。
@东京市的一些信息:市名、年份、人口(单位:百万)、人口变化(单位:百分比)和
面积(单位:平方千米)。
目一个元组列表,元组的形式为(country_code, passport-number)
4在迭代的过程中, passport变量被绑定到每个元组上。以9件
0%格式运算符能被匹配到对应的元组元素上。0for循环可以分别提取元组里的元素,也叫作拆包(anpacking),因为元组中第二个元素对我们没有什么用,所以它赋值给“-”占位符。
拆包让元组可以完美地被当作记录来使用,这也是下一节的话题。

2.3.2元组拆包示例2-7中,我们把元组('Tokyo', 2003, 32450, 0.66, 8014)里的元素分别赋值给变量
city, year, pop.chg和area,而这所有的赋值我们只用一行声明就写完了。同样,在后
面一行中,一个%运算符就把passport元组里的元素对应到了print函数的格式字符串空
档中。这两个都是对元组拆包的应用
序列构成的数组1 23

'''

a, b, *rest = range(5)
print(a, b, rest)
#(0, 1, [2, 3, 47)

a, b, *rest = range(3)
print(a, b,rest )
#(0, 1, [2])
a, b, *rest = range(2)
print(a, b, rest)
#(0, 1, [)


print(divmod(20, 8)) #(2, 4)

t =(20, 8)
print(divmod(*t)) #(2, 4)
quotient, remainder = divmod(*t)
print(quotient, remainder) #(2, 4)