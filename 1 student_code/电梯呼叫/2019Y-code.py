
s = 'lzj'
sl = s[1:]
print(sl)

#
ans = ''
for i in range(len(s)):
    if i!=0 and i != len(s)-1:
        ans += s[i]
print(ans)





left,mid,right,high,low,call = 4,6,2,8,12,3

floor_name = [str(i) for i in [left,mid,right,high,low,call]]
#floor_name = ['left','mid','right','high','low','call']

def elevator(floor_num):

    minf = float('inf')
    floor_name = ['left', 'mid', 'right', 'high', 'low', 'call']
    floor = dict(zip(floor_name,floor_num))
    return min([(k,abs(floor['call'] - floor[k])) for k,v in floor.items() if k != 'call'],key=lambda x:x[1])

floor_num = [4,6,2,8,12,3]
print(elevator(floor_num))