'''
https://www.codewars.com/kata/5832db03d5bafb7d96000107/train/python

Your task is to write an update for a lottery machine. Its current version produces a sequence
of random letters and integers (passed as a string to the function). Your code must filter out
all letters and return unique integers as a string, in their order of first appearance.
If there are no integers in the string return "One more run!"
你的任务是为一台彩票机写一个更新。它的当前版本产生一个随机字母和整数的序列（以字符串形式传递给函数）。你的代码必须过滤掉所有的字母，
并以字符串的形式返回唯一的整数，按照它们首次出现的顺序。如果字符串中没有整数，则返回 "再跑一次！"
Examples
"hPrBKWDH8yc6Lt5NQZWQ"  -->  "865"
"ynMAisVpHEqpqHBqTrwH"  -->  "One more run!"
"555"                   -->  "5"
FUNDAMENTALSSTRINGS

Test.assert_equals(lottery("wQ8Hy0y5m5oshQPeRCkG"), "805")
Test.assert_equals(lottery("ffaQtaRFKeGIIBIcSJtg"), "One more run!")
'''

age = {'ada':11,'bob':10,'candy':13}
#print(sorted(age,key=age.values()))
ages = ['11','13','11','10','13']
print(sorted(set(ages)))
print(sorted(ages,key=ages.index))
print([x for x in sorted(set(ages),key=ages.index)])

#11th solution by ericlee
def lottery(s):
    ans = ''
    st = ''.join([i for i in s if i.isdigit()])
    for c in st:
        if c not in ans:
            ans += c
    return "One more run!" if not st else ans

s = "wQ8Hy0y5m5oshQPeRCkG"
print(lottery(s))

#1st solution
def lottery(s):
    return "".join(dict.fromkeys(filter(str.isdigit, s))) or "One more run!"

def lottery(stg):
    return "".join(c for c in sorted(set(stg), key=stg.index) if c.isdecimal()) or "One more run!"

def lottery(s):
    seen = set()
    return ''.join(seen.add(a) or a for a in s if a.isdigit() and a not in seen) or "One more run!"


