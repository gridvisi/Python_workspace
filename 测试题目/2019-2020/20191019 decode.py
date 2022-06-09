

xs = 'jerryisspy'
xs = 'apple'
xs = 'banana'
step  = 9
xs = 'kjwjwj'
def shift(xs,step):
    res = ''
    for i in xs:
        x_asc = chr(ord(i) - step)
        res += x_asc  #为何这样写
    return res

print(shift(xs,step))

print(sum([i for i in range(100)]))
print([i for i in range(100)])

