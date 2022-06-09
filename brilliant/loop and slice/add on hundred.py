print([i for i in range (10)])

def fibonacci(x):
    a,b = 1,1
    ans = []
    for i in range(x):
        ans.append(a)
        a,b = b,a+b
    return a,b,ans
x = 10
print(fibonacci(x))


