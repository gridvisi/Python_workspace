ls = [1,2,3,4]
def foo(x):
    ls[3] = x
    return ls
x = 5
print(foo(x))
print(ls)

def foo(x):
    def too(y):
        return x*y
    return too
x,y = 2,3
print(foo(x))#,too(y))
print(foo(x)(y))