def count_by(x, n):
    return [i for i in range(0,x*n+1,x)][1:]
print(count_by(100,5))