'''
https://brilliant.org/daily-problems/cryptogram-even-odd/
'''

ans = []
for num in range(100,1000):
    if eval(str(num)[-1])%2==1:
        if eval(str(num)[-1] + str(num)[0]) %2 == 0:
            ans.append(str(num)[1])
print(ans)
