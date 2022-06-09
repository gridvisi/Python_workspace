'''
https://brilliant.org/daily-problems/pizza-thief/

实际运用布尔运算有许多极易忽略的细节，恰好经历测验犯错后，才能牢记。
导入课程见本期公众号链接：第七节布尔运算测验


如何有效的运用布尔运算帮助解决逻辑问题，引入今天的任务是谁吃了披萨
Donnie兴奋地等着课间吃放在冰箱的那块比萨饼，却发现它已经被吃掉了！他知道他的
四个室友中有一个人吃了，依据下面线索​推理是谁吃了？

小明唯一有把握的是，他的四个室友中有一个吃了。而当他询问他们时，他直觉到其中只
有一个人说的是实话。所以，下面是三条陈述保证是真的线索，后面是四个室友的回答：

每个室友都做了一个声明。其中一个室友说的是真话，其他三个室友说的是假话。
只有吃了披萨的室友有负疚感的。其他人都没有。
鉴于每个室友的说法，"真相 "和 "谎言 "的标签是准确的。
拉斐尔​的表现：内疚，不内疚
拉斐尔--"迈克吃了披萨"。
利奥的表现：内疚，不内疚
里奥--"我没有吃披萨。"
迈克的表现​：内疚，不内疚
迈克--"维纳斯吃了披萨"。
金星表现：内疚，不内疚

金星--"迈克说我吃了披萨，是在撒谎。"
'''

roommates = {"Raph":  lambda x, y: (not y[0] ^ x[2]),
             "Leo":   lambda x, y: (not y[1] ^ (not x[1])),
             "Mike":  lambda x, y: (not y[2] ^ x[3]),
             "Venus": lambda x, y: (not y[3] ^ (not x[3]))}

conditions = [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]

for pizza in conditions:
    for liars in conditions:
        if all([statement(pizza, liars) for statement in roommates.values()]):
            for n, p, l in zip(roommates.keys(), pizza, liars):
                print(f"{n:<6} guilty: {p}, truth: {l}")

print(1 ^ 0)
print(1 ^ 1)
print(not 1 ^ 0)
print(not (1 ^ 0))
print(not 1 ^ 1)
print(not (1 ^ 0))
print(not 0 ^ 0)
print(not 0 ^ 1)