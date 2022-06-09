import math
a = 6
b = 7.54
c = 8+0.54
d = 0*4
e = float("inf")
f = float("NaN")

print(math.isfinite(a))
print(math.isfinite(b))
print(math.isfinite(c))
print(math.isfinite(d))
print(math.isfinite(e))
print(math.isfinite(f))
#print(math.isfinite('Nano'))


num = input ("Enter number:")
print(num)
# Printing type of input value
print ("type of number", type(num))

# taking two inputs at a time
x, y = input("Enter a two value: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)
print()