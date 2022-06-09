# https://leetcode.com/problems/repeated-dna-sequences/description/
'''
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for
example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated
sequences within the DNA.
Write a function to find all the 10-letter-long sequences (substrings) that occur more
than once in a DNA molecule.
Example:
'''

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        seen = set()
        repeated = set()
        N = len(s)
        step = 7
        for i in range(0,N,step):
            cur = s[i: i+step]
            if cur in seen:
                repeated.add(cur)
            else:
                seen.add(cur)
        return list(repeated)

s = 'TACCCTGATACCTGATACCTGATACCTGATACCTGATACCT'
#s = 'TACTGATACTGATACTGATACTGATACTGATACTGAC'
myDNA = Solution()
print('myDNA:',myDNA.findRepeatedDnaSequences(s))

'''
# https://leetcode-cn.com/problems/minimum-window-substring/

给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：
包含 T 所有字符的最小子串。
示例：
输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"
说明：
如果 S 中不存这样的子串，则返回空字符串 ""。
如果 S 中存在这样的子串，我们保证它是唯一的答案。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-window-substring
#print(dna.split('TACTGATACCTGA'))
#print(dna.count('TACTGATACCTGA'))

class Solution:
    def minWindow(self, s: str, t: str) -> str:
'''

dna = 'TACCCTGATACCTGATACCTGATACCTGATACCTGATACCT'
#dna = 'TACTGATACTGATACTGATACTGATACTGATACTGAC'

#dna = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
def Repeatcur(dna):
    dnaSet = set(dna)
    #r = [dna[:i] for i in range(len(dna)) if set(dna[:i]) == set(dna)]
    for i in range(len(dna)):
        if set(dna[:i]) == set(dna):
            #if dna[:i] == dna[i:2*i]
            return i,dna[:i]
print(Repeatcur(dna))



def repeatedSubstring(dna):
    """
    :type s: str
    :rtype: bool
    """
    s = dna
    n = len(s)
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            a = s[:i]
            j = i
            while j < n and s[j:j + i] == a:
                j += i
                if j == n: return s[i:j]
    return i,j,f"{s[j:i]}",False
print('repeatedSubstring(dna):',repeatedSubstring(dna))

def key(dna):
    res = list(iter(dna))
    i, j = 0, 1
    while i < len(res) and j < len(res):
        if res[i] == res[j]:
            i += 1
            j += 1
        elif res[i] != res[j]:
            j += 1
    return ''.join(str(i) for i in res[0:j - i])
#print(key(dna))


class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                a = s[:i]
                j = i
                while j < n and s[j:j + i] == a:
                    j += i
                if j == n: return True
        return False

# Judge repeat string : repeatedSubstringPattern(self, s)
def repeatedSubstringPattern(s):
    """
    :type s: str
    :rtype: bool
    """
    n = len(s)
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            a = s[:i]
            j = i
            while j < n and s[j:j + i] == a:
                j += i
                if j == n: return True
    return False
s = 'TACCTGATACCTGATACCTGATACCTGATACCTGA'
print('repeatedSubstringPattern:',repeatedSubstringPattern(s))


# class define
class Person(object):
    """人类"""
    def __init__(self, name , age):
        self.name = name
        self.age = age

p = Person('小黑',18)
print('p.name,p.age ',p.name,p.age)

print("# __str__()这个特殊方法会在尝试将对象转换为字符串的时候调用")
# 定义一个Person类
class Person(object):
    """人类"""
    def __init__(self, name , age):
        self.name = name
        self.age = age

    # __str__()这个特殊方法会在尝试将对象转换为字符串的时候调用
    # 它的作用可以用来指定对象转换为字符串的结果print函数
    def __str__(self):
        #print(Person)
        return f"{self.name}"+' Person [name=%s , age=%d]'%(self.name,self.age)

p = Person('钢铁侠',18)
print(p)
