'''
https://brilliant.org/problems/growing-digits/
The above is an incomplete cryptogram, where AA is a positive, single-digit integer.
As shown, the final sum is a 5-digit number.

What is this final sum?
'''

n = [i for i in range(1,10)]
def cryptogram(n,step):
    sub,res = 0,[]
    for x in n:
        sub = 0
        for i in range(1, step+1):
            print(sub)
            sub += int(i*str(x))
            re = (x,sub)
        res.append(re)
    return res
step = 4
print(cryptogram(n,step))