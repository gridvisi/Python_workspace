'''
https://www.codewars.com/kata/5299413901337c637e000004/train/python

Fellow code warrior, we need your help! We seem to have lost one of our sequence elements,
and we need your help to retrieve it!

Our sequence given was supposed to contain all of the integers from 0 to 9 (in no particular
order), but one of them seems to be missing.

Write a function that accepts a sequence of unique integers between 0 and 9 (inclusive),
and returns the missing element.

Examples:
[0, 5, 1, 3, 2, 9, 7, 6, 4] --> 8
[9, 2, 4, 5, 7, 0, 8, 6, 1] --> 3
'''
seq = [0, 5, 1, 3, 2, 9, 7, 6, 4]
print(range(seq[0],seq[-1]+1))

def get_missing_element(seq):
    seq = sorted(seq)
    ans = sum([i for i in range(10)]) - sum(seq)
    return ans

def get_missing_element(seq):
    seq = sorted(seq)
    return sum([i for i in range(seq[0],seq[-1]+1)]) - sum(seq)
seq = [9, 2, 4, 5, 7, 0, 8, 6, 1]
print(get_missing_element(seq))


def get_missing_element(seq):
    sq = sorted(seq)
    start = sq[0]
    for n in sq:
        if n != start:
            return start
        start += 1
seq = [9, 2, 4, 5, 7, 0, 8, 6, 1]
print(get_missing_element(seq))

def get_missing_element(seq):
    # your code here
    return [i for i in range(sorted(seq)[0],sorted(seq)[-1]+1) if i not in seq][0]

def get_missing_element(seq):
    sq = sorted(seq)
    for i in range(1,len(sq)):
        if sq[i] - sq[i-1] != 1:
            return (sq[i]+sq[i-1])//2

seq = [9, 2, 4, 5, 7, 0, 8, 6, 1]
print(get_missing_element(seq))

#1st
def get_missing_element(seq):
    return 45 - sum(seq)