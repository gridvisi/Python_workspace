'''
https://www.geeksforgeeks.org/print-subsequences-string-iterative-method/

Examples:

Input : abc
Output : a, b, c, ab, ac, bc, abc

Input : aab
Output : a, b, aa, ab, aab
'''

'''
Approach 1 : 
Here, we discuss much easier and simpler iterative approach which is similar to Power Set. We use bit pattern from binary representation of 1 to 2^length(s) – 1.

input = “abc” 
Binary representation to consider 1 to (2^3-1), i.e 1 to 7. 
Start from left (MSB) to right (LSB) of binary representation and append characters from input string which corresponds to bit value 1 in binary representation to Final subsequence string sub.

Example: 
001 => abc . Only c corresponds to bit 1. So, subsequence = c. 
101 => abc . a and c corresponds to bit 1. So, subsequence = ac.
binary_representation (1) = 001 => c 
binary_representation (2) = 010 => b 
binary_representation (3) = 011 => bc 
binary_representation (4) = 100 => a 
binary_representation (5) = 101 => ac 
binary_representation (6) = 110 => ab 
binary_representation (7) = 111 => abc

方法1 : 
在这里，我们讨论更容易和更简单的迭代方法，它与Power Set相似。我们使用1到2^length(s)-1的二进制表示的比特模式。

输入 = "abc" 
二进制表示要考虑1到（2^3-1），即1到7。
从二进制表示的左边（MSB）到右边（LSB）开始，将输入字符串中与二进制表示中的比特值1相对应的字符附加到最终子序列字符串中。

例如。
001 => abc . 只有c对应于位1。所以，子序列=c。
101 => abc . a和c对应于位1。所以，子序列=ac。
二进制表示法(1) = 001 => c 
二进制表示法(2) = 010 => b 
binary_representation (3) = 011 => bc 
二进制代表(4) = 100 => a 
二进制表示法 (5) = 101 => AC 
二进制表示法 (6) = 110 => ab 
二进制表示法(7) = 111 => abc

通过www.DeepL.com/Translator（免费版）翻译
'''


# Python3 program to print all Subsequences
# of a string in iterative manner

# function to find subsequence
def subsequence(s, binary, length):
    sub = ""
    for j in range(length):

        # check if jth bit in binary is 1
        if (binary & (1 << j)):
            # if jth bit is 1, include it
            # in subsequence
            sub += s[j]
    return sub


# function to print all subsequences
def possibleSubsequences(s):
    # map to store subsequence
    # lexicographically by length
    sorted_subsequence = {}

    length = len(s)

    # Total number of non-empty subsequence
    # in string is 2^len-1
    limit = 2 ** length

    # i=0, corresponds to empty subsequence
    for i in range(1, limit):

        # subsequence for binary pattern i
        sub = subsequence(s, i, length)

        # storing sub in map
        if len(sub) in sorted_subsequence.keys():
            sorted_subsequence[len(sub)] = \
                tuple(list(sorted_subsequence[len(sub)]) + [sub])
        else:
            sorted_subsequence[len(sub)] = [sub]

    for it in sorted_subsequence:

        # it.first is length of Subsequence
        # it.second is set<string>
        print("Subsequences of length =", it, "are:")
        for ii in sorted(set(sorted_subsequence[it])):
            # ii is iterator of type set<string>
            print(ii, end=' ')
        print()


# Driver Code
s = "aabc"
possibleSubsequences(s)


'''
Time Complexity : O(2^{n} * l)      , where n is length of string to find subsequences and l is length of binary string.

Approach 2 : 
Approach is to get the position of rightmost set bit and and reset that bit after appending corresponding character from given string to the subsequence and will repeat the same thing till corresponding binary pattern has no set bits.

If input is s = “abc” 
Binary representation to consider 1 to (2^3-1), i.e 1 to 7. 
001 => abc . Only c corresponds to bit 1. So, subsequence = c 
101 => abc . a and c corresponds to bit 1. So, subsequence = ac.
Let us use Binary representation of 5, i.e 101. 
Rightmost bit is at position 1, append character at beginning of sub = c ,reset position 1 => 100 
Rightmost bit is at position 3, append character at beginning of sub = ac ,reset position 3 => 000 
As now we have no set bit left, we stop computing subsequence.

Example :
binary_representation (1) = 001 => c 
binary_representation (2) = 010 => b 
binary_representation (3) = 011 => bc 
binary_representation (4) = 100 => a 
binary_representation (5) = 101 => ac 
binary_representation (6) = 110 => ab 
binary_representation (7) = 111 => abc

Below is the implementation of above approach : 

时间复杂度：O(2^{n} * l)，其中n是寻找子序列的字符串长度，l是二进制字符串的长度。

方法2 : 
方法是在给定的字符串中添加相应的字符到子序列中后，得到最右边的设置位的位置，并重置该位，重复同样的事情，直到相应的二进制模式没有设置位。

如果输入是s = "abc" 
二进制表示要考虑1到（2^3-1），即1到7。
001 => abc 。只有c对应于位1。所以，子序列=c 
101 => abc . a和c对应于第1位。所以，子序列=ac。
让我们使用5的二进制表示，即101。
最右边的位在第1位，在子序列的开头添加字符 = c ,重置位置 1 => 100 
最右边的位在第3位，在子的开头添加字符 = ac ,重置位置3 => 000 
由于现在我们已经没有设置位了，我们停止计算子序列。

例子:
二进制表示法(1) = 001 => C 
binary_representation (2) = 010 => b 
binary_representation (3) = 011 => bc 
二进制表示法(4) = 100 => a 
二进制表示法 (5) = 101 => AC 
二进制表示法 (6) = 110 => ab 
二进制表示法(7) = 111 => abc

下面是上述方法的实现。
'''

# Python3 program to print all Subsequences
# of a string in an iterative manner
from math import log2, floor


# function to find subsequence
def subsequence(s, binary):
    sub = ""

    # loop while binary is greater than
    while (binary > 0):
        # get the position of rightmost set bit
        pos = floor(log2(binary & -binary) + 1)

        # append at beginning as we are
        # going from LSB to MSB
        sub = s[pos - 1] + sub

        # resets bit at pos in binary
        binary = (binary & ~(1 << (pos - 1)))

    sub = sub[::-1]
    return sub


# function to print all subsequences
def possibleSubsequences(s):
    # map to store subsequence
    # lexicographically by length
    sorted_subsequence = {}

    length = len(s)

    # Total number of non-empty subsequence
    # in string is 2^len-1
    limit = 2 ** length

    # i=0, corresponds to empty subsequence
    for i in range(1, limit):

        # subsequence for binary pattern i
        sub = subsequence(s, i)

        # storing sub in map
        if len(sub) in sorted_subsequence.keys():
            sorted_subsequence[len(sub)] = \
                tuple(list(sorted_subsequence[len(sub)]) + [sub])
        else:
            sorted_subsequence[len(sub)] = [sub]

    for it in sorted_subsequence:

        # it.first is length of Subsequence
        # it.second is set<string>
        print("Subsequences of length =", it, "are:")
        for ii in sorted(set(sorted_subsequence[it])):
            # ii is iterator of type set<string>
            print(ii, end=' ')
        print()


# Driver Code
s = "aabc"
possibleSubsequences(s)