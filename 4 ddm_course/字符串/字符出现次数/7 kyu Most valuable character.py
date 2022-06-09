'''
https://www.codewars.com/kata/5dd5128f16eced000e4c42ba/train/python
在这个Kata中，你将得到一个字符串，你的任务是返回最有价值的字符。一个字符的价值是其最后出现的索引和第一次出现的索引之间的差异。
返回具有最高值的字符。如果出现并列，则返回按字母顺序排列的最低字符。对于Golang返回符文
所有的输入都是小写。例如
solve('a') ='a'
solve('ab') = 'a'。最后出现等于每个字符的第一次出现。按词法返回最低值。
solve("axyzxyz")='x'
多用测试用例。祝您好运!

In this Kata, you will be given a string and your task is to return the most valuable character.
The value of a character is the difference between the index of its last occurrence and the index
of its first occurrence. Return the character that has the highest value. If there is a tie,
return the alphabetically lowest character. [For Golang return rune]

All inputs will be lower case.

For example:
solve('a') = 'a'
solve('ab') = 'a'. Last occurrence is equal to first occurrence of each character. Return lexicographically lowest.
solve("axyzxyz") = 'x'
More examples in test cases. Good luck!
'''
from collections import Counter
def solve(st):
    gapMax = 0
    maxc = []
    for c in set(list(st)):
        print(st[::-1].find(c),st.find(c))
        gap = len(st)-1 - st[::-1].find(c) - st.find(c)
        print(gap)
        if gap >= gapMax:
            maxc.append((c,gap))#max(set(maxc),key=lambda x:x[1])
    return sorted(set(maxc),key=lambda x:x[1],reverse=True)[0][0]\

# sorted(set(maxc),key=lambda x:x[1],reverse=True)


#st = 'bcd'
#st = 'aabccc'
st = 'a'
#st = 'bcd'
st = "axyzxyz"


#1st solution
def solve(st):
    return sorted((st.find(c) - st.rfind(c), c) for c in set(st))[0][1]
print(solve(st))

#2nd solution
def solve(st):
    return min(set(st), key=lambda c: (st.index(c)-st.rindex(c), c))