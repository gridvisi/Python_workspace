'''
从低到高
运算符 描述
lambda Lambda表达式
or 布尔“或”
and 布尔“与”
not x 布尔“非”
in，not in 成员测试
is，is not 同一性测试
<，<=，>，>=，!=，== 比较
| 按位或
^ 按位异或
& 按位与
<<，>> 移位
+，- 加法与减法
*，/，% 乘法、除法与取余
+x，-x 正负号
~x 按位翻转
** 指数
x.attribute 属性参考
x[index] 下标
x[index:index] 寻址段
f(arguments...) 函数调用
(experession,...) 绑定或元组显示
[expression,...] 列表显示
{key:datum,...} 字典显示
'expression,...' 字符串转换
'''
#万物皆有裂痕，那是光照进来的地方

score = [98,84,56,79,60,107,40]
print(all([40 <= i < 100 for i in score]))


mcree = ["Tuesday", "Thursday", "Saturday" , "Sunday"]
#Mcree周二、周四、周六和周日有空
Jack = [ ]
Leo = ["Saturday", "Sunday"]
print(mcree and Leo)
print(Leo and mcree)
print(Jack and Leo)

Alan = ['Friday', 'Sunday']
Summer = ["Saturday"]
print(Alan and Summer)


alan_agenda = ["Friday","Sunday"]   # 数组里有两个时间，周五和周日
leo_agenda =  ["Saturday","Sunday",'Monday']  # 同学他周六和周日有空
jack_agenda = []
summer = ["Saturday"]
mcree_agenda = ['Tuesday','Tursday']

week = ['Monday','Tuesday','Wednesday','Tursday','Friday','Saturday','Sunday']
for Happy_time in week:
    if Happy_time in alan_agenda and Happy_time in leo_agenda:
        print('alan and leo play game on',Happy_time)

for lee_time in week:
    if lee_time in alan_agenda or lee_time in leo_agenda or lee_time in jack_agenda or lee_time in summer:
        print('tearch lee class:',lee_time)



#for Happy_time in week:
my_study_time = ("Friday" or "Sunday")
my_play_time = ('' or "Sunday")
print(my_study_time,my_play_time)

your_study_time = ("Saturday" or "Sunday")
your_play_time = ("Sunday" or '' )

for happy_time in week:
    if Happy_time in "某人的时间段" and Happy_time in "另个人的时间段":
        print(Happy_time)

my_agenda = ["Friday", "Sunday"]  # 数组里有两个时间，周五和周日
his_agenda = ["Saturday", "Sunday"]  # 同学他周六和周日有空
res = []
for Happy_time in week:
    if Happy_time in my_agenda and Happy_time in his_agenda:
        res.append(Happy_time)
print(res)

res = "Friday" or "Sunday" and "Saturday" or "Sunday"
print(your_study_time,your_play_time,res)
print(res)

print("Sunday" and "Saturday" )
