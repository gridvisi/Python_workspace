'''
https://www.codewars.com/kata/59971e64bfccc70748000068/train/python

Test.it("Basic tests")
Test.assert_equals(convergence(3),5)
Test.assert_equals(convergence(5),6)
Test.assert_equals(convergence(10),5)
Test.assert_equals(convergence(15),2)
Test.assert_equals(convergence(500),29)
Test.assert_equals(convergence(5000),283)
'''
n = 15
print(set(list(str(n))))

#1st solution
def next(base):
    mul = 1
    for c in str(base):
        if c != "0":
            mul *= int(c)
    return base + mul


def convergence(n):
    base = 1
    test = n
    count = 0
    while test != base:
        if test > base:
            base = next(base)
        else:
            test = next(test)
            count += 1
        print(str(base) + " " + str(test))
    return count
n = 3
print(convergence(n))


#2nd solution
from operator import mul
from functools import reduce

def genSequence(n):
    yield n
    while True:
        n += reduce(mul, [int(d) for d in str(n) if d != '0']) if n > 9 else n
        yield n

def extract(seq, v):
    return sorted(seq).index(v)

def convergence(n):
    gen1, genN = genSequence(1), genSequence(n)
    seq1, seqN = {next(gen1)}, {next(genN)}
    while True:
        a,b = next(gen1), next(genN)
        seq1.add(a)
        seqN.add(b)
        if a in seqN: return extract(seqN, a)
        if b in seq1: return extract(seqN, b)




