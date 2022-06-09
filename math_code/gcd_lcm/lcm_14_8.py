
#https://brilliant.org/daily-problems/number-intersection/

#
x,y,ceil = 14,8,500

def lcm(x,y,ceil):
    ans = []
    x,y = min(x,y),max(x,y)
    for i in range(x,ceil,x):
        if i % y == 0:
            ans.append(i)
    return ans,len(ans)
print(lcm(x,y,ceil))