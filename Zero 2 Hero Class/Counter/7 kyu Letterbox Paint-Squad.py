'''
https://www.codewars.com/kata/597d75744f4190857a00008d/solutions/python


'''

def paint_letterboxes(start, finish):
    d = [str(i) for i in range(10)]
    st = ''.join([str(n) for n in range(start,finish+1)])
    return [st.count(i) for i in d]

#1st
def paint_letterboxes(start, finish):
    xs = [0] * 10
    for n in range(start, finish+1):
        for i in str(n):
            xs[int(i)] += 1
    return xs

#2nd
from collections import Counter

def paint_letterboxes(s, f):
    a = Counter("".join(map(str, range(s, f+1))))
    return [a[x] for x in "0123456789"]
