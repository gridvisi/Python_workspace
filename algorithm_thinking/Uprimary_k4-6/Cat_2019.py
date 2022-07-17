
'''

'''

s = [4, 7, 5, 6, 8, 2, 1, 3]
def fusing(s,ans = []):
    step = len(s)

    while step > 1:
        for i in range(0,len(s),2):

            x,y = max(s[i],s[i+1]),min(s[i],s[i+1])
            ans.append(int(str(x) + str(y)))
        s = ans
        step /= 2
    if step == 1: return str(s[-1])[-1],str(s[-1])
    return fusing(ans)
print(fusing(s))