'''
https://www.codewars.com/kata/5b358a1e228d316283001892/train/python

你以字符串的形式接收一个城市的名称，你需要返回一个字符串，通过使用星号（*）来显示每个字母在字符串中出现的次数。
例如："芝加哥
"芝加哥" --> "c:**,h:*,i:*,a:*,g:*,o:*"
如你所见，字母c只显示一次，但有两个星号。
返回的字符串应该只包括字母（不包括破折号、空格、撇号等）。输出中不应该有空格，不同的字母之间用逗号(,)隔开，如上例所示。
注意，返回的字符串必须按照字母在原始字符串中首次出现的顺序排列。更多的例子。
"曼谷" --> "b:*,a:*,n:*,g:*,k:**,o:*"
"拉斯维加斯" --> "l:*,a:**,s:**,v:*,e:*,g:*"玩得开心点！;)

Test.assert_equals(get_strings("Chicago"), "c:**,h:*,i:*,a:*,g:*,o:*")
Test.assert_equals(get_strings("Bangkok"), "b:*,a:*,n:*,g:*,k:**,o:*")
Test.assert_equals(get_strings("Las Vegas"), "l:*,a:**,s:**,v:*,e:*,g:*")
'''

city = "Chicago"
x = city[0] + city[1]
print(x)

print(1 == 1,1 == 2)
print(x[0] == x[1]) #True

city = "Chicago"
print(city.upper())
print([i for i in city if i == 'C' or i == 'c'])
print([i for i in city if i == 'C' or i == 'c'])

key = set(city.upper())
city_dict = dict(zip(key,[0 for i in range(len(city))]))
print('key:',key)
print(city_dict)

def get_strings(city):
    res = []
    for c in city:
        res.append(c)
    return res[1:]
print('get_str:',get_strings(city))


print(list(city))

def triangle_area(side_len, high):
    area = 0.5 * side_len * high
    return area

