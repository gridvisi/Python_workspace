
def num_primorial(n):
    p = []
    val = 2
    while len(p) < n:
        for div in p:
            print('div:',div,p)
            if val%div==0:
                val += 1
                break
        else:
            p.append(val)
    return p

n = 17
print(num_primorial(n))