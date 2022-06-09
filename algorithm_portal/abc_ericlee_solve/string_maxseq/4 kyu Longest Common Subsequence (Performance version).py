# https://www.codewars.com/kata/593ff8b39e1cc4bae9000070/train/python
'''
The longest common subsequence (LCS) problem is the problem of finding the longest subsequence common to all sequences in a set of sequences.
It differs from problems of finding common substrings: unlike substrings, subsequences are not required to occupy consecutive positions within the original sequences.

Task
Write a function lcs that accepts two strings and returns their longest common subsequence as a string. Performance matters.

Examples
lcs( "abcdef", "abc" ) => "abc"
lcs( "abcdef", "acf" ) => "acf"
lcs( "132535365", "123456789" ) => "12356"
lcs( "abcdefghijklmnopq", "apcdefghijklmnobq" ) => "acdefghijklmnoq"
Testing
This is a performance version of xDranik's kata of the same name.
This kata, however, has much more full and heavy testing. Intermediate random tests have string arguments of 20 characters; hard random tests 40 characters; extreme 60 characters (characters are chosen out of 36 different ones).

Notes
The subsequences of "abc" are "", "a", "b", "c", "ab", "ac", "bc", "abc".
"" is a valid subsequence in this kata, and a possible return value.
All inputs will be valid.
Two strings may have more than one longest common subsequence. When this occurs, return any of them.

lcs( string0, string1 ) === lcs( string1, string0 )
Wikipedia has an article that may be helpful.

最长共同子序列（LCS）问题是寻找一组序列中所有序列共同的最长子序列的问题。
它与寻找共同子串的问题不同：与子串不同，子串不需要在原始序列中占据连续位置。

任务
编写一个函数lcs，它接受两个字符串并将它们的最长共同子序列作为一个字符串返回。性能很重要。

例子
lcs( "abcdef", "abc" ) => "abc"
lcs( "abcdef", "acf" ) => "acf"
lcs( "132535365", "123456789" ) => "12356"
lcs( "abcdefghijklmnopq", "apcdefghijklmnobq" ) => "acdefghijklmnoq"
测试
这是xDranik的同名卡塔的一个表演版本。
然而，这个卡塔有更全面、更重的测试。中级随机测试有20个字符的字符串参数；高级随机测试有40个字符；极端测试有60个字符（从36个不同的字符中选择）。

注释
abc "的子序列是""、"a"、"b"、"c"、"ab"、"ac"、"bc"、"abc"。
""是这个卡塔的一个有效子序列，也是一个可能的返回值。
所有的输入都将是有效的。
两个字符串可能有一个以上的最长共同子序列。当这种情况发生时，返回其中任何一个。

lcs( string0, string1 ) === lcs( string1, string0 )
维基百科有一篇文章可能会有帮助。
'''

from itertools import product
def lcs(x, y):
    l, m = len(x), len(y)
    L = [[""] * (m + 1) for _ in range(l + 1)]
    for i, j in product(range(1, l + 1), range(1, m + 1)):
        L[i][j] = L[i - 1][j - 1] + x[i - 1] if x[i - 1] == y[j - 1] else max(L[i - 1][j], L[i][j - 1], key=len)
    return L[l][m]


'''

def lcs(x, y):
    i,j = 0,0
    x = [i for i in x if i in y]
    #x = [i for i in y if i in x]
    print(x)
    s = ''
    while i < len(x) and j < len(y):
        print(x[i],y[j])
        if x[i] != y[j]:
            if y[j] in x[i:] and x[i] in y[j:]:
                l,r = x[i:].index(y[j]),y[j:].index(x[i])
                if  l < r:
                    i += l
                    j += 1
                else:
                    j += r
                    i += 1
            else:

                if x[i] == y[j]:
                    s += y[j]
                    j += 1
                    i += 1
    return s

x,y = "anothertest", "notatest"  # "nottest")
print(lcs(x,y))
'''


# https://devtut.github.io/algorithm/substring-search.html#python-implementation-of-kmp-algorithm
def get_prefix_table(needle):
    prefix_set = set()
    n = len(needle)
    prefix_table = [0]*n
    delimeter = 1
    while(delimeter<n):
        prefix_set.add(needle[:delimeter])
        j = 1
        while(j<delimeter+1):
            if needle[j:delimeter+1] in prefix_set:
                prefix_table[delimeter] = delimeter - j + 1
                break
            j += 1
        delimeter += 1
    return prefix_table

def strstr(haystack, needle):
    # m: denoting the position within S where the prospective match for W begins
    # i: denoting the index of the currently considered character in W.
    haystack_len = len(haystack)
    needle_len = len(needle)
    if (needle_len > haystack_len) or (not haystack_len) or (not needle_len):
        return -1
    prefix_table = get_prefix_table(needle)
    m = i = 0
    while((i<needle_len) and (m<haystack_len)):
        if haystack[m] == needle[i]:
            i += 1
            m += 1
        else:
            if i != 0:
                i = prefix_table[i-1]
            else:
                m += 1
    if i==needle_len and haystack[m-1] == needle[i-1]:
        return m - needle_len
    else:
        return -1

if __name__ == '__main__':
    needle = 'abcaby'
    haystack = 'abxabcabcaby'
    needle,haystack = "nothardlythefinaltest", "zzzfinallyzzz" # "final")
    print(strstr(haystack, needle))
