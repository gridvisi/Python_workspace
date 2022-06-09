'''
https://brilliant.org/daily-problems/passing-trains/
'''

def train_len(vl,vr,last,gap):
    # output the left or right head's length of train
    # left + right = (vl + vr) * last
    # left/vl - right/vr = gap ...(1)

    # left/vr + right/vr = (vl + vr) * last/vr  ...(2)
    # (1) + (2) = left/vl + left/vr = gap + (vl + vr) * last/vr
    left = gap*vl*vr/(vl + vr) + vl*vr*last/vr
    return left,(vl + vr) * last - left,(vl + vr) * last

vl,vr,last,gap = 20,30,20,10
print(train_len(vl,vr,last,gap))

#yellow and blue
def train_len(vb,vy,last,gap):
    # output the yellow train's length of train
    # yellow + blue = (vy + vb) * last
    # yellow/vl - blue/vr = gap ...(1)

    # yellow/vr + blue/vr = (vy + vb) * last/vr  ...(2)
    # (1) + (2) = yellow/vl + blue/vr = gap + (vy + vb) * last/vr
    blue = gap*vb*vy/(vb + vy) + vb*vy*last/vy
    return blue,(vb + vy) * last - blue,(vb + vy) * last

vb,vy,last,gap = 20,30,20,10
print(train_len(vb,vy,last,gap))