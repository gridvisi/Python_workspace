'''
I'll tell you. It is a pair of two digit numbers whose product is equal to the reverse of the first number multiplied by the reverse of the second number.
For example-
{12} * {84} = {21} * {48}12∗84=21∗48
Now your job is to enter the number of such possible sequences (pairs).
'''
res = []
for i in range(1000):
    for j in range(1000):
        if i*j == int(str(i)[::-1])*int(str(j)[::-1]):
            if str(i) != str(i)[::-1] and str(j) != str(j)[::-1] and str(i) != str(j)[::-1] :
                res.append((i,j))
print(res)