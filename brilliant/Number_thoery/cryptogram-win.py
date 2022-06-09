'''
https://brilliant.org/daily-problems/cryptogram-win/

(10*i + n)*(10*i + n) = w*100 + 10*i + n
100*i*i + 20*i*n + n*n = w*100 + 10*i + n
100*(i**2 - w) + 10*i*(2*n - 1) + n*(n-1) == 0


if i*i == w and 20*n == 10 and n*n = n
    20*i + 1 == 10*i +1
so that n != 1: since n==1 not satisfied with 20*n == 10

if n == 5:
    20*n + 20 + 5 == 10*i + 5
    20*(n+1) == 10*i
    n+1 == i/2,  i == 12

if n == 6:
    20*6 + 30 + 6 == 10*i + 6
    2*6 + 3 = i
'''

for i in range(10,100):
    if str(i**2)[1:] == str(i):
        print(i)


