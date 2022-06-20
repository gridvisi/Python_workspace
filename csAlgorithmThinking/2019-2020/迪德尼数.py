

n = 10000
print(sum(int(i) for i in list(str(n**3))))

def dudeney(n):
    return list(filter(lambda i: sum(int(i) for i in list(str(i**3))) == i, range(1,n)))
print(dudeney(n))