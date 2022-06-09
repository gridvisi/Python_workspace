'''
https://www.codewars.com/kata/5f70e4cce10f9e0001c8995a/train/python

There are some stones on Bob's table in a row, and each of them can be red, green or
blue, indicated by the characters R, G, and B. Help Bob find the minimum number of
stones Bob needs to remove from the table so that each pair of adjacent stones is unique.
鲍勃的桌子上有一些石头，排成一排，每一个石头都可以是红色、绿色或蓝色，用字符R、G、B表示，帮助鲍勃找到鲍勃需要
从桌子上移走的最少的石头数量，使每一对相邻的石头都是独一无二的。
Examples:
"RGBRGBRGGB"   => 1
"RGGRGBBRGRR"  => 3
"RRRRGGGGBBBB" => 9

'''
stones = "RRRRGGGGBBBB"
def solution(stones):
    cunt = 0
    for i,e in enumerate(stones):
        if i < len(stones)-1 and stones[i] == stones[i+1]:
            cunt += 1
    return cunt
print(solution(stones))

#1st solution
def solution(s):
    st=[1 for i in range(1,len(s)) if s[i-1] == s[i]]
    return sum(st)

#2nd solution

def solution(s):
    return sum(1 for i in range(len(s)) if i and s[i-1]==s[i])

#3rd solution

from itertools import groupby
def solution(stones):
    return sum(len(list(l))-1 for _,l in groupby(stones))

#4th solution
import re
def solution(stones):
    return sum( len(m[0])-1 for m in re.finditer(r'(.)\1+',stones) )

#5th solution
def solution(stones):
    counter = -1
    previous_stone = stones[0]

    for stone in stones:
        if previous_stone == stone:
            counter += 1

        else: previous_stone = stone

    return counter

#6th solution
def solution(stones):
    res = 0
    last = None

    for i in range(len(stones)):
        current = stones[i]

        if current == last:
            res += 1

        last = current
    return res

#7th solution  fancy and cute !!!
def solution(s):
    return sum(i == j for i,j in zip(s,s[1:]))

#8th solution
def solution(stones):
    count=0
    check=stones[0]
    for x in range(1,len(stones)):
        if stones[x]==check:
            count+=1
        else:
            check=stones[x]
    return count