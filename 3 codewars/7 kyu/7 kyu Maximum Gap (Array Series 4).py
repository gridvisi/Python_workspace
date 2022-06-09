
# https://www.codewars.com/kata/maximum-gap-array-series-number-4/train/python

numbers =  [-54,37,0,64,-15,640,0]
print(sorted(numbers))

def max_gap(numbers):
    s,sn = [],sorted(numbers)
    for i,e in enumerate(sn):
        if i + 1 < len(numbers):
            s.append(sn[i+1] - sn[i])
    return max(s)

def max_gap(numbers):
    lst = sorted(numbers)
    return max(b-a for a,b in zip(lst, lst[1:]))

import numpy
def max_gap(numbers):
    return max(numpy.diff(sorted(numbers)))

def max_gap(numbers):
    sorted_n = sorted(numbers)
    return max([sorted_n[i]-sorted_n[i-1] for i in range(1, len(sorted_n))])

print(max_gap(numbers))