import sys
def gen():
   n = 0
   while n < 10:
     yield n
     n += 1

a = [0,1,2,3,4,5,6,7,8,9]
b = range(10)  # b is a range object, which is a iterable
c = gen()    # c is a iterator, which is a iterable too
print(sys.getsizeof(a))
#144
print(sys.getsizeof(b))
#48
print(sys.getsizeof(c))
#72

B = list(b)
C = list(c)
print(a)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(B)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(C)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sys.getsizeof(B))
#200

print(sys.getsizeof(C))
#160