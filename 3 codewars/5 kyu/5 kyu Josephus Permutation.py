'''
https://www.codewars.com/kata/5550d638a99ddb113e0000a2/train/python
'''

person,nth = ["C","o","d","e","W","a","r","s"],4 #['e', 's', 'W', 'o', 'C', 'd', 'r', 'a'])

from collections import deque
def dead_live(person,nth):
    circle_1 = [i for i in person]
    #circle_2 = [i for i in range(nth)]
    #circle = circle_1 + circle_2
    d, result = deque(circle_1), []
    while d:
        d.rotate(-nth+1)
        print(d)
        result.append(d.popleft())
    return result

#person,nth = 41,3
#person,nth = [1,2,3,4,5,6,7],3  #[3, 6, 2, 7, 5, 1, 4]
#person,nth = [1,2,3,4,5,6,7,8,9,10],2  #[2, 4, 6, 8, 10, 3, 7, 1, 9, 5]
print(dead_live(person,nth))

#Top 1st solution
def josephus(person, nth):
    i, res = 0, []
    while len(person) > 0:
        i = (i + nth - 1) % len(person)
        res.append(person.pop(i))
    return res
person,nth = ["C","o","d","e","W","a","r","s"],4
print(josephus(person, nth))

#Top 2nd solution
from collections import deque
def josephus(items,k):
    q = deque(items)
    return [[q.rotate(1-k), q.popleft()][1] for _ in items]

#rotate use tips
def rotate(input, d):
    Lfirst = input[0: d]
    Lsecond = input[d:]
    Rfirst = input[0: len(input) - d]
    Rsecond = input[len(input) - d:]

    print("头部切片翻转 : ", (Lsecond + Lfirst))
    print("尾部切片翻转 : ", (Rsecond + Rfirst))

if __name__ == "__main__":
    input = 'codewars'
    d = 2  # 截取两个字符
    rotate(input, d)