'''
https://www.codewars.com/kata/59a818191c55c44f3900053f/train/python
'''


def true_binary(n):
    binn = bin(n)[2:]
    '''
    x + y = int(0b + 1 * len(binn))
    x - y = n
    so that: 
    2x = int(0b + 1 * len(binn)) + n
    2y = int(0b + 1 * len(binn)) - n
    '''
    x = int('0b' + int(len(binn)) * '1',2) + n
    y = int('0b' + int(len(binn)) * '1',2) - n
    ans = [1 if i == '1' else -1 for i in str(bin(x//2)[2:])]

    return ans,binn,x/2,y/2

n = 25
print(true_binary(n))

#1
def true_binary(n):
    return [(c == '1') * 2 - 1 for c in '1' + bin(n)[2:-1]]