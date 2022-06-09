# https://www.codewars.com/kata/57c1f22d8fbb9fd88700009b/train/python

def maxlen(L1,L2):
    l,s = max(L1,L2),min(L1,L2)
    if l == s: return l//2
    elif l/2 < s: return l/2
    elif l/2 > s and l/3 < s: return s
    elif l/3 > s: return l/3

#1st solution
def maxlen(s1, s2):
    sm, lg = sorted((s1, s2))
    return min(max(lg / 3, sm), lg / 2)


def maxlen(L1,L2):
    #if max(L1,L2)//min(L1,L2) == 2:
     #   return min(L1,L2)
    return max((L1+L2)//3,3*max(L1,L2)//(L1+L2))

L1, L2 = 5,12
#L1, L2 = 2,12
L1, L2 = 5,10
print(maxlen(L1,L2))

def maxlen(L1,L2):

    # return maximal length
    bench = (L1 + L2) // 3
    if bench == max(L1,L2)//3:
        return bench
    else:
        while True:
            if L1 >= bench and L2 >= bench:
                return bench
            else:
                bench -= 1
L1, L2 = 5,12
L1, L2 = 2,12
print(maxlen(L1,L2))