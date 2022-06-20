ls = [1,2,3,4]
def foo(x):
    ls[3] = x
    return ls
x = 5
print(foo(x))
print(ls)