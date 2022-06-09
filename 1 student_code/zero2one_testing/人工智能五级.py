
'''
一、单项选择题（共 15 小题，每小题 2 分，共 30 分）
1. 现有代码 t=('a')，在 python3 解释器中查看 type(t)的到的结果为( )
A <class 'str'>
B <class 'tuple'>
C (class 'str')
D (class 'tuple')

2. python3 解释器执行如图的程序结果是什么（ ）
A b c B a c C b d D a b 3. 有集合 s = {1,2,3}，
python3 解释器执行 del s[2] 的结果为( )
A 3
B 2
C {1，2}
D TypeError 'set' object doesn't support item deletion 4.

python3 解释器对列表[1,2,（3,4）,5,6]使用 reverse 方法执行的结果为( )
A [6, 5, （3,4）, 2, 1]
B [6, 5, （3,4）, 2, 1]
C [6, 5, 2, 1, （3,4）]
D 报错 5.

关于 hash 函数，下面说法正确的是( )
A hash 函数提高了数据安全性
B hash 函数可以用来对密码进行加密
C hash 函数可以用来校验文件的一致性
D 上面说的都对

6. 以下代码执行的输出结果是：
A 出错
B Hello!Hello!
C Hello!Hello!
[2] D Hello!Hello! []

7. 执行以下代码，运行的结果是（ ）
A[‘H’, ‘ppy birthd’, ‘y to you!’]
B"Happy birthday to you!"
C 运行出错
D[‘Happy’, ‘birthday’, ‘to’,‘you!’]

8. 表 达 式 sorted([13, 1, 237, 89, 100], key=lambda x: len(str(x)) 的值为（ ）
A [1,13,89,100,237]
B [1, 13, 89, 237, 100]
C [237,100,89,13,1
D [13,1,237,89,100]

9. 关于算法的描述，以下选项中错误的是（ ）
A 算法是指解题方案的准确而完整的描述
B 算法的复杂度主要包括时间复杂度和数据复杂度
C 算法具有可行性、确定性、有穷性的基本特征
D 算法的基本要素包括数据对象的运算和操作及算 法的控制结构

10. 箱子里面有 16 张牌：红桃 A、Q、4，黑桃 J、8、 4、2、7、3，
草花 K、Q、4、5、6，方块 A、5。 无名从中取出一张，然后把点数告诉了有名，
把 花色告诉了真名。

无名让有名和真名去猜自己拿 到的牌，下面是有名和真名的
对话：（ ）

有名：我不知道这张牌
真名：我知道你不知道这张牌
有名：现在我知道了
真名：我也知道了
那么请问无名拿到的到底是什么牌？（

 A A 红桃 A
 B 红桃 4
 C 方块 5
 D 方块 A

11. 已知以下程序段，要想输出结果为 1,2,3，应该 使用的表达式是：（ ）
A print(z)
B print(",".join(x))
C print(x)
D print(",".join(z))

12. 下面代码的输出结果是（ ）
A 130.042
B 5.5e31
C 130.42
D 5.5e3

13. 下面代码的输出结果是（ ）
A 星期二
B 星期三
C 星期四
D 星期一

14. TempStr = "Hello World",以下选项中可以输出 "World"子串的是（ ）
A print(TempStr[-5:-1])
B print(TempStr[-5:0])
C print(TempStr[-4:-1])
D print(TempStr[-5:])

15. 下程序的输出结果是：（ ）
'''
t = ('a')
print(type(t))

#2
for x in {"a":"b","c":"d"}:
    print(x)

D = {"a":"b","c":"d"}
print(D)

#3
s = {1,2,3}
#del s[2]

#4
sl = [1,2,(3,4),5,6]
sl.reverse()
print(sl)


#7
ans = sorted([13, 1, 33,237, 89, 100], key=lambda x: len(str(x)))
print(ans)