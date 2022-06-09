'''
https://www.codewars.com/kata/5f5da7a415fbdc0001ae3c69/train/python

is_in_middle("AAabcBB")  ->  True
is_in_middle("AabcBB")   ->  True
is_in_middle("AabcBBB")  ->  False
'''
sequence = "AAaabcBXabcXbcAAaab"

sequence = "AAaaabcBX"
sequence = "AAaabcBabcabcabcbcAAaab"


#1st solution
def is_in_middle(seq):
    mid, rem = divmod(len(seq), 2)
    start = mid - 1
    end = start + 3
    if not rem:
        start -= 1
    return 'abc' in seq[start:end]

#2rd solution
def is_in_middle(sequence):
    n = len(sequence)
    i = (n - 3) // 2
    return sequence[i:i+3] == 'abc' or (n % 2 == 0 and sequence[i+1:i+4] == 'abc')

import re
def is_in_middle(sequence):
    pattern = 'abc'
    result = re.search(pattern,sequence)
    #print(result.span())
    result = re.finditer(pattern,sequence)
    #print(result)
    for id in result:
        print(id.span())
        l,r = id.span()[0],len(sequence) - id.span()[1]
        if abs(l - r) <= 1:
            return True
    return False
print(is_in_middle(sequence))


def is_in_middle(sequence):
    sq = sequence.split('abc')
    for i in range(len(sq)-1):
        l = sequence.find(sq[i])+len(sq[i])
        r = len(sequence) - sequence.find(sq[i + 1])
        print(l, r)
        if abs(l-r) <= 1:
            return True
    return False
print(is_in_middle(sequence))


def is_in_middle(sequence):
     l, r = sequence.find('abc'), sequence[::-1].rindex('abc'[::-1])
    # if abs(l -r) <= 1:
    #    return True
    # else:
    #    return False



def is_in_middle(sequence):
    #index = sequence.find('abc')
    #l,r = sequence.find('abc'),sequence.rfind('abc'),sequence.rindex('abc')
    sq = sequence.split('abc')
    print(sq)
    for i in range(len(sq)):
        lsq, rsq = [sq[:i] for i in range(len(sq))],[sq[i:] for i in range(len(sq))]
        if abs(len(lsq) - len(rsq)):
            return True
    return False

print(is_in_middle(sequence))

'''
解释
rfind() 返回字符串最后一次出现的索引，如果没有匹配项则返回-1
find() 返回字符串第一次出现的索引，如果没有匹配项则返回-1
两者句法相同

句法
str_super.rfind(substr, start,end)
substr：想要查找的字符串
start：开始查找的索引，并且包含此索引
end：结束查找的索引，并且不包含此索引
str_super：想要查找substr的字符串
'''

import re
print("***************查找一个匹配串******************")
s = "i love python very much, python is my favorite."
pat = 'python'
result = re.search(pat,s)
print(result)
print(result.span())
print("*********************************")
result = re.finditer(pat,s)
print(result)
for i in result:
	print(i.span())
print("*********************************")