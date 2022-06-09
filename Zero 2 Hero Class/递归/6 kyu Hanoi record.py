'''
https://www.codewars.com/kata/534eb5ad704a49dcfa000ba6/train/python

The task
Your task, is to calculate the minimal number of moves to win the game "Towers of Hanoi",
with given number of disks.

What is "Towers of Hanoi"?
Towers of Hanoi, is a simple game consisting of three rods, and a number of disks of different
sizes which can slide onto any rod. The puzzle starts with the disks in a neat stack in ascending
order of size on one rod, the smallest at the top, thus making a conical shape.

The objective of the puzzle is to move the entire stack to another rod, obeying the following
simple rules:

Only one disk can be moved at a time.
Each move consists of taking the upper disk from one of the stacks and placing it on top of
another stack i.e. a disk can only be moved if it is the uppermost disk on a stack.
No disk may be placed on top of a smaller disk.

什么是 "河内塔"？
河内塔，是一个简单的游戏，由三根杆子，和一些不同大小的圆盘组成，可以滑到任何一根杆子上。游戏开始时，
将大小不一的圆盘按升序整齐地堆放在一根杆子上，最小的在顶端，从而形成一个圆锥形。

这个谜题的目的是将整个圆盘移动到另一根杆上，并遵守以下简单的规则。

每次只能移动一个圆盘。
每次移动都是将其中一个堆栈中的上层圆盘放在另一个堆栈的顶部，也就是说，只有当一个圆盘是堆栈中最上层的
圆盘时才可以移动。
任何磁盘都不能放在较小磁盘的上面。
'''
#3rd solve by ericlee
def hanoi(disks):
    ori, more = [1], 2
    for i in range(disks-1):
        ori.append(ori[i]+more)
        print(ori[i],more)
        more*=2
    return ori[-1]

def hanoi(disks,move=0):
    if disks == 1:
        move += 1
        return move
    elif disks == 2:
        move += 3
        return move
    else:
        return 2*hanoi(disks-1,move)+1
print(hanoi(7))

#1st
def hanoi(disks):
    return 2 ** disks - 1

#2nd
#from gmpy2 import bit_mask as hanoi