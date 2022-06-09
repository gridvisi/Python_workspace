# for循环的嵌套
x = [i for i in range(10)]
print(x)

for i in x:
    for j in x:
        for k in x:
            if i + j + k == 9:
                print(i,j,k)