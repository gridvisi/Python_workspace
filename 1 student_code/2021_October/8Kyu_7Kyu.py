

# 1st Question
# 7 kyu Shortest Word
# https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/train/python
'''
        test.assert_equals(find_short("bitcoin take over the world maybe who knows perhaps"), 3)
        test.assert_equals(find_short("turns out random test cases are easier than writing out basic ones"), 3)
        test.assert_equals(find_short("lets talk about javascript the best language"), 3)
        test.assert_equals(find_short("i want to travel the world writing code one day"), 1)
        test.assert_equals(find_short("Lets all go on holiday somewhere very cold"), 2)
        test.assert_equals(find_short("Let's travel abroad shall we"), 2)
'''

s = " "
def find_short(s):
    # your code here
    return len(sorted(s.split(" "),key=len)[0])
print('排序1：',sorted(['Azxjhfgjehxdghkzd','phil', 'jack','thomas','zhou hongyu'],key=len))

print('排序2：',sorted([6, 25, 3, 7, 5, 5, 7, 3, 23]))

#clue, keywords



# 2nd Question
# 7 kyu Even numbers in an array
# https://www.codewars.com/kata/5a431c0de1ce0ec33a00000c/train/python
'''
Given an array of digitals numbers, return a new array of length number 
containing the last even numbers from the original array (in the same order). 
The original array will be not empty and will contain at least "number" even numbers.

For example:

([1, 2, 3, 4, 5, 6, 7, 8, 9], 3) => [4, 6, 8]
([-22, 5, 3, 11, 26, -6, -7, -8, -9, -8, 26], 2) => [-8, 26]
([6, -25, 3, 7, 5, 5, 7, -3, 23], 1) => [6]
'''
# list slice
def even_numbers(arr,n):
    return [i for i in arr if not i%2][-n:]


def even_numbers(arr,n):
    return list(filter(lambda n: n % 2 == 0, arr))[-n:]


#3rd Question
# 8 kyu Expressions Matter
# https://www.codewars.com/kata/5ae62fcf252e66d44d00008e/train/python
'''
Task
Given three integers a ,b ,c, return the largest number obtained after inserting the following operators and brackets: +, *, ()
In other words , try every combination of a,b,c with [*+()] , and return the Maximum Obtained
Consider an Example :
With the numbers are 1, 2 and 3 , here are some ways of placing signs and brackets:

1 * (2 + 3) = 5
1 * 2 * 3 = 6
1 + 2 * 3 = 7
(1 + 2) * 3 = 9
So the maximum value that you can obtain is 9.

Notes
The numbers are always positive.
The numbers are in the range (1  ≤  a, b, c  ≤  10).
You can use the same operation more than once.
It's not necessary to place all the signs and brackets.
Repetition in numbers may occur .
You cannot swap the operands. For instance, in the given example you cannot get expression (1 + 3) * 2 = 8.


        test.assert_equals(expression_matter(2, 1, 2), 6)
        test.assert_equals(expression_matter(2, 1, 1), 4)
        test.assert_equals(expression_matter(2, 2, 4), 16)
        test.assert_equals(expression_matter(3, 3, 3), 27)
        test.assert_equals(expression_matter(1, 1, 1), 3)
        test.assert_equals(expression_matter(1, 2, 3), 9)
        test.assert_equals(expression_matter(1, 3, 1), 5)
        test.assert_equals(expression_matter(2, 2, 2), 8)
        test.assert_equals(expression_matter(5, 1, 3), 20)
        test.assert_equals(expression_matter(3, 5, 7), 105)
        test.assert_equals(expression_matter(5, 6, 1), 35)
        test.assert_equals(expression_matter(1, 6, 1), 8)
        test.assert_equals(expression_matter(2, 6, 1), 14)
        test.assert_equals(expression_matter(6, 7, 1), 48)
        test.assert_equals(expression_matter(2, 10, 3), 60)
        test.assert_equals(expression_matter(1, 8, 3), 27)
        test.assert_equals(expression_matter(9, 7, 2), 126)
        test.assert_equals(expression_matter(1, 1, 10), 20)
        test.assert_equals(expression_matter(9, 1, 1), 18)
        test.assert_equals(expression_matter(10, 5, 6), 300)
        test.assert_equals(expression_matter(1, 10, 1), 12)
'''


def expression_matter(a, b, c):
    return max([a + b + c, a * b * c, (a + b) * c, a * (b + c), a + b * c, a * b + c])

def expression_matter(a, b, c):
    return max(a*b*c, a+b+c, (a+b)*c, a*(b+c))



#4th
# 7 kyu Exclamation marks series
# Move all exclamation marks to the end of the sentence
'''
remove("Hi!") === "Hi!"
remove("Hi! Hi!") === "Hi Hi!!"
remove("Hi! Hi! Hi!") === "Hi Hi Hi!!!"
remove("Hi! !Hi Hi!") === "Hi Hi Hi!!!"
remove("Hi! Hi!! Hi!") === "Hi Hi Hi!!!!"
'''
def remove(s):
    head, tail = "",""
    for i in s:
        if i != "!":
            head += i
        else:
            tail += "!"
    return head + tail

def remove(s):
    return s.replace('!','') + s.count('!') * '!'

def remove(s):
    return s.replace('!', '') + '!'*s.count('!')

def remove(s: str) -> str:
    r = s.replace('!', '')
    return r + '!' * (len(s) - len(r))


#5th 7 kyu Computer problem series #1: Fill the Hard Disk Drive
'''
Your task is to determine how many files of the copy queue you will be able to save into your Hard Disk Drive. The files must be saved in the order they appear in the queue.

Input:
Array of file sizes (0 <= s <= 100)
Capacity of the HD (0 <= c <= 500)
Output:
Number of files that can be fully saved in the HD.
Examples:
save([4,4,4,3,3], 12) -> 3
# 4+4+4 <= 12, but 4+4+4+3 > 12
save([4,4,4,3,3], 11) -> 2
# 4+4 <= 11, but 4+4+4 > 11
Do not expect any negative or invalid inputs.

你的任务是确定你能将复制队列中的多少个文件保存到你的硬盘上。这些文件必须按照它们在队列中
出现的顺序保存。

输入。
文件大小的阵列(0 <= s <= 100)
硬盘的容量 (0 <= c <= 500)
输出。
可以完全保存在HD中的文件数量。
例子。
save([4,4,4,3,3], 12) -> 3
# 4+4+4 <= 12, 但 4+4+4+3 > 12
save([4,4,4,3,3], 11) -> 2
# 4+4 <= 11, 但 4+4+4 > 11
do not expect 任何负面或无效的输入。

'''
#1st
def save(sizes, hd):
    for i,s in enumerate(sizes):
        if hd < s: return i
        hd -= s
    return len(sizes)

def save(sizes, hd):
    max_file = []
    for i in sizes:
        max_file.append(i)
        if sum(max_file) > hd:
            return len(max_file) - 1
    else:return len(sizes)

from bisect import bisect
from itertools import accumulate
def save(sizes, hd):
    return bisect(list(accumulate(sizes)), hd)


def save(sizes, hd):
    return save(sizes[:-1], hd) if sum(sizes) > hd else len(sizes)


from itertools import *
def save(sizes, hd):
    return sum(1 for _ in takewhile(hd.__ge__, accumulate(sizes)))


def save(sizes, hd):
    return sum(1 for i in range(len(sizes)) if sum(sizes[:i+1])<=hd)


#6th set()
'''
What will the output be?

A) {}
B) {"Brain", "Yakko", "Wakko"}
C) {"Mike", "Pinky"}
D) {'Pinky', 'Dot', 'Mike'}
'''

phil = {'math','programming','english'}
jason = {'physics','programming','history'}
print('phil and jason:',phil and jason)
print('交集：',[course for course in phil if course in jason])
print('^',phil ^ jason)
print('&',phil & jason)
#print(phil + jason) #去掉重复
print(phil - jason)

s = ['a','b','c','a']
print(set(s))

#7th 8 kyu USD => CNY
def usdcny(usd):
    return "%.2f" % (usd * 6.75) + " Chinese Yuan"

print('usd cny:',usdcny(7))

def usdcny(usd):
    return "1 Chinese Yuan"



#8th 7 kyu last digits of a number
def solution(n,d):
    return [] if d<=0 else list(map(int,list(str(n)[-d:])))

def solution(n,d):
    s = str(n)
    return list(map(int,s))[-d if d>0 else len(s):]

# The 9th Question
#7 kyu Pairs of integers from 0 to n
'''
generate_pairs(2) should return
[ [0, 0], [0, 1], [0, 2], [1, 1], [1, 2], [2, 2] ]
'''
def generate_pairs(n):
    ans = []
    for i in range(n+1):
        for j in range(n+1):
            if j >= i:
                ans.append([i,j])
    return ans

def generate_pairs(n):
    return [[i,j] for i in range(n+1) for j in range(i, n+1)]

#10th Question
# 7 kyu Basic JS - Calculating averages
# https://www.codewars.com/kata/529f32794a6db5d32a00071f/solutions/python
class Calculator:
    @staticmethod
    def average(*args):
        return sum([*args])/len([*args]) if len([*args]) else 0


class Calculator:
    @staticmethod
    def average(*_a):
        return sum( _a ) / len( _a ) if len( _a ) >  0 else 0

from statistics import mean
class Calculator:
    @staticmethod
    def average(*args):
        return len(args) and mean(args)

#11th Question
#7 kyu Series of integers from 0 to n

def generate_integers(n):
    return list(range(n + 1))

def generate_integers(n):
    lst = []
    for i in range(n+1):
        lst.append(list(range(i)))
    return lst


#12th Question
'''
一堂历史课
小马快车是1859-60年在美国运营的一项邮件服务。

小马快车在被横贯大陆的电报淘汰之前，它将大西洋和太平洋海岸之间的信息传递时间缩短到大约
10天。

它是如何工作的有一些站点，其中骑手换上一匹新马，继续前进，或
将邮件袋交给下一个骑手,站点是沿小马快车路线从一个站点到下一个站点的
距离（英里）的列表/阵列。
实施骑手方法/功能，以返回有多少骑手需要将邮件从一端送到另一端。
注意：每个骑手尽可能地旅行，但绝不超过100英里。

好运DM
7 kyu The Pony Express
https://www.codewars.com/kata/5b18e9e06aefb52e1d0001e9/train/python
'''
def riders(stations):
    horse = 1
    distance = 100
    for i in stations:
        if distance < i:
            horse += 1
            distance = 100
        distance -= i  #考虑空缺这一行考察学生
    return horse
print()

# not good solution
def riders(stations):
    horse = 1
    distance = 0
    for i in stations:
        distance += i
        if distance >= 100:
            horse += 1
            distance = i
    return horse

stations = [6, 24, 6, 8, 28, 8, 23, 47, 17, 29,
            37, 18, 40, 49] #, 4

print(riders(stations))

#First solution
def riders(stations):
    riders, travelled = 1, 0
    # [43, 23, 40, 13]), 2)
    for dist in stations:
        if travelled + dist > 100:
            riders += 1
            travelled = dist
        else:
            travelled += dist
    return riders


#13 Question
#8 kyu Is it even?
def is_even(n):
    return n%2 == 0


#14 Question
#7 kyu Number of People in the Bus
# https://www.codewars.com/kata/5648b12ce68d9daa6b000099/train/python


def number(bus_stops):
    person = 0
    for c in bus_stops:
        person += c[0]
        person -= c[1]
    return person

def number(bus_stops):
    return sum([stop[0] - stop[1] for stop in bus_stops])

def number(bus_stops):
    return sum(on - off for on, off in bus_stops)


#15 Question
# 7 kyu Bits Battle
# https://www.codewars.com/kata/58856a06760b85c4e6000055/train/python
'''
他的奇数和偶数正在相互争斗!

你会得到一个正整数的列表。列表中的奇数将使用它们的二进制表示法中的1比特进行战斗，
而偶数将使用它们的0比特进行战斗。如果列表中存在，数字0将是中立的，因此不为任何一方而战。

你应该返回。

如果奇数的1位数大于偶数的0位数，则赔率获胜
如果奇数的1的数量小于偶数的0，则偶数获胜
如果相等则平局，包括如果列表为空
请注意，任何可能出现在二进制表示中的前缀，例如0b，不应该被计入战斗。

例子。
对于一个输入的列表[5, 3, 14]。

赔率。5和3 => 101和11 => 四个1
偶数：14 => 1110 => 一个0
结果：赔率以4-1赢得战斗

如果你喜欢这个卡塔，你可以在这里找到一个不错的变体。

基本谜题游戏二进制比特
'''
def bits_battle(numbers):
    odd,even = 0,0
    for i in numbers:
        print(bin(i))
        if i%2:odd += bin(i)[2:].count('1')
        else:even += bin(i)[2:].count('0')
    return 'tie' if odd == even else 'odds win' if odd>even else 'evens win'

numbers = [1, 13, 16] # 'tie'

print(bits_battle(numbers))


#16 Question
# 8 kyu Third Angle of a Triangle
# https://www.codewars.com/kata/5a023c426975981341000014/train/python
def other_angle(a, b):
    return 180 - a- b


#17 Question
# 7 kyu Consecutive letters
# https://www.codewars.com/kata/5ce6728c939bf80029988b57/train/python
'''
test.assert_equals(solve("abc"),True)
test.assert_equals(solve("abd"), False)
test.assert_equals(solve("dabc"),True)
test.assert_equals(solve("abbc"), False)
'''
import string
def solve(st):
    s,sort_st = string.ascii_lowercase,sorted(list(st))
    it,seq = iter(sort_st),s[s.index(sort_st[0]):s.index(sort_st[0])+len(st)]
    #print(list(it))
    print(seq)
    return all([next(it) == i for i in seq])


import string

def solve(st):
  return ''.join(sorted(st)) in string.ascii_letters
st = 'dabce'
print(solve(st))


def solve(s):
    return len(s) == len(set(s)) == ord(max(s)) - ord(min(s)) + 1

from string import ascii_lowercase

def solve(string: str) -> bool:
    """
    Check if the given string contains consecutive letters as they
    appear in the English alphabet and if each letter occurs only once.
    """
    char_ixs = sorted(map(ascii_lowercase.index, string))
    return all([n - p == 1 for (p, n) in list(zip(char_ixs, char_ixs[1:]))])


'''

https://www.codewars.com/kata/56d904db9963e9cf5000037d

Series:
01: A and B?
02: Incomplete string
03: True or False
04: Something capitalized
05: Uniq or not Uniq
06: Spatiotemporal index
07: Math of Primary School
08: Math of Middle school
09: From nothingness To nothingness
10: Not perfect? Throw away!
11: Welcome to take the bus
12: A happy day will come
13: Sum of 15(Hetu Luosliu)
14: Nebula or Vortex
15: Sport Star
16: Falsetto Rap Concert
17: Wind whispers
18: Mobile phone simulator
19: Join but not join
20: I hate big and small
21: I want to become diabetic ;-)
22: How many blocks?
23: Operator hidden in a string
24: Substring Magic
25: Report about something
26: Retention and discard I
27: Retention and discard II
28: How many "word"?
29: Hail and Waterfall
30: Love Forever
31: Digital swimming pool
32: Archery contest
33: The repair of parchment
34: Who are you?
35: Safe position
Special recommendation
Another series, innovative and interesting, medium difficulty. People who like to challenge, can try these kata:

Play Tetris : Shape anastomosis
Play FlappyBird : Advance Bravely
'''