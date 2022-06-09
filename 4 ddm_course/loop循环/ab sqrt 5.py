x = 1000
re,res = [],[]
for i in range(x):
    for j in range(x):
        re.append([i,j])
        if (i*i + j*j) % 5 == 0:
            res.append([i,j])
print(len(res),len(re))