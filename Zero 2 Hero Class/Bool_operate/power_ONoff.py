chandi1 = 2
chandi2 = 3

#1-20
t1 = 0
t2 = 0
for y in range(1,21):
    if y % 2 == 0:  #
        t1 += 1
    if y % 3 == 0:
        t2 += 1
print(t1,t2)




name = 'lzj'
jiami = ''
for i in name:
    jiami += str(ord(i)+3)+' '
print(jiami)
print(jiami.split(" "))

yuanwen = ''
for c in jiami.split(" "):
    if c != '':
        yuanwen += chr(int(c)-3)
print(yuanwen)


kevin, ada = 11, 17
print(kevin == ada) #True 年龄相同，False 不一样
mother,father = 35,34

#return

# True #bool布尔类型
"True" #字符串


red,yellow,green = 1,1,1 #关灯状态

if red == 1:
    yellow = 0
    green = 0
print('red,yellow,green:',red,yellow,green)




# bool_logic 布尔运算符合
# 灯的开关 0  1
#
# input: output:
#  1     0
#  0     1

#  True  False
#  0     1

print(True == 1,False == 0)

def power_on_off(x): #power_on ,power_off,
    return not x     #not = 不
x = 1
print(power_on_off(x))

#bool 运算符合

# or，and，not

a = [i for i in range(11) if i%2==0]
b = [i for i in range(11) if i%3==0]
minute,sec = 61//60,61%60

c = [i for i in range(11) if i%3==0 and i%2==0]
d = [i for i in range(11) if i%3==0 or i%2==0]

print('c:',c)
print('d:',d)

print(not(0))
#

#红绿灯
# red -> green -> yellow ->red --- --->
def traffic_light(color):
    if color=='red':return 'green'
    if color=='green':return 'yellow'
    if color=='yellow':return 'red'
    if color == None:return "打电话叫人来修"
    if color == "red green yellow":return "打电话叫人来修"

color = 'green'
color = None
color = "red green yellow" #三灯齐齐亮了
print(traffic_light(color))