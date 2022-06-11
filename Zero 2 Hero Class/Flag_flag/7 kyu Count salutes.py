'''
https://www.codewars.com/kata/605ae9e1d2be8a0023b494ed/train/python

说明
有一条狭窄的走廊，人们只能在其中左右走动。当两个人在走廊上相遇时，按照传统，
他们必须互相敬礼。人们以同样的速度左右移动。

你的任务是写一个函数，给定一个在走廊上移动的人的字符串表示，
。
注意：当人们相遇时，会发生2个敬礼，一个向另一个敬礼，反之亦然。

输入内容
向右移动的人用>表示，向左移动的人用<表示，例如输入是>--<-->->。

例子
输入。>----->-----<--<
产出： 8

解释： 向右移动的两个人都会遇到向左移动的两个人。
因此，总共会发生4次相遇，会发生8次敬礼。

输入。<---<--->----<
产出： 2

解释： 只有一次会mian。
'''

def count_salutes(hallway):
    # Your code goes here :)
    left,right = [],[]
    cunt = 0
    for i,arrow in enumerate(hallway):
        if arrow == '>':
            right.append(i)
        elif arrow == '<':
            #left.append(i)
            cunt += 2*sum([i>r for r in right])
    return cunt

#1st
def count_salutes(hallway: str) -> int:
    right = 0
    salutes = 0
    for p in hallway:
        if p == '>':
            right += 1
        if p == '<':
            salutes += 2*right
    return salutes

hallway = '<----<---<-->'
hallway = '>-<->-<'
print(count_salutes(hallway))