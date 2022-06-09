'''
榔头、钉子和榫卯结构


如果将python的高级函数rotate比作榔头，约瑟夫问题比作钉子，那么是先有榔头，还是先有钉子？
显然，约瑟夫问题在python语言发明之前就有了。

直到你会用rotate函数后，忍不住感慨rotate简直是为约瑟夫问题量身定做的。当然，高手不见得
用rotate，就像榫卯结构的家具没有一根钉子，没有钉子，自然用不到榔头。

约瑟夫环问题的名字来源于古代历史学家约瑟夫一生中最重要的事件：根据他的故事，他和他的40名
士兵在一次围攻中被罗马人困在一个山洞里。

他们拒绝向敌人投降，而是选择了集体自杀，但有一个转折：他们围成一个圆圈，接着每三个人杀
一个人，直到剩下最后一个人（而且应该是自杀来结束这一行为）。
'''

from collections import deque
# 运用高级函数rotate deque
person,nth = [i for i in range(17)],7
p = deque(person).rotate(7)

print(p)

def dead_live(person,nth):
    circle_p = [i for i in person]
    d, result = deque(circle_p), []

    while d:
        d.rotate(-nth+1)
        print(d)
        result.append(d.popleft())
    return result
print(dead_live(person,nth))

#高手总是乐此不疲的少几行代码：
#Top 2nd solution
from collections import deque
def josephus(items,k):
    q = deque(items)
    return [[q.rotate(1-k), q.popleft()][1] for _ in items]

#不使用高级函数

def josephus(person, nth):
    i, res = 0, []
    while len(person) > 0:
        i = (i + nth - 1) % len(person)
        res.append(person.pop(i))
    return res