import datetime

# 为什么街道两边的门牌号分别按奇偶排序？
odd_doorplate = [11,13,15,17]
even_doorplate = [14,16,18,20]


# 一个年级有3个班，如何设计学生证的号码，通过首位数即能判断班级？


# 注射疫苗要避免人群聚集，设计一个流程在一天的时间内

# 如何查找班上姓李的？姓王 etc

person = ["lyc","诸葛亮", "李张梓霖","张李梓沐","邓爱希香","lyc" ,"李张总领", "张涵奇", "周宏宇", "唐诚心", "刘一芝",
          "汪刚", "郑嘉", "龙心", "谭心", "邢小台", "宋雨","张吴含","张吴","李懿轩","lyc"]

print(person.count('lyc'))
person.append('batman')
print(person[-1],person[1])
lzh = '李正浩'
print('李正浩'[0],)
# 变量name来表示所有人的名字
# 如果  那么  if
print(person[2:7])
for name in person:
    if name[0] == '李':
        print(name)


class_1 = ['abc']
class_6 = ['xyz','lzh','李正浩']

print('李正浩' in class_1)
lzh = '00000100100100'
lzh_int = [int(i) for i in list(lzh)]
print('lzh_int:',lzh_int,sum(lzh_int))

#count money
print('count how many 1 in lzh:',lzh.count('1'))
print(list(lzh))
print(sum([1,2,3]))
print(lzh.count('1') == 1)



x = '李正浩' in class_6
print(x + 1)

print('1==2',1==2)
print(1 == True,0 == False)

if '李正浩' in person:
    print('李正浩:',"okay")
else:
    print('李正浩:',"not in person")



start = person.index("张李梓沐")
end = person.index("周宏宇")
print(f"{start}:"+f"{end}",person[start:end])

print('张涵奇',person.index("张涵奇"))

print('The first,second,third,fourth',[])
print(person[:-1])
print(person[::-1])
print(person[1:2])
start,end = person.index( "李张梓霖"),person.index( "龙心")+1
print(person.index( "李张梓霖"),person.index( "龙心"))
print(person[start:end])
print([i for i in enumerate(person)])
person_tuple = [i for i in enumerate(person)]
#person_tuple[0][0] = 1
print(person_tuple)