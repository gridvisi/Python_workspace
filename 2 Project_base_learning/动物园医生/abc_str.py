__author__ = 'Administrator'

# I would recommend always using parentheses
# to indicate start and end of tuple
# even though parentheses are optional.
# Explicit is better than implicit.
zoo = ('python', 'elephant', 'penguin')
print('Number of animals in the zoo is', len(zoo))

new_zoo = 'monkey', 'camel', zoo    # parentheses not required but are a good idea
print('Number of cages in the new zoo is', len(new_zoo))
print('All animals in new zoo are', new_zoo)
print('Animals brought from old zoo are', new_zoo[2])
print('Last animal brought from old zoo is', new_zoo[2][2])
print('Number of animals in the new zoo is',
      len(new_zoo)-1+len(new_zoo[2]))

'''
a = 1234
A = str(a)
b = "abcd"
s = str(a)
print(A[2])
print(s)

x = 123423434
def sumdigit(x):
    j = len(str(x))
    char = str(x)
    total = 0
    for i in j:
        total += char[i]
    return total

print(sumdigit(x))
'''
# 整数各位数求和直至位个位数
# class


def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = str(num)
        res = 0
        for i in s:
            res += int(i)
        while res > 9:
            s = str(res)
            res = 0
            for i in s:
                res += int(i)
        return res

print(addDigits(0,234345))