'''
A binary gap within a positive number num is any sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of num.
For example:
9 has binary representation 1001 and contains a binary gap of length 2.
529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3.
20 has binary representation 10100 and contains one binary gap of length 1.
15 has binary representation 1111 and has 0 binary gaps.
Write function gap(num) that, given a positive num, returns the length of its longest binary gap.
The function should return 0 if num doesn't contain a binary gap.
'''

def gap(num):
    s,re,large = bin(num),[],0
    for i,e in enumerate(s[2:]):
        if e == '1':
            re.append(i)
    large = re[1] - re[0]
    for j in range(len(re) - 1):
        if re[j+1] -re[j] > large:
            large = re[j+1] -re[j]
    return large-1,re
num = 15

def gap(num):
    s = bin(num)[2:].strip("0")
    return max(map(len, s.split("1")))
print(gap(num))

n = 171
print(bin(n)[2:].strip("0"))

str = "123abcrun12oob31123212"
print (str.strip( '2312' ))  # 字符序列为 12