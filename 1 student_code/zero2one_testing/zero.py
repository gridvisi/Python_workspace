def mutilpy(a,b):
    return a * b

#
print([i for i in range(3,11,3)])
print([i for i in range(1,11) if i % 3 == 0])

# range(1,7) score = 100
ada = alex = 10
print(id(ada),id(alex))

print('alex:',ada,alex)


#1 + 。。。。10937482

print(sum([i for i in range(1000)]))
#print(sum([i for i in range(101)]))



#10937483

print(1 == 2)
print('a' == 'A')
print(100 == 10 * 10)

#变量有类型
age = 12
name = 'feifei'
#print(name + age)

#list
alex_profile = ['boy','12','programming'] # want_list

alex_profile.append('football')

print('new:',alex_profile)


print('1:',alex_profile)

print('2:',alex_profile[2])

ada_profile = 'boy','12','programming'
print('2:',ada_profile)

ade_profile = ('boy','12','programming')
print('3:',ade_profile)

print('==',ada_profile == ade_profile)

for item in ada_profile:
    print('4:',item)

for item in ade_profile:
    print('5:',item)

for gender in ['male','female']:
    print('gender:',gender)

alex = "boy"
ada = 'girl'

print('alex == girl',alex == 'girl')

boy_name = "alex"
girl_name = "ada"
teacher_name = "alex"
print(boy_name == teacher_name)

#say hello

print(boy_name,girl_name)

name = '1+1'
print(name)
name = 1 + 1
print(name)



#重庆 beijing
#追加一个城市比如 "shenzhen": "深圳"
city = ["chongqing","beijing","成都"]

print(city)

#["chongqing","beijing","成都"]
#如何追加一个城市进来

city.append(["shenzhen","深圳"])

city = {"chongqing":"重庆","北京":"beijing" }

print(city["chongqing"],city["北京"])
city["shenzhen"] = "深圳"
print(city)

#{'chongqing': '重庆', '北京': 'beijing', 'shenzhen': '深圳'}


key = [" 科学启蒙系列 "," 四大名著 "]
value1 = ["天气","地球","身体"]
value2 = ["四大名著 ","三国演义","西游记","水浒"]
books = {"科学启蒙系列": ["天气","地球","身体"],
            "四大名著": ["三国演义","西游记","水浒"]}

print(books["四大名著"])
#输出结果
#['三国演义', '西游记', '水浒']

