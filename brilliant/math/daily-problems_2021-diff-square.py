'''
https://brilliant.org/daily-problems/2021-diff-square/
'''

year = 2021
years = 3000
ans = []
for i in range(years):
    for j in range(years):
        if (i+j) * (i-j) == year:
            ans.append([i,j])
print(ans)