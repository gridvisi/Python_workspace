def bit_flip(a,b,c):
    return a or b and c
#a,b,c = 0,0,1
res = []
for a in (0,1):
    for b in (0,1):
        for c in (0,1):
            res.append((a,b,c,bit_flip(a,b,c)))
print(res)

input = [bin(i)[2:]  for i in range(8)]
#input = [i for i in range(10)]
print(input)
print(bit_flip(a,b,c))