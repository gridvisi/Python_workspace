def countBits(n):
    n = list(bin(n))
    n.remove('0')
    n.remove('b')
    return n.count('1')
print(countBits(4))