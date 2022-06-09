'''
https://www.codewars.com/kata/55fd2d567d94ac3bc9000064/train/python
          1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...

'''

def row_sum_odd_numbers(n):
    left = 1
    for i in range(1,n):
        #print(left)
        left = i*2 + left
    return [left+2*j for j in range(n)]
n = 5
print(row_sum_odd_numbers(n))

def row_sum_odd_numbers(n):
    #your code here
    return n ** 3