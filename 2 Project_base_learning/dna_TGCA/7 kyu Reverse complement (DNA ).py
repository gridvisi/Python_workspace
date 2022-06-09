'''
https://www.codewars.com/kata/574a7d0dca4a8a0fbe000100/train/python
在遗传学中，序列的反向补码是通过将序列反转，然后取每个符号的补码形成的。

DNA中的四种核苷酸是腺嘌呤（A）、胞嘧啶（C）、鸟嘌呤（G）和胸腺嘧啶（Thymine）。

A是T的补码
C是G的补数。
这是一个双向关系，所以。

T是A的补数
G是C的补码。
对于这个卡塔，你需要完成反向补码函数，即取一个DNA字符串并返回反向补码字符串。

注意：你需要注意大写和小写。如果一个序列包含一些无效字符，你需要返回 "无效序列"。

这个卡塔是基于下面的卡塔，但增加了一个小步骤。
In genetic the reverse complement of a sequence is formed by reversing the sequence
and then taking the complement of each symbol.

The four nucleotides in DNA is Adenine (A), Cytosine (C), Guanine (G) and Thymine
(Thymine).

A is the complement of T
C is the complement of G.
This is a bi-directional relation so:

T is the complement of A
G is the complement of C.
For this kata you need to complete the reverse complement function that take a DNA string
and return the reverse complement string.

Note: You need to take care of lower and upper case. And if a sequence conatains some
invalid characters you need to return "Invalid sequence".

This kata is based on the following one but with a little step in addition.
'''

def reverse_complement(dna):
    encode = {'A':'T','T':'A','C':'G','G':'C'}
    for i in dna:
        if i not in 'GACT':return "Invalid sequence"
    return ''.join([encode.get(i,'') for i in dna[::-1]])
dna = "GACTGACTGTA"
dna = "xyz"
dna = ''
print(reverse_complement(dna))

#1st
from string import maketrans

def reverse_complement(dna):
    if len(dna.translate(None, "ATGC")) > 0:
        return "Invalid sequence"
    return dna.translate(maketrans("ATCG","TAGC"))[::-1]

#2nd
get = dict(zip("ATCG", "TAGC")).__getitem__

def reverse_complement(dna):
    try:
        return ''.join(map(get, reversed(dna)))
    except KeyError:
        return "Invalid sequence"

#3rd
def reverse_complement(dna):
    # your code here
    reverse = {'A': 'T', 'T':'A', 'C':'G', 'G':'C'}
    r_c = ''
    for nucl in reversed(dna):
        if nucl not in reverse:
            return "Invalid sequence"
        else: r_c += reverse[nucl]
    return r_c