



def multiply(a, b):
    return a * b
a = 1
b = 2
x = multiply(a, b)
print(x)
c = 9
d = 10
y = multiply(c, d)
def add(x,y):
    return x + y

print(add(2,7))

a ,b, h = 9, 4, 3

s = 2*(a*b + b*h + a*h)
print("面积：",s)

a = [1,2,4,5,6]
b = [2,5,7,3,9]
h = [6,9,2,8,5]

seq = []
for i in range(len(a)):
    s1 = multiply(a[i],b[i])
    s2 = multiply(b[i],h[i])
    s3 = multiply(a[i],h[i])
    s = (s1 + s2 + s3) * 2
    seq.append(s)
print(seq)






def add(a, b):
    pass


def subtract(a, b):
    pass





def divide(a, b):
    pass

