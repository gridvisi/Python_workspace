import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
plt.plot(squares)
plt.show()


#die class

from random import randint


class Die():
    '''表示一个投掷骰子的类'''

    def __init__(self, num_sides=6):
        '''骰子默认为6面'''
        self.num_sides = num_sides

    def roll(self):
        '''返回一个位于1和骰子面数之间的随机值'''
        return randint(1, self.num_sides)

#from die import Die

# 创建一个D6
die = Die()

# 投掷几次骰子，并将结果存储到列表中
results = []
for rool_num in range(1000):
    result = die.roll()
    results.append(result)

# 分析结果
frequencies = []
for value in range(1, die.num_sides +1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
import pygal
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times"
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_label = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')

#原文链接：https :/ /blog.csdn.ne t /qq_3759694 3 /articl e /detail s /107242404


'''

import matplotlib.pyplot as plt
from random_walk import RandomWalk

# 创建一个 RandomWalk 实例，并将其包含的点都绘制出来
rw = RandomWalk()
rw.fill_walk()
plt.scatter(rw.x_values, rw.y_values, s=15)
plt.show()


'''
