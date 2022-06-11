'''
There are some stones on Bob's table in a row, and each
of them can be red, green or blue, indicated by the
characters R, G, and B.

Help Bob find the minimum number of stones he needs to
remove from the table so that the stones in each pair
of adjacent stones have different colours.

Examples:

"RGBRGBRGGB"   => 1
"RGGRGBBRGRR"  => 3
"RRRRGGGGBBBB" => 9

'''

def solution(stones):
    # Do some magic
    cunt = 0
    start = stones[0]
    for i in range(1,len(stones)):
        if start == stones[i]:
            cunt += 1
        elif start != stones[i]:
            start = stones[i]
    return cunt

#1st
def solution(s):
    st=[1 for i in range(1,len(s)) if s[i-1]==s[i]]
    return sum(st)

#2nd
def solution(stones):
    return sum(a==b for a,b in zip(stones, stones[1:]))

#3rd
from itertools import groupby
def solution(stones):
    return sum(len(list(grp))-1 for _, grp in groupby(stones))