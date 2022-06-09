
seq = [1,2,3,5,6,7,9,11,12]

ans = []
for i in range(seq[0],seq[-1]+1):
    if i not in seq:
        ans.append(i)

print(ans)