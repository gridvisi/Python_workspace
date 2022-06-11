# https://www.codewars.com/kata/5581a7651185fe13190000ee/train/python

def pattern(n):
    ans = ' '
    # line = list(''*(2*n - 2)).extend("\n") #'NoneType' object does not support item assignment
    line = list(' '*(2*n - 1))
    #print('*'.join(line))
    for i in range(n):
        line[n-i:] = [str(i) for i in list(range(1,n+1))]
        ans += ''.join(line)+ "\n"

    return ans
n = 5
print(pattern(n))