#https://www.codewars.com/kata/57507369b0b6d1b5a60001b3/train/python
'''
test.describe("Basic tests")
test.assert_equals(decompose_single_strand("AGGTGACACCGCAAGCCTTATATTAGC"),
"Frame 1: AGG TGA CAC CGC AAG CCT TAT ATT AGC\n
Frame 2: A GGT GAC ACC GCA AGC CTT ATA TTA GC\n
Frame 3: AG GTG ACA CCG CAA GCC TTA TAT TAG C")

遗传学中，阅读框架是将核苷酸（DNA碱基）序列划分为一组连续的、不重叠的三联体（也称为密码子）的一种方式。在翻译过程中，每个三联体都被翻译成一种氨基酸，以创造蛋白质。

输入
在一条DNA链中，你可以找到3个阅读框，以下面的输入序列为例。

Agtgacaccgcaagccttatattagc
输出
对于输出，我们将采取组合方式，并以下列方式显示。

框架1：AGG TGA CAC CGC AAG CCT TAT ATT AGC
框架1：AGG TGA CAC CGC AAG CCT TAT ATT AGC
框架2：A GGT GAC ACC GCA AGC CTT ATA TTA GC
框架3：AG GTG ACA CCG CAA GCC TTA TAT TAG C
对于第1帧，从第一个基数（字母）开始，将所有这些字母分成三组。

对于第2帧，将它们分成三组，从第二个基数（字母）开始，但第一基数（字母）在开头。

对于第3帧，将它们分成三组，从第三个字母开始，但第一和第二基数（字母）以相同的
顺序在开始。

系列
将单链DNA分解成3个阅读框

将双链DNA分解成6个阅读框

在6个框架内将DNA翻译成蛋白质
'''


def decompose_single_strand(dna):
    return '\n'.join('Frame {}: {}'.format(k + 1, frame(dna, k)) for k in range(3))


def frame(s, k):
    return ' '.join(([s[:k]] if k else []) + [s[i:i + 3] for i in range(k, len(s), 3)])

single_strand = "AGGTGACACCGCAAGCCTTATATTAGC"

print(decompose_single_strand(single_strand))
