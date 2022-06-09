__author__ = 'Administrator'
'''
When 31513 and 34369 are each divided by a certain three-digit number, the remainders are equal. Find this remainder.'''

print(10%3)

for i in range (100,int(31513/2)):
    if 31513 % i == 34369 % i:
        print(i,int(31513/i),31513 % i)
'''
A particularly long integer ends with an 8. Shifting this 8 digit to the leftmost position creates
new number which is twice the original. Find the smallest possible value of the original number.
Clarification: This 8-shift procedure looks as follows: shift 8
'''

for j in range(1000000000000000):
    if 2 * (10*j + 8) == 80 * 10**len(str(j)) + j:
        print('smallest:',j)

'''
 将四位数的数字顺序重新排列后，可以得到一些新的四位数。现有一个四位数码互不相同，且没有0的四位数M，它比新数中最大的小3834，
 比新数中最小的大4338。求这个四位数
'''

for k in range(1000,10000):
